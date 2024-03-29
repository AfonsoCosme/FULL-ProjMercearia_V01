### LOGICA DO SISTEMA
from PrjMercado_Model import *
from PrjMercado_Dao import *
from datetime import datetime

########### DEFINE CLASSES ###########
###########
########### CATEGORIA ############
###########
class CategoriaCont:
    def CadastraCategoria(self, novaCategoria):
        verifCad = CategoriaDao.ler()
        existeCat = list(filter(lambda verifCad: verifCad.categoria == novaCategoria, verifCad))

        if not existeCat:
            CategoriaDao.salvar(novaCategoria)
            print('CATEGORIA cadastrada com SUCESSO')
        else:
            print('*** CATEGORIA já cadastrada ***')

    def DeleteCategoria(self, deleteCategoria):
        verifCad = CategoriaDao.ler()
        existeCat = list(filter(lambda verifCad: verifCad.categoria == deleteCategoria, verifCad))

        if existeCat:
            existeCat = list(filter(lambda verifCad: verifCad.categoria != deleteCategoria, verifCad))
            CategoriaDao.clearArq()
            for i in existeCat:
                CategoriaDao.salvar(i.categoria)
            print("CATEGORIA removida com SUCESSO")
        else:
            print("*** CATEGORIA não cadastrada ***")

    def AlteraCategoria(self, alteraCategoria, newCategoria):
        verifCad = CategoriaDao.ler()
        existeCat = list(filter(lambda verifCad: verifCad.categoria == alteraCategoria, verifCad))

        if existeCat:
            existeNew = list(filter(lambda verifCad: verifCad.categoria == newCategoria, verifCad))
            if not existeNew:
                verifCad = list(map(lambda verifCad: Categoria(newCategoria)
                                        if(verifCad.categoria == alteraCategoria)
                                        else(verifCad), verifCad))
                CategoriaDao.clearArq()
                for i in verifCad:
                    CategoriaDao.salvar(i.categoria)
                print("CATEGORIA alterada com SUCESSO")
            else:
                print("*** nova CATEGORIA já cadastrada ***")
        else:
            print("*** CATEGORIA não cadastrada ***")

    def ListaCategoria(self):
        verifCad = CategoriaDao.ler()
        if verifCad:
            for i in verifCad:
                print(f'Categoria: {i.categoria}')
        else:
            print('*** nenhuma CATEGORIA cadastrada ***')

###########
############ ESTOQUE ############
###########
class EstoqueCont:
    def CadastraProduto(self, nome, preco, categoria, qtdEstoque):
        verifProd = EstoqueDao.ler()
        verifCat = CategoriaDao.ler()
        existeProd = list(filter(lambda verifProd: verifProd.produto.nome == nome, verifProd))
        existeCat = list(filter(lambda verifProd: verifProd.categoria == categoria, verifCat))

        if existeCat:
            if not existeProd:
                produto = Produtos(nome, preco, categoria)
                EstoqueDao.salvar(produto, qtdEstoque)
                print('PRODUTO cadastrado com SUCESSO')
            else:
                print('*** PRODUTO já cadastrado ***')
        else:
            print('*** CATEGORIA não cadastrada ***')

    def DeleteProduto(self, nome):
        verifProd = EstoqueDao.ler()
        existeProd = list(filter(lambda verifProd: verifProd.produto.nome == nome, verifProd))

        if existeProd:
            existeProd = list(filter(lambda verifProd: verifProd.produto.nome != nome, verifProd))
            EstoqueDao.clearArq()
            for i in existeProd:
                EstoqueDao.salvar(Produtos(i.produto.nome,
                                           i.produto.preco,
                                           i.produto.categoria),
                                  str(i.qtdEstoque))
            print("PRODUTO removido com SUCESSO")
        else:
            print("*** PRODUTO não cadastrado ***")

    def AlteraProduto(self, alteraProduto, novonomeProduto, novoprecoProduto, novacategoriaProduto, novaqtdProduto):
        verifProd = EstoqueDao.ler()
        verifCat = CategoriaDao.ler()
        existeProd = list(filter(lambda verifProd: verifProd.produto.nome == alteraProduto, verifProd))
        existePNew = list(filter(lambda verifProd: verifProd.produto.nome == novonomeProduto, verifProd))
        existeCat = list(filter(lambda verifProd: verifProd.categoria == novacategoriaProduto, verifCat))

        if existeCat:
            if existeProd:
                if not existePNew:
                    verifProd = list(map(lambda verifProd: Estoque(Produtos(novonomeProduto,
                                                                            novoprecoProduto,
                                                                            novacategoriaProduto),
                                                                            novaqtdProduto)
                                if (verifProd.produto.nome == alteraProduto)
                                else (verifProd), verifProd))
                    EstoqueDao.clearArq()
                    for i in verifProd:
                        EstoqueDao.salvar(Produtos(i.produto.nome,
                                                   i.produto.preco,
                                                   i.produto.categoria),
                                          str(i.qtdEstoque))
                    print('PRODUTO alterado com SUCESSO')
                else:
                    print('*** NOVO PRODUTO já cadastrado ***')
            else:
                print('*** PRODUTO não cadastrado ***')
        else:
            print('*** CATEGORIA não cadastrada ***')

    def ListaEstoque(self, produto):
        verifProd = EstoqueDao.ler()
        existeProd = list(filter(lambda verifProd: verifProd.produto.nome == produto, verifProd))
        if existeProd:
            for i in existeProd:
                print(f'O estoque do produto: {i.produto.nome} '
                      f'da categoria: {i.produto.categoria} '
                      f'com preço de: {i.produto.preco} '
                      f'é de {i.qtdEstoque}')
        else:
            print('*** PRODUTO não cadastrado ***')

