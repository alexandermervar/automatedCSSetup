from multiprocessing import parent_process
from selenium import webdriver
import os

parentDirectory = os.getcwd()

driver = webdriver.Firefox(executable_path= parentDirectory + '/geckodriver')