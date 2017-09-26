import webbrowser


class Movie():
    """ This class stores movie information"""

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """ These methods allow for each movie to display its unique info"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
       
    def show_trailer(self):
        """ This function plays the movie's trailer once clicked"""
        webbrowser.open(self.trailer_youtube_url)
