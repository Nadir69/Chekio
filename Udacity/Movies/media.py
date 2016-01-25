import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    """A program with my favourite movies"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, title, storyline, poster_image, trailer, duration):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, title, season, episode, tv_station, duration):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station