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
#browser.maximize_window()
browser.get('https://www.mathtrainer.org/')
time.sleep(1)
startButton = browser.find_element_by_class_name("start.is-armed")
startButton.click()

x=0


#---------first round-------------
while x<10:
    
    time.sleep(2)
    firstNumberText = browser.find_element_by_xpath('//*[@id="app"]/div/section/section/div/div/span/span/span/span[2]/span[1]/span[2]').text
    secondNumberText = browser.find_element_by_xpath('//*[@id="app"]/div/section/section/div/div/span/span/span/span[2]/span[2]/span[2]').text
    operator = browser.find_element_by_class_name('mbin').text
    progressFiltered = 0

    firstNumber = int(firstNumberText)
    secondNumber = int(secondNumberText)
    if(operator == "+"):
        answer = firstNumber + secondNumber
    elif(operator == "−"):
        answer = firstNumber - secondNumber
    elif(operator == "÷"):
        answer = firstNumber / secondNumber
    elif(operator == "×"):
        answer = firstNumber * secondNumber
    textAnswer = str(answer)
    print(firstNumber,operator,secondNumber,'=',answer,' | ',progressFiltered, "%")
    keyboard.type(textAnswer)

    progress = browser.find_element_by_class_name('progress').get_attribute("style")
    progressFiltered = str(progress)
    progressFiltered = re.sub('width: ', '',progressFiltered)
    progressFiltered = re.sub('%;', '',progressFiltered)
    progressFiltered = int(progressFiltered)

    numberOfTimes = round(100 / progressFiltered) - 1
    progressFilteredDisplay = progressFiltered
    for i in range(numberOfTimes):
        time.sleep(2)
        firstNumberText = browser.find_element_by_xpath('//*[@id="app"]/div/section/section/div/div/span/span/span/span[2]/span[1]/span[2]').text
        secondNumberText = browser.find_element_by_xpath('//*[@id="app"]/div/section/section/div/div/span/span/span/span[2]/span[2]/span[2]').text
        operator = browser.find_element_by_class_name('mbin').text
        
        firstNumber = int(firstNumberText)
        secondNumber = int(secondNumberText)
        print(firstNumber,operator,secondNumber)

        if(operator == "+"):
            answer = firstNumber + secondNumber
        if(operator == "−"):
            answer = firstNumber - secondNumber
        if(operator == "÷"):
            answer = firstNumber / secondNumber
        if(operator == "×"):
            answer = firstNumber * secondNumber
        textAnswer = str(answer)
        print(firstNumber,operator,secondNumber,'=',answer,' | ',progressFilteredDisplay, "%")
        keyboard.type(textAnswer)
        progressFilteredDisplay += progressFiltered

    time.sleep(3)
    continueButton = browser.find_element_by_class_name("start.is-armed")
    continueButton.click()
    x-=1

