from Automator import Automator
import json
from collections import namedtuple
from pprint import pprint

if __name__ == "__main__":

    ##initalized parameters

    firstName = ""
    lastName = ""
    link = ""
    email = ""
    zip = ""
    phone = ""

    chromeCorrd = ['','']
    eightTeenButtonCord = ['','']
    ticketButtonCord = ['','']
    mobileButtonCord = ['','']
    recaptionCord = ['','']
    submitButtonCord = ['','']

    #get my automator object
    myAutomator = Automator()
  
    ##open inputs.json and parse through data
    with open('inputs.json') as f:
        #parce json into dictionary
        inputs = json.load(f)
        #for each set of inputs 
        for entries in inputs:
            #get the current input
            entry = inputs[entries]
            #get parameters and assign to varaiables
            firstName = entry["firstName"]
            lastName = entry["lastName"]
            link = entry["link"]
            email = entry["email"]
            zip = entry["zip"]
            phone = entry["phone"]

            #get corrdinates and assign to variables
            chromeCorrd[0] = int(entry["chromeCorrd"]['x'])
            chromeCorrd[1] = int(entry["chromeCorrd"]['y'])

            eightTeenButtonCord[0] = int(entry["eightTeenButtonCord"]['x'])
            eightTeenButtonCord[1] = int(entry["eightTeenButtonCord"]['y'])

            ticketButtonCord[0] = int(entry["ticketButtonCord"]['x'])
            ticketButtonCord[1] = int(entry["ticketButtonCord"]['y'])

            mobileButtonCord[0] = int(entry["mobileButtonCord"]['x'])
            mobileButtonCord[1] = int(entry["mobileButtonCord"]['y'])

            recaptionCord[0] = int(entry["recaptionCord"]['x'])
            recaptionCord[1] = int(entry["recaptionCord"]['y'])

            submitButtonCord[0] = int(entry["submitButtonCord"]['x'])
            submitButtonCord[1] = int(entry["submitButtonCord"]['y'])

            #pass parameters to object
            myAutomator.setFirstName(firstName) \
                                    .setLastName(lastName) \
                                    .setLink(link) \
                                    .setEmail(email) \
                                    .setZip(zip) \
                                    .setPhone(phone) \
                                    .setChromeCord(chromeCorrd) \
                                    .setEightTeenButtonCord(eightTeenButtonCord) \
                                    .setMobileButtonCord(mobileButtonCord) \
                                    .setRecaptionCord(recaptionCord) \
                                    .setTicketButtonCord(ticketButtonCord) \
                                    .setSubmitButtonCord(submitButtonCord)

            #run automate method      
            myAutomator.automate(submit=False,mobile=True)
