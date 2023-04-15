# this script will open Chrome browser, extract data and save values in excel.

from selenium import webdriver as seleniumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import pyautogui as timeResponse
import pandas as pd
import os

# get browser that will use.
browser = seleniumOptions.Chrome()

# open url to get the data.
browser.get('https://rpachallengeocr.azurewebsites.net/')

i = 1
row = 1
dataFrameList = []

while i < 4:
    # find xpath according table element
    tableElement = browser.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    # extract rows and columns finding the tag.
    rows = browser.find_elements(By.TAG_NAME, 'tr')
    columns = browser.find_elements(By.TAG_NAME, 'td')

    # for using to cycle through the data within the table.
    for currentLine in rows:
        print(currentLine.text)
        dataFrameList.append(currentLine.text)
        row += 1

    i += 1

    # wait computer response.
    timeResponse.sleep(2)

    # find xpath according Next button element.
    browser.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # wait computer response.
    timeResponse.sleep(2)

# create excel file extractdatachrome.xlsx and save workbook.
excelFile = pd.ExcelWriter('OutputExtractDataTable.xlsx', engine='xlsxwriter')
excelFile._save()

# add column dados and values from dataFrameList.
dataFrame = pd.DataFrame(dataFrameList, columns=['Output'])
excelFile = pd.ExcelWriter('OutputExtractDataTable.xlsx', engine='xlsxwriter')

# convert the workboot to excel, add sheet and save.
dataFrame.to_excel(excelFile, sheet_name='Sheet1', index=False)
excelFile._save()