import pandas as pd

# Função que será chamada no lugar de `addtb`
def addtb(cpf, nome):
    # Implementar a função de acordo com a necessidade
    print(f"CPF: {cpf}, Nome: {nome}")

# Ler o arquivo Excel
all_arq_excel = pd.read_excel('../Dados.xlsx')

# Converter os dados para CSV
dados_brutos = all_arq_excel.to_csv(index=False)

# Dividir os dados em linhas
dados = dados_brutos.split('\n')

# Remover o cabeçalho
dados_clean = dados[1:]

# Mapear os dados e processar
for res in dados_clean:
    data_build = res.split(',')
    if len(data_build) < 2:
        continue  # Ignorar linhas incompletas
    cpf = data_build[0]
    nome = data_build[1]
    if cpf.strip():
        addtb(cpf, nome)