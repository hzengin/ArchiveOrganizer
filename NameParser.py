__author__ = 'hzengin'

from Movie import *

class NameParser:
    def __init__(self):
        print("")

    def parse(self,pattern,movie):
        pattern = pattern.replace("[TITLE]",movie.title)
        pattern = pattern.replace("[YEAR]",movie.year)
        pattern = pattern.replace("[RATING]",movie.rating)
        return pattern