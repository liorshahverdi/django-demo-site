from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000/investigator/') #index view

assert 'Investigator' in browser.title