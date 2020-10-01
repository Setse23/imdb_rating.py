import requests
from bs4 import BeautifulSoup
from string import ascii_letters

movie = input("\nWhat movie do you what to see the rating for? > ")
source = requests.get(f'https://imdb.com/find?q={movie}&s=tt').text
soup = BeautifulSoup(source, 'lxml')

class MovieRating():
	def __init__(self, num_of_movies, lst):
		self.num_of_movies = num_of_movies
		self.lst = lst
		

	def appending_movies(self, soup):
		for title in soup.find_all('tr'):
			if self.num_of_movies > 0:
				self.lst.append(title.text)
				self.num_of_movies -= 1

		return self.lst

	def user_movie_input(self):
		print('\n---------------MOVIES--------------')
		for counter, film in enumerate(self.lst, 1):
			print(f'{counter} -> {film.strip()}')

		print()
		user_movie = int(input("Enter the number of the movie that is your pick > "))
		user_movie = list(enumerate(self.lst, 1))[user_movie - 1]
		print()

		user_movie = user_movie[1].strip()
		return user_movie

	def new_webpage(self):
		index_list =[]

		user_movie = MovieRating.user_movie_input(self)
		for link in soup.find_all('td', class_='result_text'):
			if link.text.strip() == user_movie:
				new_link = link.find('a')

		new_link = new_link['href']

		new_source = requests.get(f'https://www.imdb.com{new_link}').text
		return new_source

	def give_rating(self):
		new_source = MovieRating.new_webpage(self)
		new_soup = BeautifulSoup(new_source, 'lxml')

		for rating in new_soup.find_all('div' , {'class' : 'ratingValue'}):
			rating = rating.strong.text

		for raters in new_soup.find_all('span', {'class' : 'small'}):
			raters = raters.text
			
		return("\n{} based on {} user ratings.\n".format(rating, raters))

program = MovieRating(10, [])

program.appending_movies(soup)
print(program.give_rating())