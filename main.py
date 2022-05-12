from selenium import webdriver




def open_webdriver():
  # open Chrome and navigate to url 
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/")
  return driver

def get_new_Arrival(driver):
  section_title = driver.find_element(by="xpath",value="/html/body/main/article/div[2]/section/div/h2")
  print(section_title.text)
  new_arrivals = driver.find_element(by="xpath", value="/html/body/main/article/div[2]/section/div/div")
  return new_arrivals.text
  

def write_file(products):
  file = open("ecommercefile.txt","w")
  file.write(products)
  file.close()


def main():
  driver = open_webdriver()
  page_title = driver.title
  print(page_title)
  products = get_new_Arrival(driver)
  write_file(products)
  print(products)


main()