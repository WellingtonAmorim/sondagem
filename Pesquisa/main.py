#
#                             FIEMT
#
# To do:
#   - implementar envio de email
#   - Tratamento de erros;
#   - implementação de log
#   - implementar envio de log no email
#   - implementar atualização das url's automaticamente


import raspagem
import email
import numpy as np

def main():
    # Define as URL's das pesquisas. Tem que alterar mes e ano
    url_si = "https://enquetes.sphinxnaweb.com/cnipesquisa/SI_ago_2021/relat%C3%B3rio.htm"
    url_sic = "https://enquetes.sphinxnaweb.com/cnipesquisa/SIC_ago_2021/relat%C3%B3rio.htm"

    # Define o caminho das bases de industrias.
    # Elas são enviadas pela CNI, e atualizadas anualmente por eles.
    path_empresas_si = "bases/SI.xlsx"
    path_empresas_sic = "bases/SIC.xlsx"

    try:
        # Executa função de raspagem, do arquivo raspagem.py
        # envia como parâmetros a url da pesquisa
        # e o caminho da lista de empresas.
        # Retorna uma lista de duas dimensões com um dataframe
        # e o número de respondentes
        empresas_si = raspagem.get_respondentes(url_si, path_empresas_si)
        empresas_sic = raspagem.get_respondentes(url_sic, path_empresas_sic)

        #Linhas comentadas caso campo copy esteja em branco
        #empresas_si[0] = empresas_si[0].replace(np.nan, '', regex=True)
        #empresas_sic[0] = empresas_sic[0].replace(np.nan, '', regex=True)

        print(f'Empresas da Sondagem Industrial: {empresas_si[0]}')
        print(f'Empresas da Sondagem da Construção: {empresas_sic[0]}')
        print(f'Número de respondentes da Sondagem Industrial: {empresas_si[1]}')
        print(f'Número de respondentes da Sondagem da Construção: {empresas_sic[1]}')

        #Salva em CSV a lista de empresas da raspagem, ela não é utilizada para enviar
        #Utilizado apenas para consulta pessoal
        empresas_si[0].to_csv('Contatos_SI.txt', sep=',', index=False)
        empresas_sic[0].to_csv('Contatos_SIC.txt', sep=',', index=False)

        #Executa função de envio de email para sondagem industrial
        assunto_email_si = "Sondagem Industrial - Ago/2021"
        caminho_mensagem_si = "mensagens/mensagem_si.html"
        email.envia_email_pesquisa(empresas_si[0], assunto_email_si, caminho_mensagem_si)

        #Executa função de envio de email para Construção
        assunto_email_sic = "Sondagem Indústria da Construção - Ago/2021"
        caminho_mensagem_sic = "mensagens/mensagem_sic.html"
        email.envia_email_pesquisa(empresas_sic[0], assunto_email_sic, caminho_mensagem_sic)


    except Exception as ex:
        print(ex)
        print("erro")


if __name__ == "__main__":
    main()
