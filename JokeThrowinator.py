from joke.jokes import * #Importing the modules
import time
import random
import tkinter
from tkinter import messagebox as mb

window = tkinter.Tk() #Making a window
window.withdraw() #Remove from screen

RanTimes = [500, 600, 700, 100, 1500, 3000, 5000, 7000, 10000] #Array for random times

def RanJoke(): #Making the function to call and show the joke
	Joke = icanhazdad() #Storing joke
	TimeChoice = random.choice(RanTimes) #Selecting random time
	time.sleep(TimeChoice) #Delaying for that amount of time.
	mb.showwarning('Joke Time', Joke) #Shows joke

while True: #Creating an endless loop for jokes
	RanJoke() #Calling the function for the joke