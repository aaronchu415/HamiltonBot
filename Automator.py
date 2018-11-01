
import pyautogui
import time
from random import randint

class Automator:

    def __init__(self):

        #Default preamaters
        self.link = "https://www.luckyseat.com/hamilton-ny/"
        self.firstName = "default"
        self.lastName = "default"
        self.email = "default@gmail.com"
        self.zip = "94111"
        self.phone = "4155555555"

        self.chromeCorrd = {
            "x": 1424,
            "y": 302
        }

        self.eightTeenButtonCord = {
            "x": 224,
            "y": 327
        }

        self.ticketButtonCord = {
            "x": 959,
            "y": 657
        }

        self.mobileButtonCord = {
            "x": 212,
            "y": 555
        }

        self.recaptionCord = {
            "x": 227,
            "y": 764
        }

        self.submitButtonCord = {
            "x": 376,
            "y": 855
        }

        self.firstRun = True

    def setLink(self, link):
        self.link = link
        return self

    def setFirstName(self, firstName):
        self.firstName = firstName
        return self

    def setLastName(self, lastName):
        self.lastName = lastName
        return self

    def setEmail(self, email):
        self.email = email
        return self

    def setZip(self, zip):
        self.zip = zip
        return self

    def setPhone(self, phone):
        self.phone = phone
        return self

    def setChromeCord(self, tupleXY):
        self.chromeCorrd["x"] = tupleXY[0]
        self.chromeCorrd["y"] = tupleXY[1]
        return self

    def setEightTeenButtonCord(self, tupleXY):
        self.eightTeenButtonCord["x"] = tupleXY[0]
        self.eightTeenButtonCord["y"] = tupleXY[1]
        return self

    def setTicketButtonCord(self, tupleXY):
        self.ticketButtonCord["x"] = tupleXY[0]
        self.ticketButtonCord["y"] = tupleXY[1]
        return self

    def setMobileButtonCord(self, tupleXY):
        self.mobileButtonCord["x"] = tupleXY[0]
        self.mobileButtonCord["y"] = tupleXY[1]
        return self

    def setRecaptionCord(self, tupleXY):
        self.recaptionCord["x"] = tupleXY[0]
        self.recaptionCord["y"] = tupleXY[1]
        return self

    def setSubmitButtonCord(self, tupleXY):
        self.submitButtonCord["x"] = tupleXY[0]
        self.submitButtonCord["y"] = tupleXY[1]
        return self

    #move mouse from xy to another xy cord. 
    def mouseMove(self, x1,y1,x2,y2):

        #move in a random time
        time = randint(1, 2) * .1
        #starting point
        pyautogui.moveTo(x1, y1, duration=time)

        #move to 3 random locations
        for i in range(3):
            time = randint(1, 2) * .1
            randomX = x1 + randint(50, 500)
            randomY = y1 + randint(50, 500)
            pyautogui.moveTo(randomX, randomY, duration=time)

        #move to destination
        pyautogui.moveTo(x2, y2, duration=time)    

    def automate(self, mobile=True, submit=False):
        # double click the chrome icon if first time running, else skip step as we have already selected chrome
        if (self.firstRun):
            pyautogui.click(self.chromeCorrd["x"],
                            self.chromeCorrd["y"], button='left')
        # press command N to open a new window
        pyautogui.keyDown('command')
        pyautogui.keyDown('shiftleft')
        pyautogui.press('n')
        pyautogui.keyUp('command')
        pyautogui.keyUp('shiftleft')
        # type in the link and press enter
        pyautogui.typewrite(self.link)
        pyautogui.press('enter')

        # wait for page to load
        # press tab 4 times to get to the firstname field

        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')

        # fill in form. press tab after each input
        pyautogui.typewrite(self.firstName)
        pyautogui.press('tab')
        pyautogui.typewrite(self.lastName)
        pyautogui.press('tab')
        pyautogui.typewrite(self.email)
        pyautogui.press('tab')
        pyautogui.typewrite(self.zip)
        pyautogui.press('tab')
        pyautogui.press('tab')

        if (mobile):
            pyautogui.typewrite(self.phone)
            pyautogui.press('tab')

        # press down to get to the bottom of the form
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')

        #click the button
        pyautogui.click(self.eightTeenButtonCord["x"],
                        self.eightTeenButtonCord["y"], button='left')
        time.sleep(1)

        #if user wants to enter mobile then enter, else skip
        if (mobile):
            ##move mouse from previous button to next button
            self.mouseMove(self.eightTeenButtonCord["x"], self.eightTeenButtonCord["y"], self.mobileButtonCord["x"], self.mobileButtonCord["y"])

            pyautogui.click(self.mobileButtonCord["x"],
                            self.mobileButtonCord["y"], button='left')
            time.sleep(1)
            
            self.mouseMove(self.mobileButtonCord["x"], self.mobileButtonCord["y"], self.ticketButtonCord["x"], self.ticketButtonCord["y"])

        else:
            ##move mouse from previous button to next button
            self.mouseMove(self.eightTeenButtonCord["x"], self.eightTeenButtonCord["y"], self.ticketButtonCord["x"], self.ticketButtonCord["y"])

        #click the button
        pyautogui.click(self.ticketButtonCord["x"],
                        self.ticketButtonCord["y"], button='left')
        time.sleep(1)

        ##move mouse from previous button to next button
        self.mouseMove(self.ticketButtonCord["x"], self.ticketButtonCord["y"],self.recaptionCord["x"], self.recaptionCord["y"])

        #click the button
        pyautogui.click(self.recaptionCord["x"],
                        self.recaptionCord["y"], button='left')
        time.sleep(3)


        #if user wants to submit then press submit, else nothing
        if (submit):
            ##move mouse from previous button to next button
            self.mouseMove(self.recaptionCord["x"], self.recaptionCord["y"],self.submitButtonCord["x"], self.submitButtonCord["y"])

            pyautogui.click(self.submitButtonCord["x"],
                            self.submitButtonCord["y"], button='left')
            time.sleep(1)

        # press command N to open a new window
        pyautogui.keyDown('command')
        pyautogui.press('m')
        pyautogui.keyUp('command')
        self.firstRun = False
        time.sleep(4)
