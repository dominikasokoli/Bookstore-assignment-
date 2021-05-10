import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

w=webdriver.Firefox()
w.get("http://www.empik.com")
#searchbutton_empik = WebDriverWait(w, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "input[name=’q-i’]"))
#searchbutton_empik.clear()

search_input = w.find_element_by_xpath('//*[@id="bq"]')
search_input.send_keys('Harry Potter')
search_btn = w.find_element_by_xpath('//*[@id="searchSet"]/button')
search_btn.click()
