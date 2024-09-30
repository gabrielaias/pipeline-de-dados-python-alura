from processamento_dados import Dados

# Definindo os caminhos para os arquivos de dados
path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extraindo dados da Empresa A
dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.nome_colunas)  # Exibe os nomes das colunas da Empresa A
print(dados_empresaA.qtd_linhas)     # Exibe a quantidade de linhas da Empresa A

# Extraindo dados da Empresa B
dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)  # Exibe os nomes das colunas da Empresa B
print(dados_empresaB.qtd_linhas)     # Exibe a quantidade de linhas da Empresa B

# Transformando os nomes das colunas para padronização
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

# Renomeando as colunas da Empresa B
dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)  # Exibe os novos nomes das colunas da Empresa B

# Realizando a fusão dos dados das duas empresas
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)      # Exibe os nomes das colunas do conjunto de dados combinado
print(dados_fusao.qtd_linhas)         # Exibe a quantidade de linhas no conjunto de dados combinado

# Salvando os dados combinados em um novo arquivo CSV
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'Dados combinados salvos em: {path_dados_combinados}')

