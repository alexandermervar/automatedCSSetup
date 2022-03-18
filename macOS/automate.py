from selenium import webdriver
import os
import time

parentDirectory = os.getcwd()
timeForUser = 20

driver = webdriver.Firefox(executable_path= parentDirectory + '/geckodriver')

# Create an array of urls to visit
urls = ['https://tcciub.pie.iu.edu/ShiftsReport', 'https://tcciub.pie.iu.edu/DailyRecords?page=0&pageLimit=101', 'https://tcciub.pie.iu.edu/Tickets', 'https://iu.service-now.com/']

# Opens the first url in the array
driver.get(urls[0])

# Sign in with IU Login button xpath
# /html/body/div/div[2]/div/div[2]/div/div/p/button[1]
driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/p/button[1]').click()

# Sleep to allow user to sign in
time.sleep(timeForUser)

# Open remainder of the urls in the array
i = 1
for url in urls[1:]:
    #open tab
    driver.execute_script("window.open('');")
    #switch to new tab
    driver.switch_to.window(driver.window_handles[i])
    # open new url
    driver.get(url)
    i += 1