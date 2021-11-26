import time


class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        current = time.time()
        calc_ticks = int(current - self.__age)
        if 0 <= calc_ticks < 60:
            return str(calc_ticks) + "s"
        elif 60 <= calc_ticks < 3600:
            calc_ticks = int(calc_ticks / 60)
            return str(calc_ticks) + "m"
        elif 3600 <= calc_ticks < 86400:
            calc_ticks = int(calc_ticks / 3600)
            return str(calc_ticks) + "h"