###########
########### VENDA ###########
###########
class VendaCont:
    def CadastraVenda(self, nomeProduto, vendedor, comprador, qtdCompra):
        verifProd = EstoqueDao.ler()
        existeProd = list(filter(lambda verifProd: verifProd.produto.nome == nomeProduto, verifProd))

        if existeProd:
            if int(qtdCompra) <= int(existeProd[0].qtdEstoque):
                newEstoque = int(existeProd[0].qtdEstoque) - int(qtdCompra)
                valCompra = int(existeProd[0].produto.preco) * int(qtdCompra)

                verifProd = list(map(lambda verifProd:
                                     Estoque(Produtos(nomeProduto,
                                                      verifProd.produto.preco,
                                                      verifProd.produto.categoria),
                                            newEstoque)
                                    if (verifProd.produto.nome == nomeProduto)
                                    else (verifProd), verifProd))
                ### grava arq ESTOQUE
                EstoqueDao.clearArq()
                for i in verifProd:
                    EstoqueDao.salvar(Produtos(i.produto.nome,
                                               i.produto.preco,
                                               i.produto.categoria),
                                      str(i.qtdEstoque))
                ### grava arq VENDA
                prodVendido = Venda(Produtos(nomeProduto, existeProd[0].produto.preco, existeProd[0].produto.categoria),
                                    vendedor,
                                    comprador,
                                    str(qtdCompra),
                                    str(valCompra))
                VendaDao.salvar(prodVendido)
                print('PRODUTO vendido com SUCESSO')
            else:
                print('QUANTIDADE da venda maior que estoque')
        else:
            print('*** PRODUTO não cadastrado ***')

    def ListaMaiorVenda(self):
        verifVenda = VendaDao.ler()
        prodVendidos = []

        for i in verifVenda:
            prodArq = i.itenVendido.nome
            qtdArq = i.qtdVendida
            prodLis = list(filter(lambda x: x['prod: '] == prodArq, prodVendidos))
            if prodLis:
                prodVendidos = list(map(lambda x: {'prod: ': prodArq, 'qtd: ': int(qtdArq) + int(x['qtd: '])}
                                        if (x['prod: '] == prodArq)
                                        else (x), prodVendidos))
            else:
                prodVendidos.append({'prod: ': prodArq, 'qtd: ': qtdArq})

        prodLisOrd = sorted(prodVendidos, key=lambda k: int(k['qtd: ']), reverse=True)
        classif = 1
        print('========== RANKING PRODUTOS MAIS VENDIDOS ==========')
        for i in prodLisOrd:
            print(f'Ranking : {classif} / Produto: {i['prod: ']}')
            classif +=1

    def ListaVendaPeriodo(self, datIni, datFim):
        veriVenda = VendaDao.ler()
        datIniConv = datetime.strptime(datIni, '%d/%m/%Y')
        datFimConv = datetime.strptime(datFim, '%d/%m/%Y')
        exiteVenda = list(filter(lambda x: datetime.strptime(x.datVenda, '%d/%m/%Y') >=datIniConv and
                                           datetime.strptime(x.datVenda, '%d/%m/%Y') <= datFimConv, veriVenda))

        if exiteVenda:
            print('********** VENDAS DO PERÍODO **********')
            print(f"        {datIni} a {datFim}")
            print('***************************************')

            totVenda = 0
            totQtd = 0
            for i in exiteVenda:
                totVenda += float(i.valVenda)
                totQtd += int(i.qtdVendida)
                print(f"Data: {i.datVenda} "
                      f"Produto: {i.itenVendido.nome}  "
                      f"Cat: {i.itenVendido.categoria}  "
                      f"Vend: {i.vendedor}  "
                      f"Comp: {i.comprador}  "
                      f"Qtd: {i.qtdVendida}  "
                      f"R$: {i.valVenda}  ")
            print('***************************************')
            print(f"Total Venda: {totVenda} Total Produtos Vendidos: {totQtd}")
        else:
            print(f"Sem vendas para o período de {datIni} a {datFim}")

