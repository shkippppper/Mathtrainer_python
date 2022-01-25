from cgitb import text
from re import A
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

option1 = Options()
option1.add_argument("--disable-notifications")
browser =webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option1)
browser.maximize_window()
browser.get('https://www.mathtrainer.org/')
time.sleep(0.5)
startButton = browser.find_element_by_class_name("start.is-armed")
startButton.click()
for i in range(3):

    for x in range(4):
        time.sleep(1)
        firstNumberText = browser.find_element_by_class_name("a").text
        secondNumberText = browser.find_element_by_class_name("b").text
        operator = browser.find_element_by_class_name("operator").text

        firstNumber = int(firstNumberText)
        secondNumber = int(secondNumberText)


        print(firstNumber)
        print(operator)
        print(secondNumber)

        if(operator == "+"):
            answer = firstNumber + secondNumber
        elif(operator == "-"):
            answer = firstNumber - secondNumber
        elif(operator == "/"):
            answer = firstNumber / secondNumber
        elif(operator == "*"):
            answer = firstNumber * secondNumber

        print (answer)
        textAnswer = str(answer)

        keyboard.type(textAnswer)
    time.sleep(3)
    continueButton = browser.find_element_by_class_name("start.is-armed")
    continueButton.click()

