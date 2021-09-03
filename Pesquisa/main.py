#
#                             FIEMT
#
#
#
#
# Retorna uma lista contendo:
#   0: um DataFrame com todas as empresas que participam da pesquisa
#      discriminando as que responderam e as que ainda faltam
#      responder.
#   1: O número de respondentes encontrado.
#
# To do:
#   - Tratamento de erros;
#   - Arquivo de log
#   - implementar envio de log no email


import raspagem


def main():
    url_si = "https://enquetes.sphinxnaweb.com/cnipesquisa/SI_ago_2021/relat%C3%B3rio.htm"
    path_empresas_si = "bases/SI.xlsx"
    url_sic = "https://enquetes.sphinxnaweb.com/cnipesquisa/SIC_ago_2021/relat%C3%B3rio.htm"
    path_empresas_sic = "bases/SIC.xlsx"

    try:
        empresas_si = raspagem.get_respondentes(url_si, path_empresas_si)
        empresas_sic = raspagem.get_respondentes(url_sic, path_empresas_sic)

        print(f'Empresas da Sondagem Industrial: {empresas_si[0]}')
        print(f'Empresas da Sondagem da Construção: {empresas_sic[0]}')
        print(f'Número de respondentes da Sondagem Industrial: {empresas_si[1]}')
        print(f'Número de respondentes da Sondagem da Construção: {empresas_sic[1]}')
    except Exception as ex:
        print(ex)
        print("erro")


if __name__ == "__main__":
    main()
