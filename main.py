from selenium import webdriver # selenium -> Ele permite que controla o navegador
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
import time # time -> Importa tempo para adicionar pausas (sleep())

service = Service(executable_path="chromedriver.exe") # Local do service para abrir
driver = webdriver.Chrome(service=service) # Usando o driver para o Chromo

driver.get('https://www.google.com/') # Permite que vai abrir o navegador pelo link desejado que colocou

input_element = driver.find_element(By.CLASS_NAME, "gLFyf") # Outra parte, para controlar o input, o usuário precisa encontrar o nome da CLASSE
input_element.send_keys("You need to type anything for this search") # Envia as chaves para dentro do input do Google

time.sleep(5) # O navegador fica aberto por 5 segundos

driver.quit() # Após 5 segundos, o navegador fecha automáticamente

