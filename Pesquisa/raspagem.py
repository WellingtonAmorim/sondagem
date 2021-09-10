#
#                             FIEMT
#
# Esse classe tem o objetivo de buscar os respondentes das pesquisas
# da Sondagem Industrial e Sondagem Industrial da Construção no site
# da CNI.
# Verifica quais empresas ainda não responderam.
#
# Retorna uma lista contendo:
#   0: um DataFrame com todas as empresas que participam da pesquisa
#      discriminando as que responderam e as que ainda faltam
#      responder.
#   1: O número de respondentes encontrado.
#
# To do:
#   - Try muito longo, quebrar ele em mais try's
#   - Tratamento de erros;
#   - Arquivo de log
#   - verificar alternativas para o webdriver()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from time import sleep
import numpy as np


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

        except Exception as ex:
            print(ex)
            print('Esperando tabela carregar (2)....')
            sleep(1)
            pass

    return False


def get_respondentes(url, base_empresas):
    print('Iniciando busca por respondentes')
    try:

        driver = webdriver.Chrome()
        driver.get(url)

        element = driver.find_element_by_xpath('//*[@id="txtlogin"]')
        element.send_keys("FIEMT")
        element = driver.find_element_by_xpath('//*[@id="txtSurvey"]')
        element.send_keys("44646MT", Keys.ENTER)

        iframe = driver.find_element_by_xpath('//iframe')
        driver.switch_to.frame(iframe)
        codes_list_si = []

        if espera_tabela_carregar(driver) is True:
            xpath_expression = '//tr/td[1]'
            selenium_codes = driver.find_elements_by_xpath(xpath_expression)

            for id_pesquisa in selenium_codes:
                codes_list_si.append(id_pesquisa.text)
                print(id_pesquisa.text)
        else:
            print('Houve um erro ao carregar a tabela')

        dict_id = {'ID': codes_list_si}

        cod_respondente = pd.DataFrame(dict_id)

        driver.close()

        numero_respostas = cod_respondente.shape[0]

        empresas = pd.read_excel(base_empresas)

        empresas['Copia'] = empresas['Copia'].str.strip()

        empresas.loc[empresas['ID'].isin(cod_respondente['ID'].values), 'Check'] = 'OK'

        empresas.to_csv('bases/Contatos_SI.txt', sep=',', index=False, header=False)

        empresas.columns = ['name', 'code', 'email', 'copy', 'check']

        empresas = empresas.replace(np.nan, '', regex=True)

        print('Atualização de contatos de SI terminado.')

        empresas_respostas = [empresas, numero_respostas]

        return empresas_respostas

    except Exception as ex:
        print(ex)
        print('Erro na Busca por respondentes')
