from adaptor.banner import Banner
from adaptor.print import Print


class PrintBanner(Print):
    def __init__(self, string):
        self.__banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_strong(self):
        self.__banner.show_with_aster()