import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()  # Lê os dados ao inicializar
        self.nome_colunas = self.get_columns()  # Obtém os nomes das colunas
        self.qtd_linhas = self.size_data()  # Conta a quantidade de linhas

    def leitura_json(self):
        # Lê os dados de um arquivo JSON
        with open(self.path, 'r') as file:
            return json.load(file)

    def leitura_csv(self):
        # Lê os dados de um arquivo CSV
        with open(self.path, 'r') as file:
            return list(csv.DictReader(file, delimiter=','))

    def leitura_dados(self):
        # Lê os dados com base no tipo especificado (CSV ou JSON)
        if self.tipo_dados == 'csv':
            return self.leitura_csv()
        elif self.tipo_dados == 'json':
            return self.leitura_json()
        return []

    def get_columns(self):
        # Retorna os nomes das colunas dos dados
        return list(self.dados[0].keys()) if self.dados else []

    def rename_columns(self, key_mapping):
        # Renomeia as colunas com base em um mapeamento de chaves
        for old_dict in self.dados:
            for old_key in list(old_dict.keys()):
                new_key = key_mapping.get(old_key, old_key)
                old_dict[new_key] = old_dict.pop(old_key)  # Renomear chave
        self.nome_colunas = self.get_columns()  # Atualiza os nomes das colunas

    def size_data(self):
        # Retorna a quantidade de linhas nos dados
        return len(self.dados)

    @classmethod
    def join(cls, dadosA, dadosB):
        # Junta os dados de duas instâncias da classe Dados
        new_instance = cls([], 'list')  # Cria uma nova instância
        new_instance.dados = dadosA.dados + dadosB.dados  # Combina os dados
        new_instance.nome_colunas = dadosA.nome_colunas  # Mantém os nomes das colunas da primeira instância
        new_instance.qtd_linhas = len(new_instance.dados)  # Atualiza a quantidade de linhas
        return new_instance

    def transformar_dados_para_tabela(self):
        # Converte os dados em um formato de tabela
        tabela = [self.nome_colunas]  # Adiciona os nomes das colunas como a primeira linha
        for row in self.dados:
            tabela.append([row.get(col, 'Indisponível') for col in self.nome_colunas])  # Preenche os dados
        return tabela

    def salvando_dados(self, path):
        # Salva os dados em um arquivo CSV
        dados_tabela = self.transformar_dados_para_tabela()  # Converte os dados para tabela
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(dados_tabela)  # Escreve os dados no arquivo