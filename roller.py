#!/usr/bin/env python
# coding: utf-8

# In[1]:


# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView.
# Resource for graphics https://mcsp.wartburg.edu//zelle/python/graphics/graphics.pdf

from random import randrange
from graphics import GraphWin, Point

# Custom widgets button and DieView
# They are their own classes in a different jupyter notebook. This is how they link to this notebook

from button import Button
from dieview import DieView

def main():
    # create the application window
    win = GraphWin("Dice Roller") # Constructs a new graphics window for drawing on the screen. (title, width, height)
    
    win.setCoords(0, 0, 10, 10) # Sets the coordinate system of the window in the format (xll, yll, xur, yur)
                                # The lower-left corner is (xll, yll) and the upper-right corner is (xur, yur)
        
    win.setBackground("red2") # Sets the window background to the given color

    # draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse() # Pauses for the user to click a mouse in the window and returns where the mouse was 
                        # clicked as a Point object.
        
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse() 

    # close
    win.close() # Closes the on-screen window

main()


# In[ ]:




