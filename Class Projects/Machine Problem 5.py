#
# Machine Problem 5
# CS 1300
# Bruce Miller
#
# Description: This script will use the cs1graphics module to create a graphics
# scene and then animate the scene. The initial scene has a sun, a
# cloud, a tree, and a bull. The sun is a Circle, the cloud is a
# Polygon, the tree and bull use the Layer class to combine
# multiple objects. When the animation starts, a second bull
# enters the scene and butts the first bull into the air and off
# the screen. Meanwhile, the sun and cloud are moving across the
# sky, and the tree leaves are growing.

#

from cs1graphics import *
from time import sleep

def makeGrass():
    #
    # Creates a green Rectangle on the lower portion of the scene which will
    # be the grassy area of the scene.
    #
    # There are no parameters.
    #
    # Returns the grass object.
    #
    
    grass = Rectangle(1600, 450, Point(800,675))
    grass.setFillColor('darkGreen')
    grass.setBorderColor('darkGreen')
    return grass


### Setup Canvas
sky = Canvas(1600, 900, 'skyBlue', 'My World')
#grass = 
sky.add(makeGrass())


### Animate
leafSize = 50
timeDelay = 0.1
loopFrames = True
while loopFrames:
    break
    tree = makeTree(leafSize)
    sleep(timeDelay)
