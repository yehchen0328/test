# 載入需要的套件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 



# 設定 Chrome 選項
chrome_options = webdriver.ChromeOptions()

#無頭模式(網頁不會跳出但會在背景執行)
#chrome_options.add_argument('--headless')

# 啟動瀏覽器
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')
# 訪問要去的網址
browser.get('https://bard.google.com/chat?hl=zh-TW')

#抓取search欄位
search = browser.find_element_by_class_name("textarea")
#輸入問題
search.send_keys("Help me with an English reading question of 300 to 400 words, give me answer options, and give me an analysis of the answer in English and Chinese.")
search.send_keys(Keys.RETURN)

#print(browser.title)
time.sleep(3600)