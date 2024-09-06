from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import schedule

urls = {
    "kabum": ['https://www.kabum.com.br/produto/542929/console-playstation-5-slim-ssd-1tb-edicao-digital-branco-2-jogos-1000038914', 
              '//*[@id="blocoValores"]/div[2]/div[1]/div/h4'],
    "comprarGames": ['https://www.comprargames.com.br/playstation/ps5/console/ps5-slim-digital-lacrado', 
                     '//*[@id="corpo"]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/span/strong'],
    "pontoFrio": ['https://www.pontofrio.com.br/console-playstation-5-slim-edition-branco-returnal-e-ratchet-e-clank-controle-sem-fio-dualsense-branco/p/1566915315?utm_source=Google&utm_medium=BuscaOrganica&utm_campaign=DescontoEspecial', 
                  '//*[@id="product-price"]/span[2]'],
}
def varrer_precos():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1920,1080', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    print("Iniciando a automação!")
    precos_playstation = []

    for key, value in urls.items():
        print("Começando capturar a",key)
        try:
            driver.get(value[0])
            sleep(1.5)
            preco_element = driver.find_element(By.XPATH, value[1])
            preco = preco_element.text
            precos_playstation.append((key,preco))
            print(f"Preço de {[key]} é {preco}")
            sleep(3.5)
        except:
            print(f"problema para acessar a url de {key}")
        try:
            if len(precos_playstation) == len(urls):
                print("Acompanhe agora o resultado das capturas:")
                print()
                for preco in precos_playstation:
                    print(f"{preco[0]}: {preco[1]}")
                    print()
        except:
            print("Número de preços não é igual ao número de sites visitados.")

    print("Finalizando a automação!")
    driver.quit()


schedule.every(15).seconds.do(varrer_precos)

while True:
    schedule.run_pending()
    sleep(1)