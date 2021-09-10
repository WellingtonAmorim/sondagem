#
#                             FIEMT
#
# To do:
#   - implementar caso o data frame recebido esteja vazio
#   - Ocultar Email e senha
#   - Arquivo de log
#   - verificar alternativas para o webdriver()

import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import numpy as np


def read_template(mensagem_si):
    with open(mensagem_si, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def envia_email_pesquisa(lista_empresas,assunto,layout_menssagem):
    message_template = read_template(layout_menssagem)
    for index, row in lista_empresas.iterrows():
        try:
            print(row['check'])
            print(row['copy'])
            # set up the SMTP server
            CAIO_USER = 'caio.hatanaka@fiemt.ind.br'
            CAIO_PASS = 'Hatanaka100!'
            s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
            s.starttls()
            s.login(CAIO_USER, CAIO_PASS)
            if (row['check'] == "OK"):
                continue

            msg = MIMEMultipart()  # create a message

            # add in the actual person name to the message template
            mensagem_si = message_template.substitute(NAME=row['name'], CODE=row['code'])

            # setup the parameters of the message
            msg['From'] = CAIO_USER
            msg['To'] = row['email']
            msg['Cc'] = row['copy']
            msg['Subject'] = assunto

            # add in the message body
            msg.attach(MIMEText(mensagem_si, 'html'))
            print(row['name'])
            print(row['code'])
            # send the message via the server set up earlier.
            s.send_message(msg)

            del msg
            s.quit()
            print('Todos os emails do SI foram enviados')

        except Exception as ex:
            print(ex)
            cod = row['code']
            name = row['name']
            print(f'Deu ruim no {cod, name}')

#
#df = pd.read_csv('bases/Contatos_SIC.txt')
#df = df.replace(np.nan, '', regex=True)
#
#assunto_email_sic = "Sondagem Indústria da Construção - Ago/2021"
#caminho_mensagem = "mensagens/mensagem_sic.html"
#envia_email_pesquisa(df,assunto_email_sic,caminho_mensagem)
#
#
#