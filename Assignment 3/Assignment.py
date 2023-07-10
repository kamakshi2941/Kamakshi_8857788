# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.youtube.com/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("friends")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(3)

# Verifying that the search results page has loaded
assert "friends" in driver.title
time.sleep(3)

# Selecting a video from the search results
video_link = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
time.sleep(3)
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
video_link.click()


time.sleep(3)


channel= driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/a/yt-img-shadow/img")
time.sleep(3)
channel.click()
time.sleep(3)

no_thanks_button= driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-mealbar-promo-renderer/div/div[2]/yt-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
no_thanks_button.click()
time.sleep(2)

feed= driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/tp-yt-app-toolbar/div/div/tp-yt-paper-tabs/div/div/tp-yt-paper-tab[2]/div/div[1]")
time.sleep(3)
feed.click()
time.sleep(3)
# Clicking on no thanks button
# no_thanks_button= driver.find_element("xpath","/html/body/div[5]/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div[3]/div/span[2]/span/input")
# no_thanks_button.click()
# time.sleep(2)


# Closing the webdriver
driver.close()
