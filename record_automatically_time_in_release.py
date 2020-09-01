from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def login(driver,id,password):
    """ログイン処理
    MAEYESにログインする

    """

    time.sleep(10)
    # User account入力処理
    userAccountForm = driver.find_element_by_name('userCode')
    userAccountForm.send_keys(id)

    # Password入力処理
    passwordForm = driver.find_element_by_name('password')
    passwordForm.send_keys(password)

    # Loginボタンクリック
    loginButton = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[5]/div/div/div/table/tbody/tr[2]/td[2]/div/div/table/tbody/tr/td/div')
    loginButton.click()


def recordTimeIn(driver):
    """ 出勤打刻
    出勤ボタンをクリックする

    """
    
    time.sleep(10)
    # 出勤ボタンの要素を取得し、クリックする
    buttonOfTimeIn = driver.find_element_by_xpath('//*[@id="x-auto-150"]/div/div/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/table/tbody/tr[2]/td[2]/div/div')
    buttonOfTimeIn.click()
    
 
URL = 'http://mfpserver.cmn.ng.ts-local/maeyes/'
USERID = '4917'
PASSWORD = 'tsid4917'


options = Options()

#options.set_headless(True)

driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()

driver.get(URL)

login(driver,USERID,PASSWORD)

recordTimeIn(driver)