###########
########### FORNECEDOR ############
###########
class FornecedorCont:
    def CadastraFornecedor(self, nome, novoCnpj, telefone, novaCategoria):
        verifFornec = FornecedorDao.ler()
        verifCad = CategoriaDao.ler()
        existeFornec = list(filter(lambda verifFornec: verifFornec.cnpj == novoCnpj and
                                                       verifFornec.categoria == novaCategoria, verifFornec))
        existeCat = list(filter(lambda verifCad: verifCad.categoria == novaCategoria, verifCad))

        if not existeFornec:
            if not existeCat:
                print('CATEGORIA não cadastrada')
            else:
                FornecedorDao.salvar(Fornecedor(nome, 
                                                novoCnpj, 
                                                telefone, 
                                                novaCategoria))
                print('FORNECEDOR/CATEGORIA cadastrado com SUCESSO')
        else:
            print('*** FORNECEDOR/CATEGORIA já cadastrado ***')

    def DeleteFornecedor(self, deleteCnpj, deleteCategoria):
        verifFornec = FornecedorDao.ler()
        existeFornec = list(filter(lambda verifFornec: verifFornec.cnpj == deleteCnpj and
                                                       verifFornec.categoria == deleteCategoria, verifFornec))

        if existeFornec:
            existeFornec = list(filter(lambda verifFornec: verifFornec.cnpj != deleteCnpj or
                                                           verifFornec.categoria != deleteCategoria, verifFornec))
            FornecedorDao.clearArq()
            for i in existeFornec:
                FornecedorDao.salvar(Fornecedor(i.nome, 
                                                i.cnpj, 
                                                i.telefone, 
                                                i.categoria))
            print("FORNECEDOR/CATEGORIA removido com SUCESSO")
        else:
            print("*** FORNECEDOR/CATEGORIA não cadastrado ***")

    def AlteraFornecedor(self, atuCnpj, atuCategoria, alteraNome, alteraCnpj, alteraTelefone, alteraCategoria):
            verifFornec = FornecedorDao.ler()
            verifCad = CategoriaDao.ler()
            existeFornec = list(filter(lambda verifFornec: verifFornec.cnpj == atuCnpj and
                                       verifFornec.categoria == atuCategoria, verifFornec))
            existeCat = list(filter(lambda verifCad: verifCad.categoria == atuCategoria, verifCad))

            if existeFornec:
                if existeCat:
                    verifFornec = list(map(lambda verifFornec:
                                           Fornecedor(alteraNome,
                                                      alteraCnpj,
                                                      alteraTelefone,
                                                      alteraCategoria)
                                    if (verifFornec.cnpj == atuCnpj and
                                        verifFornec.categoria == atuCategoria)
                                    else (verifFornec), verifFornec))

                    FornecedorDao.clearArq()
                    for i in verifFornec:
                        FornecedorDao.salvar(Fornecedor(i.nome,
                                                        i.cnpj,
                                                        i.telefone,
                                                        i.categoria))
                    print('FORNECEDOR/CATEGORIA alterado com SUCESSO')
                else:
                    print('CATEGORIA não cadastrada')
                
            else:
                print('*** FORNECEDOR/CATEGORIA não cadastrado ***')

    def ListaFornecedor(self):
            verifFornec = FornecedorDao.ler()
    
            if verifFornec:
                for i in verifFornec:
                    print(f'Fornecedor: {i.nome} '
                          f'CNPJ: {i.cnpj} '
                          f'Telefone: {i.telefone} '
                          f'Categoria {i.categoria}')
            else:
                print('*** sem FORNECEDOR/CATEGORIA não cadastrado ***')

###########
########### PESSOA ############
###########
class PessoaCont:
    def CadastraPessoa(self, nome, novoCpf, telefone, email, endereco):
        verifPessoa = PessoaDao.ler()
        existePessoa = list(filter(lambda verifPessoa: verifPessoa.cpf == novoCpf, verifPessoa))

        if not existePessoa:
            PessoaDao.salvar(Pessoa(nome, 
                                    novoCpf, 
                                    telefone, 
                                    email, 
                                    endereco))
            print('CLIENTE cadastrado com SUCESSO')
        else:
            print('*** CLIENTE já cadastrado ***')

    def DeletePessoa(self, deleteCpf):
        verifPessoa = PessoaDao.ler()
        existePessoa = list(filter(lambda verifPessoa: verifPessoa.cpf == deleteCpf, verifPessoa))

        if existePessoa:
            existePessoa = list(filter(lambda verifPessoa: verifPessoa.cpf != deleteCpf, verifPessoa))

            PessoaDao.clearArq()
            for i in existePessoa:
                PessoaDao.salvar(Pessoa(i.nome, 
                                        i.cpf, 
                                        i.telefone, 
                                        i.email, 
                                        i.endereco))
            print("CLIENTE removido com SUCESSO")
        else:
            print("*** CLIENTE não cadastrado ***")



teste = PessoaCont()
teste.CadastraPessoa('CM/AfonsoCosme', '333', '(21)98855-9341', 'acm@conduzo.com.br', 'moro aqui...')
teste.DeletePessoa('555')
#teste.AlteraFornecedor('35.822.063/0001-60', 'Bombonier', 'ACM Fornec 68', '35.822.063/0001-60','(21)98855-9999', 'Bombonier')
#teste.ListaFornecedor()
#teste.LisVendaPeriodo("10/03/2024", "12/03/2024")'

