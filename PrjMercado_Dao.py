### ACESSO A BASE DE DADOS
#IMPORTA BIBLIOTECAS PUBLICAS E LOCAIS
from PrjMercado_Model import *

########### DEFINE CLASSES ###########
########### CATEGORIA ###########
class CategoriaDao:
    @classmethod
    def clearArq(cls):
        with open('Arq_PrjMerc_Categ.txt', 'w') as arq:       ### excluir todas as linhas do arq
            arq.truncate(0)
    @classmethod
    def salvar(cls, categoria):
        with open('Arq_PrjMerc_Categ.txt', 'a') as arq:
            arq.writelines(categoria + "\n")

    @classmethod
    def ler(cls):
        with open('Arq_PrjMerc_Categ.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace("\n", ""), cls.categoria))  ### retira \n na leitura
        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat

###### PRODUTO
# class ProdutoDao:
#     @classmethod
#     def salvar(cls, produto):
#         with open('Arq_PrjMerc_Produto.txt', 'a') as arq:
#            arq.writelines(produto.nome + "|" +
#                           produto.preco + "|" +
#                           produto.categoria + "\n")
#     @classmethod
#     def ler(cls):
#         with open('Arq_PrjMerc_Produto.txt', 'r') as arq:
#             cls.produto = arq.readlines()
#
#         cls.produto = list(map(lambda x: x.replace("\n", ""), cls.produto))  ### retira \n na leitura
#         cls.produto = list(map(lambda x: x.split("|"), cls.produto))  ### separa registro em cada |
#         prod = []
#         for i in cls.produto:
#             prod.append(Produtos(i[0], i[1], i[2]))
#         return prod
# # p1 = Produtos("sabão", "45", "limpeza/Higiene")
# # ProdutoDao.salvar(p1)
# # pro = ProdutoDao.ler()

###### ESTOQUE
class EstoqueDao:
    @classmethod
    def clearArq(cls):
        with open('Arq_PrjMerc_Estoque.txt', 'w') as arq:       ### excluir todas as linhas do arq
            arq.truncate(0)

    @classmethod
    def salvar(cls, produto: Produtos, qtdEstoque):
        with open('Arq_PrjMerc_Estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" +
                           produto.preco + "|" +
                           produto.categoria + "|" +
                           str(qtdEstoque) + "\n")
    @classmethod
    def ler(cls):
        with open('Arq_PrjMerc_Estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))  ### retira \n na leitura
        cls.estoque = list(map(lambda x: x.split("|"), cls.estoque))  ### separa registro em cada |
        est = []
        if len(cls.estoque) > 0:
           for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        return est

########### VENDA ###########
class VendaDao:
    @classmethod
    def clearArq(cls):
        with open('Arq_PrjMerc_Venda.txt', 'w') as arq:       ### excluir todas as linhas do arq
            arq.truncate(0)

    @classmethod
    def salvar(cls, venda: Venda):
        with open('Arq_PrjMerc_Venda.txt', 'a') as arq:
            arq.writelines(venda.itenVendido.nome + "|" +
                           venda.itenVendido.preco + "|" +
                           venda.itenVendido.categoria + "|" +
                           venda.vendedor + "|" +
                           venda.comprador + "|" +
                           str(venda.qtdVendida) + "|" +
                           str(venda.valVenda) + "|" +
                           venda.datVenda + "\n")

    @classmethod
    def ler(cls):
        with open('Arq_PrjMerc_Venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace("\n", ""), cls.venda))     ### retira \n na leitura
        cls.venda = list(map(lambda x: x.split("|"), cls.venda))            ### separa registro em cada |
        vendareal = []
        for i in cls.venda:
            vendareal.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6], i[7]))
        return vendareal

#p1 = Produtos("abacate", "15", "Diversos")
#v1 = Venda(p1, "vend 01", "comp 04", 999, 300)
#VendaDao.salvar(v1)
vd = VendaDao.ler()
#print(vd[0].itenVendido.nome, vd[0].itenVendido.preco, vd[0].comprador, vd[0].datVenda)

###### FORNECEDOR
class FornecedorDao:
    @classmethod
    def clearArq(cls):
        with open('Arq_PrjMerc_Fornecedor.txt', 'w') as arq:       ### excluir todas as linhas do arq
            arq.truncate(0)

    @classmethod
    def salvar(cls, fornecedor):
        with open('Arq_PrjMerc_Fornecedor.txt', 'a') as arq:
           arq.writelines(fornecedor.nome + "|" +
                          fornecedor.cnpj + "|" +
                          fornecedor.telefone + "|" +
                          fornecedor.categoria + "\n")
    @classmethod
    def ler(cls):
        with open('Arq_PrjMerc_Fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace("\n", ""), cls.fornecedor))  ### retira \n na leitura
        cls.fornecedor = list(map(lambda x: x.split("|"), cls.fornecedor))  ### separa registro em cada |
        fornec = []
        for i in cls.fornecedor:
            fornec.append(Fornecedor(i[0], i[1], i[2],i[3]))
        return fornec
# f1 = Fornecedor("fornec 02", "88888888888888", "21888888888", "Matinal")
# FornecedorDao.salvar(f1)
# fo = FornecedorDao.ler()
# print(fo[0].nome, fo[0].cnpj, fo[0].telefone, fo[0].categoria)

###### PESSOA
class PessoaDao:
    @classmethod
    def clearArq(cls):
        with open('Arq_PrjMerc_Cliente.txt', 'w') as arq:       ### excluir todas as linhas do arq
            arq.truncate(0)

    @classmethod
    def salvar(cls, pessoa):
        with open('Arq_PrjMerc_Cliente.txt', 'a') as arq:
           arq.writelines(pessoa.nome + "|" +
                          pessoa.cpf + "|" +
                          pessoa.telefone + "|" +
                          pessoa.email + "|" +
                          pessoa.endereco + "\n")
    @classmethod
    def ler(cls):
        with open('Arq_PrjMerc_Cliente.txt', 'r') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))  ### retira \n na leitura
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))  ### separa registro em cada |
        cli = []
        for i in cls.clientes:
            cli.append(Pessoa(i[0], i[1], i[2],i[3], i[4]))
        return cli
#p1 = Pessoa("PL Gordinho", "90987890876", "21966666666",
#             "lugordinho@conduzo.com.br","moro logo ali, 1740 casa 3B")
#PessoaDao.salvar(p1)
#pe = PessoaDao.ler()
#print(pe[0].nome, pe[0].cpf, pe[0].telefone, pe[0].email, pe[0].endereco)

# ###### FUNCIONARIO
class FuncionarioDao:
    @classmethod
    def clearArq(cls):
        with open('Arq_PrjMerc_Funcionario.txt', 'w') as arq:       ### excluir todas as linhas do arq
            arq.truncate(0)

    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('Arq_PrjMerc_Funcionario.txt', 'a') as arq:
           arq.writelines(funcionario.nome + "|" +
                          funcionario.cpf + "|" +
                          funcionario.telefone + "|" +
                          funcionario.email + "|" +
                          funcionario.endereco + "|" +
                          funcionario.clt + "\n")
    @classmethod
    def ler(cls):
        with open('Arq_PrjMerc_Funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(map(lambda x: x.replace("\n", ""), cls.funcionario))  ### retira \n na leitura
        cls.funcionario = list(map(lambda x: x.split("|"), cls.funcionario))  ### separa registro em cada |

        func = []
        for i in cls.funcionario:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))
        return func
