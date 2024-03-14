from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

class PasseiDiretoBot:
    def __init__(self):
      options = webdriver.ChromeOptions()
      options.add_argument('lang=pt-br')
      options.add_experimental_option("detach", True)
      self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    

    def getLink(self):
      try:
        path = os.getcwd() + "//" + "./index.html"
        self.driver.get("file://" + path)

        self.link = input("Digite o Link: ")
      
      except Exception:
        print("Erro ao pegar o link")
        pass


    def abirSite(self):
      try:
        self.driver.get(self.link)
        time.sleep(2)
      
      except Exception:
        print("Erro ao abrir o site")
        pass


    def deletePaywallAlert(self):
      try:
        paywallAlert = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[3]')
        paywallAlertClass = paywallAlert.get_attribute('class')
        self.driver.execute_script(f'''
          var l = document.getElementsByClassName("{paywallAlertClass}")[0];
          l.parentNode.removeChild(l);
        ''')
        time.sleep(1)
      except Exception:
        print("Erro ao remover paywall")
        pass


    def removeFeedBack(self):
      try:
        feedback = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[2]/div/div[2]/div')
        feedbackClass = feedback.get_attribute('class')
        self.driver.execute_script(f'''
          var l = document.getElementsByClassName("{feedbackClass}")[0];
          l.parentNode.removeChild(l);
        ''')
        time.sleep(1)
      except Exception:
        print("Erro ao remover feedback")
        pass


    def removeBlur(self):
      try:
        textWithBlur = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[2]/div/div[2]/section')
        textWithBlurClass = textWithBlur.get_attribute('class')
        textWithBlurP = self.driver.find_element('xpath', '//*[@id="viewer-wrapper"]/div[2]/div/section/div/div[2]/div/div[2]/section/div/p')
        
        textWithBlurPHtmlContent = textWithBlurP.text.split('\n')
        time.sleep(1)

        script = f'''
          var l = document.getElementsByClassName("{textWithBlurClass}")[0];
        '''

        # Adicionando cada parágrafo como um elemento <p>
        for paragraph in textWithBlurPHtmlContent:
            script += f'''
              var p = document.createElement("p");
              p.innerText = `{paragraph}`;
              p.innerHTML += "<br />";
              l.parentNode.appendChild(p);
            '''

        self.driver.execute_script(script)

        time.sleep(1)
        
        self.driver.execute_script(f'''
          var l = document.getElementsByClassName("{textWithBlurClass}")[0];
          l.parentNode.removeChild(l);
        ''')
        time.sleep(1)
        
      except Exception:
        print("Erro ao remover blur")
        pass


    def iniciarBot(self):
      self.getLink()
      self.abirSite()
      self.deletePaywallAlert()
      self.removeFeedBack()
      self.removeBlur()
    

bot = PasseiDiretoBot()
bot.iniciarBot()