import requests
import bs4
# import collections

def main():
	url = get_url_from_user()
	the_html = get_html_from_web(url)
	get_info_from_html(the_html)


def get_url_from_user():
	# the_url = input('What is the name of the website you want to scrape? ')
	# the_url = 'http://www.aavso.org'
	the_url = 'http://www.teamfortress.com/'
	return the_url


def get_html_from_web(a_url):
	response = requests.get(a_url)
	return response.text

def get_info_from_html(html):
	soup = bs4.BeautifulSoup(html, "html5lib")
	comic = soup.find(id='leftColPosts').get_text()

	comic = cleanup_text(comic)
	print(comic)
	type(comic)	

def cleanup_text(messy : str):
	if not messy:
		return messy

	messy = messy.strip()
	return messy
				


if __name__ == '__main__':
	main()	
