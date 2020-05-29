from selenium import webdriver

geckodriver_path = r'C:\Users\Romas\geckodriver\geckodriver.exe'

browser = webdriver.Firefox(executable_path=geckodriver_path)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
