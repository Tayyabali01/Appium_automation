import base64
import os
import time
from multiprocessing.connection import wait
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from time import sleep

#from selenium import TestLogin

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "7.0",
  "appium:deviceName": "Samsung s6edge",
  "appium:app": "C:\\appium\\Duplicate Photo Remover Niam Tech.apk"
}

#
  # """MAKING CONNECTION WITH TESTING DEVICE"""
driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_cap)
driver.start_recording_screen()


"""LOCATING ELEMENTS AND PERFORMING ACTIONS"""
##FLUENT WAIT###
wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[ElementClickInterceptedException])

userconsent_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.Button[2]')))
userconsent_button.click()
StorageperYes_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]')))
StorageperYes_button.click()
getstarted_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')))
getstarted_button.click()

#TestAdclose_button = wait.until(EC.element_to_be_clickable((By.ID,'close-button-container')))
#TestAdclose_button.click()
allphotos_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup[1]')))
allphotos_button.click()
selectphoto1_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.CheckBox')))
selectphoto1_button.click()
delete_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.Button')))
delete_button.click()
confirmationdelete_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.Button[2]')))
confirmationdelete_button.click()

"""Saving screenrecording of action performed"""
video_rawadata = driver.stop_recording_screen()
video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

"""CREATE FILEPATH"""
filePath = os.path.join("C:/appium/Screenrecordings", video_name+".mp4")
# print(filePath)
with open(filePath,"wb") as vd:
  vd.write(base64.b64decode(video_rawadata))




time.sleep(120)