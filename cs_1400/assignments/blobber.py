class Blobber:
    def __init__(self, __name, __color, __radius, __height):
        self.__name = __name
        self.__color = __color
        self.__radius = __radius
        self.__height = __height
    


    def vitalsOk(self, volume, vitals):

        if volume >= vitals >= (volume * .9):
            blobberOk = True
        else:
            blobberOk = False   

        