import webbrowser

#Create a standard movie class

class Movie():

# double underscores mean init is a reserved keyword
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# Opens a browser and shows the movie's trailer on YouTube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)