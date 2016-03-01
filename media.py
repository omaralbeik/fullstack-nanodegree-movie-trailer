import webbrowser


class Media():
    """Media is the parent class for Movie and TVShow classes,
    it contains all generic information for both"""

    def __init__(self, title, story_line, poster_image_url,
                 trailer_youtube_url, year):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.year = year


class Movie(Media):
    """Movie class is a child class of Media,
    specifically for holding movies information"""

    def __init__(self, title, story_line, poster_image_url,
                 trailer_youtube_url, year, duration):
        Media.__init__(self, title, story_line,
                       poster_image_url, trailer_youtube_url, year)
        self.duration = duration


class TVShow(Media):
    """TVShow class is a child class of Media,
    specifically for holding tv shows information"""

    def __init__(self, title, story_line, poster_image_url,
                 trailer_youtube_url, year, seasons_count):
        Media.__init__(self, title, story_line,
                       poster_image_url, trailer_youtube_url, year)
        self.seasons_count = seasons_count
