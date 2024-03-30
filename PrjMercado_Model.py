### MODELAGEM DOS DADOS
#IMPORTA BIBLIOTECAS PUBLICAS E LOCAIS
from datetime import datetime

# DEFINE CLASSES

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, qtdEstoque):
        self.produto = produto
        self.qtdEstoque = qtdEstoque

class Venda:
    def __init__(self, itenVendido: Produtos, vendedor, comprador, qtdVendida, valVenda, datVenda = datetime.now().strftime("%d/%m/%y")):
        self.itenVendido = itenVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.qtdVendida = qtdVendida
        self.valVenda = valVenda
        self.datVenda = datVenda

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

""" class Funcionario(Pessoa):
    def __init__(self, dadosPessoa: Pessoa, clt):
        self.dadosPessoa = dadosPessoa
        self.clt = clt """

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, endereco, clt):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, telefone, email, endereco)
