import requests
import collections

MovieResult = collections.namedtuple(
	'MovieResult',
	'Title,Poster,Type,imdbID,Year'
)


class MovieClient:
	def __init__(self, search_text):

		if not search_text or not search_text.strip():
			raise ValueError('You must specify a search string.')

		self.search_text = search_text

	def perform_search(self):
		url = 'http://www.omdbapi.com/?s={}&y=&plot=short&r=json'.format(self.search_text)

		r = requests.get(url)
		data = r.json()

		results = data['Search']

	#movies = []   ***NON-PYTHONIC WAY TO POPULATE LIST
#for result in results:
#	m = MovieResult(
#		Title=result['Title'],
#		Poster=result['Poster'],
#		Type=result['Type'],
#		imdbID=result['imdbID'],
#		Year=result['Year']
#	)
#	movies.append(m)'''

# def method_with_kws(pos1, **kwargs)
# pass

#movies = []   ***AN IMPROVEMENT, BUT STILL NOT BEST PYTHONIC WAY...
#for result in results:
#	m = MovieResult(**result)
#	movies.append(m)'''

		movies = [
			MovieResult(**m) 
			for m in results
			]

		movies.sort(key=lambda m: m.Title)

		return movies
