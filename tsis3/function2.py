# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def func1(movie_name):
	for movie in movies:
		if movie["name"] == movie_name:
			if movie["imdb"] > 5.5:
				return True
			else:
				return False
	print("There is no film with that name!")

#print(func1("Exam"))

def func2():
	sublist = []
	for movie in movies:
		if movie["imdb"] > 5.5:
			sublist.append(movie["name"])
	return sublist

#print(func2())

def func3(category_name):
	films = []
	for movie in movies:
		if movie["category"] == category_name:
			films.append(movie["name"])
	return films

#print(func3("Romance"))

def func4(films):
	avr = 0
	Len = 0
	for movie in movies:
		if movie["name"] in films:
			avr += movie["imdb"]
			Len += 1
	avr /= Len
	return avr

#print(func4(["We Two", "Exam", "Colonia"]))

def func5(category_name):
	avr = 0
	Len = 0
	for movie in movies:
		if movie["category"] == category_name:
			avr += movie["imdb"]
			Len += 1
	avr /= Len
	return avr

#print(func5("Romance"))
