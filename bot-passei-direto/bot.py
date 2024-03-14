from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

class PasseiDiretoBot:
    def __init__(self):
      options = webdriver.ChromeOptions()
      options.add_argument('lang=pt-br')
      options.add_experimental_option("detach", True)
      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    def getLink(self):
      path = os.getcwd() + "//" + "./index.html"
      print(path)
      self.driver.get("file://" + path)

      self.link = input("Digite o Link: ")

    def abirSite(self):
      self.driver.get(self.link)
      time.sleep(3)

    def deletePaywallAlert(self):
      try:
        paywallAlert = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[3]')
        paywallAlertClass = paywallAlert.get_attribute('class')
        self.driver.execute_script(f'''
          var l = document.getElementsByClassName("{paywallAlertClass}")[0];
          l.parentNode.removeChild(l);
        ''')
        time.sleep(1)
      except:
        print("Erro ao remover paywall")
        pass

    def removeBlur(self):
      # try:
        textWithBlur = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[2]/div/div[2]/section')
        print(textWithBlur)
        textWithBlurClass = textWithBlur.get_attribute('class')
        textWithBlurP = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[2]/div/div[2]/section/div/p')
        
        textWithBlurPHtmlContent = textWithBlurP.text
        time.sleep(1)
        
        self.driver.execute_script(f'''
          var l = document.getElementsByClassName("{textWithBlurClass}")[0];
          l.parentNode.appendChild(document.createTextNode("{textWithBlurPHtmlContent}"));
        ''')
        time.sleep(1)
        
        self.driver.execute_script(f'''
          var l = document.getElementsByClassName("{textWithBlurClass}")[0];
          l.parentNode.removeChild(l);
        ''')
        time.sleep(1)
        
      # except:
      #   print("Erro ao remover blur")
      #   pass

    def iniciarBot(self):
      self.getLink()
      self.abirSite()
      self.deletePaywallAlert()
      self.removeBlur()
    

bot = PasseiDiretoBot()
bot.iniciarBot()