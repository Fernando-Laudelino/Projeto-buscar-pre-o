from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl


driver = webdriver.Chrome()

driver.get(
    "https://www.kabum.com.br/computadores/monitores?int_banner_name=MSI_MONITORES&int_banner_position=MENU_SUSPENSO&gad_source=1&gclid=CjwKCAiAlJKuBhAdEiwAnZb7lXZb04td7FCRbbrrxxwhWDUyOjW052KM1tqOh9Bu1oScwlJRy6KMIxoCHOgQAvD_BwE"
)

titulos = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")
valores = driver.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

# Criar a planilha
workbook = openpyxl.Workbook()
# Criando a aba do produto
workbook.create_sheet(title='Monitor')
# Selecionar a página de produtos
sheet_monitor = workbook['Monitor']
sheet_monitor['A1'].value = 'Produto'
sheet_monitor['b1'].value = 'Preco'
workbook.save('produtos.xlsx') 
# Faz a leitura e salva em colunas.
for t,v in zip (titulos,valores):
    sheet_monitor.append([t.text,v.text])
workbook.save('produtos.xlsx')



