from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Importa a classe servide
# selenium -> Ele permite que controla o navegador
# time -> Importa tempo para adicionar pausas (sleep())

import time

# Cria uma classe principal que define todo o jogo
class CookieClicker:
    def __init__(self):
        self.SITE_LINK = "https://www.google.com/" # define o link do jogo
        self.SITE_MAP = {
            "buttons": {
                "xpath": '//*[@id="bigCookie"]'
            },
            "upgrade": {
                "xpath": "//*[@id='product$$NUMBER$$']"
            }
        } # Cria um dicionário vazio para armazenar XPaths do elementos da página
        # Usando o Service para especificar o caminho do chromedriver
        service = Service(executable_path="C:\\Users\\dsadm\\Desktop\\Desktop\\selenium\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service) # Inicializa o ChromeDriver (controlar o navegador Chrome via Selenium, passando para o service)
        self.driver.maximize_window()

    # Vai permitir abrir o site
    def abrir_site(self):
        time.sleep(2) # espera 2 segundos 
        self.driver.get(self.SITE_LINK) # acessar o site do jogo
        time.sleep(10) # espera mais de 10 segundos para garantir que tudo carregue

    # Vai clicar no cookie
    def clicar_no_cookie(self):
        self.driver.find_element_by_xpath(self.SITE_MAP["buttons"]["biscoito"]["xpath"]).click()
        # Ele vai clicar no cookie usando o XPath salvo no site_map

    # Vai encontrar o melhor upgrade possível
    def pegar_melhor_upgrade(self):
        encontrei = False
        elemento_atual = 2

        # Coneça a procurar pelos upgrades disponíveis a partir do item 2
        # Checa a classe do elemento
        while not encontrei:
            objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$NUMBER$$", str(elemento_atual)) 
            classes_objetos = self.driver.find_element_by_xpath(objeto).get_attribute("class")
            
            if not "enable" in classes_objetos: # Se não tiver "enable":, o botão está desativado, então o anterior era o melhor possível
                encontrei = True
            else: 
                elemento_atual += 1
        return elemento_atual - 1 # Vai retornar o índice do melhor upgrade

    # Vai comprar o upgrade
    def comprar_upgrade(self):
        objeto = self.SITE_MAP["buttons"]["upgrade"]["xpath"].replace("$$NUMBER$$", str(self.pegar_melhor_upgrade()))
        self.driver.find_element_by_xpath(objeto).click()
    # Usa o índice retornando para clicar no melhor upgrade
    
biscoito = CookieClicker()
biscoito.abrir_site()
    
# Incrementa o i para que o loop infinito aconteca e clica automático sem parar

i = 0

while True: # Usando o while true
    if i % 500 == 0 and i != 0: # uma lógica que a cada 500 cliques, o script faz uma pausa, compra um upgrade (se for possível) e retorna ao ciclos de cliques
        time.sleep(1)
        biscoito.comprar_upgrade()
        time.sleep(1)
    biscoito.clicar_no_cookie()
    i += 1 # Incrementa o próximo clique repetidamente