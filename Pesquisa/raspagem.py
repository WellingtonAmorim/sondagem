from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from time import sleep


def espera_tabela_carregar(driver, timeout_second=60):
    print('Iniciando o processo de espera da tabela')
    first_time = time.time()
    xpath_expression = '//tr/td[1]'
    while time.time() - first_time <= timeout_second:

        try:
            elements = driver.find_elements_by_xpath(xpath_expression)
            if len(elements) > 1:
                return True
            else:
                print('Esperando tabela carregar (1)....')
                sleep(1)

        except:
            print('Esperando tabela carregar (2)....')
            sleep(1)
            pass

    return False

driver = webdriver.Chrome()
driver.get("https://enquetes.sphinxnaweb.com/cnipesquisa/SI_ago_2021/relat%C3%B3rio.htm")

element = driver.find_element_by_xpath('//*[@id="txtlogin"]')
element.send_keys("FIEMT")
element = driver.find_element_by_xpath('//*[@id="txtSurvey"]')
element.send_keys("44646MT", Keys.ENTER)

iframe = driver.find_element_by_xpath('//iframe')
driver.switch_to.frame(iframe)

if espera_tabela_carregar(driver) is True:

    xpath_expression = '//tr/td[1]'
    selenium_codes = driver.find_elements_by_xpath(xpath_expression)
    codes_list_SI = []
    for id in selenium_codes:
        codes_list_SI.append(id.text)
        print(id.text)
else:
    print('Houve um erro ao carregar a tabela')

dict = {'ID': codes_list_SI}
df = pd.DataFrame(dict)
df.to_excel('temp/Selenium_codes_SI.xlsx')

driver.close()

df1 = pd.read_excel('SI.xlsx')
df2 = pd.read_excel('temp/Selenium_codes_SI.xlsx')

df1['Copia'] = df1['Copia'].str.strip()

df1.loc[df1['ID'].isin(df2['ID'].values ), 'Check'] = 'OK'

df1.to_csv('Contatos_SI.txt', sep=',', index=False, header=False)

print('Atualização de contatos de SI terminado.')



#def espera_tabela_carregar(driver, timeout_second=60):
#    print('Iniciando o processo de espera da tabela')
#    first_time = time.time()
#    xpath_expression = '//tr/td[1]'
#    while time.time() - first_time <= timeout_second:
#
#        try:
#            elements = driver.find_elements_by_xpath(xpath_expression)
#            if len(elements) > 1:
#                return True
#            else:
#                print('Esperando tabela carregar (1)....')
#                sleep(1)
#
#        except:
#            print('Esperando tabela carregar (2)....')
#            sleep(1)
#            pass
#
#    return False
#
#driver = webdriver.Chrome()
#driver.get("https://enquetes.sphinxnaweb.com/cnipesquisa/SIC_jul_2021/relat%C3%B3rio.htm")
#
#element = driver.find_element_by_xpath('//*[@id="txtlogin"]')
#element.send_keys("FIEMT")
#element = driver.find_element_by_xpath('//*[@id="txtSurvey"]')
#element.send_keys("44646MT", Keys.ENTER)
#
#iframe = driver.find_element_by_xpath('//iframe')
#driver.switch_to.frame(iframe)
#
#if espera_tabela_carregar(driver) is True:
#
#    xpath_expression = '//tr/td[1]'
#    selenium_codes = driver.find_elements_by_xpath(xpath_expression)
#    codes_list_SIC = []
#    for id in selenium_codes:
#        codes_list_SIC.append(id.text)
#        print(id.text)
#else:
#    print('Houve um erro ao carregar a tabela')
#
#dict = {'ID': codes_list_SIC}
#df = pd.DataFrame(dict)
#df.to_excel('Selenium_codes_SIC.xlsx')
#
#driver.close()
#
#df3 = pd.read_excel('SIC.xlsx')
#df4 = pd.read_excel('Selenium_codes_SIC.xlsx')
#
#df3['Copia'] = df3['Copia'].str.strip()
#
#df3.loc[df3['ID'].isin(df4['ID'].values), 'Check'] = 'OK'
#
#df3.to_csv('arquivos/Contatos_SIC.txt', sep=',', index=False, header=False)
#
#print('Atualização de contatos de SIC terminado.')