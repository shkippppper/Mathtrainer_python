from cgitb import text
from re import A
from tkinter.ttk import Progressbar
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
from pynput.keyboard import Key, Controller

keyboard = Controller()

option1 = Options()
option1.add_argument("--disable-notifications")
browser =webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option1)
browser.maximize_window()
browser.get('https://www.mathtrainer.org/')
time.sleep(1.5)
startButton = browser.find_element_by_class_name("start.is-armed")
startButton.click()



#---------first round-------------
for i in range(4):
    time.sleep(1.5)
    firstNumberText = browser.find_element_by_class_name("a").text
    secondNumberText = browser.find_element_by_class_name("b").text
    operator = browser.find_element_by_class_name("operator").text

    progress = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div').get_attribute("style")
    progressFiltered = str(progress)
    progressFiltered = re.sub('width', '',progressFiltered)
    progressFiltered = re.sub('%;', '',progressFiltered)
    progressFiltered = re.sub(':', '',progressFiltered)
    progressFiltered = re.sub(' ', '',progressFiltered)
    firstNumber = int(firstNumberText)
    secondNumber = int(secondNumberText)       
    progressForWhile = int(progressFiltered)
    if(operator == "+"):
        answer = firstNumber + secondNumber
    elif(operator == "-"):
        answer = firstNumber - secondNumber
    elif(operator == "/"):
        answer = firstNumber / secondNumber
    elif(operator == "*"):
        answer = firstNumber * secondNumber
    textAnswer = str(answer)
    print(firstNumber,operator,secondNumber,'=',answer,' | ',progressFiltered, "%")
    keyboard.type(textAnswer)

#---------end of first round-------------

progressForWhile = 0
time.sleep(3)
continueButton = browser.find_element_by_class_name("start.is-armed")
continueButton.click()

#---------rest of the rounds-----------

for i in range(6):

    #while progressForWhile <85:
    for z in range(8):
        time.sleep(2)
        firstNumberText = browser.find_element_by_class_name("a").text
        secondNumberText = browser.find_element_by_class_name("b").text
        operator = browser.find_element_by_class_name("operator").text
        
        progress = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div').get_attribute("style")

        progressFiltered = str(progress)
        progressFiltered = re.sub('width', '',progressFiltered)
        progressFiltered = re.sub('%;', '',progressFiltered)
        progressFiltered = re.sub(':', '',progressFiltered)
        progressFiltered = re.sub(' ', '',progressFiltered)


        firstNumber = int(firstNumberText)
        secondNumber = int(secondNumberText)       
        progressForWhile = int(progressFiltered)

        if(operator == "+"):
            answer = firstNumber + secondNumber
        elif(operator == "-"):
            answer = firstNumber - secondNumber
        elif(operator == "/"):
            answer = firstNumber / secondNumber
        elif(operator == "*"):
            answer = firstNumber * secondNumber

        textAnswer = str(answer)
        print(firstNumber,operator,secondNumber,'=',answer,' | ',progressFiltered, "%")

        keyboard.type(textAnswer)
    time.sleep(5)
    continueButton = browser.find_element_by_class_name("start.is-armed")
    continueButton.click()
    progressForWhile = 0

#---------rest of the rounds-----------
