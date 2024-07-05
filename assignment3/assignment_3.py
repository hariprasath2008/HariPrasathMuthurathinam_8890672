from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigating to the YouTube homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element(By.NAME, "search_query")
search_bar.send_keys("Paara Song")
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Clicking on the first video in the search results
first_video_link = driver.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
first_video_link.click()
time.sleep(10)

# Clicking on the first suggested video (recommended on the sidebar)
try:
    first_suggested_video = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//ytd-compact-video-renderer//a[@id='thumbnail'])[1]"))
    )
    first_suggested_video.click()
except Exception as e:
    print("Error clicking the first suggested video:", e)
time.sleep(10)

# Subscribing to the channel
try:
    subscribe_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ytd-subscribe-button-renderer//button"))
    )
    subscribe_button.click()
except Exception as e:
    print("Error clicking subscribe button:", e)

# Navigating to the YouTube Trending page
driver.get("https://www.youtube.com/feed/trending")
time.sleep(5)

# Clicking on the first video in the trending list
first_trending_video_link = driver.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
first_trending_video_link.click()
time.sleep(5)

# Waiting for the sign-in page to load
time.sleep(5)

# Closing the webdriver
driver.close()
