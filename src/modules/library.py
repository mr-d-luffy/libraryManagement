# inbuilt modules of python
from random import sample


# this class is the module of main file
class library():
    # this function create 8 digit id for searsh in database
    @staticmethod
    def createID():
        number = "1234567890"
        alpha = "abcdefghijklmnoqrstuvwxyz"
        alpha = alpha.upper()
        all = number+alpha
        ID = ''.join(sample(all, 8))
        return ID

# testing of functions
if __name__ == "__main__":
    l = library()
    print(l.createID())