import webbrowser

class Movie():
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]  
        """class Movie() with PEP 484 type annotations.tuserlevel() with PEP 484 type annotations.

      Input:
          self, movie_title etc: The  inputs are instance variables. In this case, they are variables specifically unique
          to each instance of class Movie(). Those instances being each Movie(i.e The_Matrix, Lord_of_The_Rings etc).
          Self, is the object or instance being created of class Movie().
          self.title, self.storyline etc: Instance Variables unique to each Movie.

        Behavior:
            Function init is called, it initializes or creates space in memory to
            remember details like title, storyline, poster_image, and trailer_youtube that 
            we want to remember inside our class Movie().
            Function then initializes variables with info init is going to receive (movie_title etc).
            So when init function gets called, self becomes instance being created like self = The_Matrix etc.
                  
        Return:
            Returns each instance variable or piece of information about movie including
            movie_title, movie_storyline, poster_image, and trailer_youtube.orresponding quiz to user and answers to be compared for that quiz, invalid input if user answer is wrong.

        """
    

        def __init__(self, movie_title, movie_storyline, poster_image,
         trailer_youtube):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube 

        def show_trailer(self):
            """def show_trailer() with PEP 484 type annotations.un_quiz  with PEP 484 type annotations:  

        Input:
            self. Also, def show_trailer(self) is an instance method like def __init__ because it is a function
            that is defined inside a class and is associated with an instance. 
        Behavior:
            Function opens web browser with correct URL. The link or correct URL is stored in
            instance variable trailer_youtube_url.         
        Return:
            Returns correct movie trailer youtube URL link.

            """
            webbrowser.open(self.trailer_youtube_url)
