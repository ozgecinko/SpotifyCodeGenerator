# import cv2 library
import cv2
import random


class SpotifyCode:
    # read the images
    zero = cv2.imread('images/0.png')
    one = cv2.imread('images/1.png')
    two = cv2.imread('images/2.png')
    three = cv2.imread('images/3.png')
    four = cv2.imread('images/4.png')
    five = cv2.imread('images/5.png')
    six = cv2.imread('images/6.png')
    seven = cv2.imread('images/7.png')
    logo = cv2.imread('images/logo.png')

    img_list = [logo]
    random_lst = list()

    def __init__(self, song_name):
        self.song_name = song_name

    def visualize_list(self, code_list):
        for item in code_list:
            num = int(item)
            if num == 0:
                self.img_list.append(self.zero)
            elif num == 1:
                self.img_list.append(self.one)
            elif num == 2:
                self.img_list.append(self.two)
            elif num == 3:
                self.img_list.append(self.three)
            elif num == 4:
                self.img_list.append(self.four)
            elif num == 5:
                self.img_list.append(self.five)
            elif num == 6:
                self.img_list.append(self.six)
            elif num == 7:
                self.img_list.append(self.seven)
        # show the output image
        code = cv2.hconcat(self.img_list)
        cv2.imshow('SpotifyCode.jpg', code)
        cv2.waitKey(0)

    def create_random_code(self):
        # create random 20 numbers
        self.random_lst = [random.randint(0, 7) for x in range(20)]
        # begins and finishes with 0
        self.random_lst.insert(0, 0)
        self.random_lst.append(0)
        # 11th index is 7
        self.random_lst.insert(11, 7)
        return self.random_lst


song = SpotifyCode("Call Out My Name")
song.visualize_list([0, 4, 2, 5, 2, 5, 7, 3, 1, 3, 6, 7, 0, 4, 2, 2, 2, 3, 1, 3, 2, 4, 0])


"""
# This needs URI and media reference connection. Couldn't figure it out yet.
song = SpotifyCode("Random Spotify Song")
random_code = song.create_random_code()
song.visualize_list(random_code)
"""