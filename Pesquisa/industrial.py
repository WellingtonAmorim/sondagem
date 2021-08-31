import time
start_time = time.time()

# Ler contatos
def get_contacts(sondagem):
    names = []
    codes = []
    emails = []
    copys = []
    checks = []
    with open(sondagem, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(",")[0])
            codes.append(a_contact.split(",")[1])
            emails.append(a_contact.split(",")[2])
            copys.append(a_contact.split(",")[3])
            checks.append(a_contact.split(",")[4])
    return names, codes, emails, copys, checks

#Ler mensagem html
from string import Template

def read_template(mensagem_si):
    with open(mensagem_si, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# import the smtplib module. It should be included in Python by default
import smtplib

names, codes, emails, copys, checks = get_contacts('C:/Users/caio.hatanaka/PycharmProjects/pythonProject/Contatos_SI.txt')  # read contacts
message_template = read_template('mensagem_si.html')

# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# For each contact, send the email:
for name, code, email, copy, check in zip(names, codes, emails, copys, checks):
    # set up the SMTP server
    CAIO_USER = 'caio.hatanaka@fiemt.ind.br'
    CAIO_PASS = 'Hatanaka100!'
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(CAIO_USER, CAIO_PASS)
    if ("OK" in check):
        continue

    msg = MIMEMultipart()  # create a message

    # add in the actual person name to the message template
    mensagem_si = message_template.substitute(NAME=name.title(), CODE=code.title())

    # setup the parameters of the message
    msg['From'] = CAIO_USER
    msg['To'] = email
    msg['Cc'] = copy
    msg['Subject'] = "Sondagem Industrial - Jul/2021"

    # add in the message body
    msg.attach(MIMEText(mensagem_si, 'html'))
    print(name.title())
    print(code.title())
    # send the message via the server set up earlier.
    s.send_message(msg)

    del msg
    s.quit()

print('Todos os emails do SI foram enviados')

print("--- %s seconds ---" % (time.time() - start_time))