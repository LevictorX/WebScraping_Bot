from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import xlrd

# Print informando o inicio do bot
print('Iniciando bot...')

# Atribuindo arquivos excel e criando arquivo txt
arq = open('resultado.txt', 'w') #variavel para criação de arquivo.txt para escrita. Onde sera armazenado o resultado da pesquisa do bot
workbook = xlrd.open_workbook('excel.xls') #criando variavel para atribuir a planilha, utilizando a biblioteca xlrd 
sheet = workbook.sheet_by_name('Plan1') #selecionando a pagina "sheet" que vai ser trabalhada na planilha
rows = sheet.nrows #variavel para fazer a contagem de numeros de linhas
columns = sheet.ncols #variavel para fazer a cotagem de numero de colunas
# modulo options para desativar o log do terminal

options = Options() #variavel atribuida ao modulo options do selenium
options.add_argument('--disable-loggin') #argumento adicionado para desabilitar log
options.add_argument('--log-level=3')

# Buscando o executavel do chromedriver e configurando o site a ser automatizado.
driver = webdriver.Chrome('/home/victorgdso/Documentos/Codes/chromedriver', options=options) #Selecionando o diretorio do chromedriver
driver.maximize_window() #configurando para deixar a tela maximizada para quando iniciar o bot
driver.get("https://registro.br/") #pegando o endereço do site a ser acessado

# laço de repetição para pesquisar os dominios listados no excell na area de pesquisa do site e armazenar os que podem ser comprados ou não
for curr_row in range(0, rows):
    x = sheet.cell_value(curr_row, 0) #Leitura das celulas da planilha
    pesquisa = driver.find_element(By.ID,'is-avail-field') #selecionando a barra de pesquisa do site
    time.sleep(1)
    pesquisa.clear() #limpar a barra de pesquisa para iniciar uma nova
    time.sleep(1)
    pesquisa.send_keys(x) #adicionando a barra de pesquisa as celulas da planilha
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN) #enviando o comando de pressionar ENTER
    time.sleep(1)
    driver.find_element(By.XPATH,'//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    time.sleep(1)
    texto = 'Dominio %s %s\n' %(x, driver.find_element(By.XPATH,'//*[@id="app"]/main/section/div[2]/div/p/span/strong').text )
    arq.write(texto)

arq.close()
driver.close()