# Python with Selenium
#
# Count the number of times "pancakes" appears in the search

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.pingodoce.pt/")

# Pop up notification "Agora Não" doesn't work
#notification = browser.find_element_by_xpath('/html/body/div/div[1]/div[4]/div/button[1]')
#notification.click()

#Accept all cookies
cookies = browser.find_element_by_xpath('//*[@id="onetrust-close-btn-container"]/button')
cookies.click()

#Search "Receitas de panquecas" on input search
input_text = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/form/div[1]/input').send_keys("Receitas de panquecas")
browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/form/div[1]/button').click()

page_content = browser.page_source

word = "Panquecas"
word_count = page_content.count(word)
print("==============================\n")
print("The word appears " + str(word_count) + " times.\n")
print("==============================\n")

