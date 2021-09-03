#
#                             FIEMT
#
#
#
#
# To do:
#   - implementar envio de email
#   - Tratamento de erros;
#   - implementação de log
#   - implementar envio de log no email
#   - implementar atualização das url's automaticamente


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

        empresas_si[0].to_csv('Contatos_SI.txt', sep=',', index=False)
        empresas_sic[0].to_csv('Contatos_SI.txt', sep=',', index=False)

    except Exception as ex:
        print(ex)
        print("erro")


if __name__ == "__main__":
    main()
