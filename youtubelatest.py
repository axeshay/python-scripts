from selenium import webdriver
import sys
browser = webdriver.Firefox()
if(len(sys.argv)>1):
    user_input = " ".join(sys.argv[1:])

browser.get("http://www.youtube.com/results?search_query=" + user_input)
element = browser.find_element_by_class_name("style-scope ytd-vertical-list-renderer")
another_element = element.find_element_by_id("dismissable")
another_element.click()
