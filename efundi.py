import os
from selenium import webdriver
import time

my_user = os.environ['username']
my_pass = os.environ['password']

def efundi():
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome('/home/runner/efundi-covid/chromedriver',options=chrome_options)
  driver.get('http://diyservices.nwu.ac.za/')

  usernamebox = driver.find_element_by_xpath('//*[@id="username"]')
  passwordbox = driver.find_element_by_xpath('//*[@id="password"]')
  submitbtn = driver.find_element_by_xpath('//*[@id="fm1"]/section[4]/input[4]')
  usernamebox.send_keys(str(my_user))
  passwordbox.send_keys(str(my_pass))
  submitbtn.click()
  time.sleep(5)

  driver.get('https://diyservices.nwu.ac.za/covid-19-pre-screening')
  #driver.maximize_window()
  time.sleep(5)

  driver.switch_to.frame(frame_reference=driver.find_element_by_xpath('//*[@id="myFrame"]'))
  checkbox = driver.find_element_by_id("gwt-uid-2")
  #checkbox = driver.find_element_by_xpath('')
  driver.execute_script("arguments[0].click();", checkbox)
  time.sleep(5)

  # if vaccinated uncomment line below
  vac = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[1]/div/div/div/div[2]/span[1]/label')

  # if not vaccinated uncomment next line and comment out the line above
  #vac = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[1]/div/div/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", vac)

  fever = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[1]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", fever)

  cough = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[3]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", cough)

  sore = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[5]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", sore)

  short = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[7]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", short)

  taste = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[9]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", taste)

  smell = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[11]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", smell)

  head = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[13]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", head)

  fatigue = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[5]/div/div[15]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", fatigue)

  close = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[9]/div/div[1]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", close)

  travel = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[9]/div/div[3]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", travel)

  test = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[5]/div/div[9]/div/div[5]/div/div[2]/span[2]/label')
  driver.execute_script("arguments[0].click();", test)

  submitbtn2 = driver.find_element_by_id('submit')
  driver.execute_script("arguments[0].click();", submitbtn2)
  time.sleep(5)
  driver.quit()