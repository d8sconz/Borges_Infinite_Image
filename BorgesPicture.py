import sys, pygame, PIL, urllib2
from pygame.locals import *
from PIL import Image, ImageFilter
import random
import numpy
import pygame.surfarray as surfarray

pygame.init()
sWidth, sHeight = 329, 240 #Screen dimensions
screenSize=(sWidth, sHeight)
surface = pygame.display.set_mode(screenSize,0,32)
pygame.display.set_caption("Borges Infinite Image")

global count
count = 0
cnt = 0

def show (image):
    surface.blit (image, (0,0))
    #pygame.draw.circle(surface, (255,0,0), (x,y), 5, 1)    #for testing
    pygame.display.update()
    #raw_input("Press Enter to continue...")                #for testing


def progress (strt, stp):
    pass

def filterContour():
    global cnt
    im = Image.open("contour.jpg")
    im1 = im.filter(ImageFilter.DETAIL)
    im1.save("contour.jpg")
    #im = Image.open("contour.jpg")
    #im1 = im.filter(ImageFilter.EDGE_ENHANCE)
    #im.save("contour.jpg")
    im = pygame.image.load("contour.jpg")
    show(im)

    print "loaded Contour.jpg " + str(cnt)
    cnt += 1
    #im1.show ()
    #raw_input("Press Enter to continue...")

def openImage():
    try:
        im = pygame.image.load("my_image.jpg")
        pygame.image.save(im, "contour.jpg")
        surface.blit (im, (0,0))
        pygame.display.update()
    except:
        surface.fill ((255, 255, 255))

openImage()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loopExit=False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loopExit = False # Be IDLE friendly!
                pygame.quit()
                sys.exit()

    ###Open the image with PIL
    img = Image.open("contour.jpg")
    ###build a list of each pixel in the image.
    pixels = img.load()
    ###set up pygame array
    ar = pygame.PixelArray (surface)

    x = random.randrange(sWidth-1)
    y = random.randrange(sHeight-1)

    data = []
    r = 0
    g = 0
    b = 0
    #print "current location: ",x,y         #for testing
    avgCount = 0
    for xadj in range(0,3):
        for yadj in range(0,3):
            if x +(xadj-1) > sWidth or y + (yadj-1) > sHeight or x + (xadj-1) < 0 or y + (yadj-1) < 0:
                continue
            if xadj-1 == 0 and yadj-1 == 0:
                continue
            cpixel = pixels[(x +(xadj-1)),(y + (yadj-1))]
            #print 'At position ', '(', x + xadj-1, y + yadj-1, ')', 'color data equals ',pixels[(x +(xadj-1)),(y + (yadj-1))] #for testing
            data.append(cpixel)

    for num in range(len(data)):
        r+=data[num][0]
        #g+=data[num][1]
        #b+=data[num][2]

        avgCount+=1
        #print 'total of color channels at iteration ',avgCount, r, g, b         #for testing

    ###Get the averages, and return!
    if r == 0:
        continue
    rAvg = r/avgCount
    #gAvg = g/avgCount
    #bAvg = b/avgCount
    #print 'average color at location (',x,y,')','(',rAvg,rAvg,rAvg,')'    #for testing
    ar[x][y] =(rAvg,rAvg,rAvg)
    sf = ar.make_surface()
    del ar
    show (sf)
    count += 1
    if count == 3000:
        pygame.image.save(sf, 'contour.jpg')
        #filterContour()
        count = 0


#Graveyard of code bits

#1 For getting known images from known sites on the web

"""
import urllib2
import webbrowser
import os
# find yourself a picture on a web page you like
# (right click on the picture, look under properties and copy the address)
picture_page = "http://lifesimages.files.wordpress.com/2008/06/black-and-white-magnolia.jpg"
#webbrowser.open(picture_page) # test
# open the web page picture and read it into a variable
opener1 = urllib2.build_opener()
page1 = opener1.open(picture_page)
my_picture = page1.read()
# open file for binary write and save picture
# picture_page[-4:] extracts extension eg. .gif
# (most image file extensions have three letters, otherwise modify)
filename = "my_image" + picture_page[-4:]
print filename # test
fout = open(filename, "wb")
fout.write(my_picture)
fout.close()
im = pygame.image.load(filename)
im = pygame.transform.scale(im, (sWidth, sHeight))
pygame.image.save(im, filename)
# was it saved correctly?
# test it out ...
webbrowser.open(filename)
# or ...
# on Windows this will display the image in the default viewer
#os.startfile(filename)

"""


#2 for generating shades of gray
"""i=1
j=1
cols = [(230,230,230),(210,210,210),(190,190,190),(158,158,158),(255,255,255),(96,96,96),(64,64,64),(32,32,32),(16,16,16)]
col = random.randrange(9)
color = cols[col]"""
