# usando o playwright

from playwright.sync_api import sync_playwright # permite que crie nosso próprio browser
import time

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False) # permite qual navegador vai usar para testar

    # abre o navegador
    page = browser.new_page()

    # navegar para outra página
    page.goto("https://tailwindcss.com/")

    # pegar infomações da página
    print(f"Site: {page.title()}") # pega o título

    # selecionar o elemento da tela
    # 1° forma: XPATH
    page.locator('xpath=/html/body/div[2]/div/div[2]/div[2]/div[1]/div[6]/div/a').click() # Clica o botão
    time.sleep(2)

    # 2° forma: get_by
    installation = page.get_by_role("link", name='Editor Setup').click() # botão installation
    time.sleep(2)

    editor_setup = page.get_by_role("navigation").get_by_role("link",name='Installation').click() # botão editor_setup
    time.sleep(2)

    compatibility = page.get_by_role("navigation").get_by_role("link", name="Compatibility").click() # botão compatibility
    time.sleep(2)

    upgrade_guide = page.get_by_role("navigation").get_by_role("link", name="Upgrade guide").click() # botão upgrade_guide
    time.sleep(2)

    time.sleep(5)
    browser.close()
