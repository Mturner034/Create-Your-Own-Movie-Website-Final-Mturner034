import fresh_tomatoes
import media 

toy_story = media.Movie(movie_title = "Toy Story",
						movie_storyline = "A story of a boy and his toys that come to life",
						poster_image_url = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						trailer_youtube_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(movie_title ="Avatar",
					 movie_storyline = "A marine on an alien planet",
					 poster_image_url ="https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 trailer_youtube_url = "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_matrix = media.Movie(movie_title ="The Matrix",
					 movie_storyline = "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
					 poster_image_url ="https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
					 trailer_youtube_url ="https://www.youtube.com/watch?v=vKQi3bBA1y8")

lord_of_the_rings = media.Movie(movie_title = "Lord of The Rings: The Fellowship of the Ring",
					 movie_storyline = "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
					 poster_image_url = "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",
					 trailer_youtube_url ="https://www.youtube.com/watch?v=V75dMMIW2B4")

edge_of_tomorrow = media.Movie(movie_title = "Edge of Tomorrow",
					 		   movie_storyline = "A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.",
					 		   poster_image_url ="https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
					 		   trailer_youtube_url ="https://www.youtube.com/watch?v=vw61gCe2oqI")

Ex_Machina = media.Movie(movie_title = "Ex Machina",
					 	 movie_storyline = "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.",
					 	 poster_image_url ="https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
					 	 trailer_youtube_url ="https://www.youtube.com/watch?v=EoQuVnKhxaM")

movies = [toy_story, avatar, the_matrix, lord_of_the_rings, edge_of_tomorrow, Ex_Machina,]
fresh_tomatoes.open_movies_page(movies)
#print (media.Movie.VALID_RATINGS)

#print(avatar.storyline)
#the_matrix.show_trailer()
#avatar.show_trailer()