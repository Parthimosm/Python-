import time
import webbrowser
import sys


running = False
runner = input("Do you want this program to start? (y/n):  ")

if runner == "y":
    print("The Program has started")
    running = True
else:
    print("The Program will not start") 



while running == True:
    stop = input("Type stop to stop")
    if stop == "stop":
        running = False
        print("The Program has stopped")
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=FrZRIW87eWI") 
    

