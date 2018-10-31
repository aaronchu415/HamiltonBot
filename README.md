HamiltonBot
=========

This is a Python Bot that uses pyautogui to automatically enter user defined data into the Hamilton Website.

###### Setup:

install pyautogui and dependencies:

  1. ```sudo pip3 install pyobjc-framework-Quartz```
  2. ```sudo pip3 install pyobjc-core```
  3. ```sudo pip3 install pyobjc```
  4. ```sudo pip3 install pyautogui```
  
Configre input.json:

  Enter your own data (sample has been provided as input1 and input2, copy and paste to add more inputs. 
  Each input will generate a new window and submission)
  
  Configure the X,Y Cordinates. To get corrdinates you can run in terminal:
  
    > python3 
    > import pyautogui
    > pyautogui.position()
  
  
###### Design:
  The files contains the follow design:
	
    Automator.py (Class)
    Input.json (Config file for script)
    Main.py (Entry Point):

###### Run:

  Open Terminal:

    > cd HamiltonBot
    > python3 main.py
