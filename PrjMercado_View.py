### INTERFACE GRAFICA

from PrjMercado_Controller import PessoaController
from PrjMercado_Dao import PessoaDao

while True:
    decisao = int(input(' 1-Cadastrar\n 2-Consultar\n 3-Encerrar:\n'))

    if decisao == 3:
        break

    if decisao == 1:
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        cpf = input('Digite o cpf: ')

        if PessoaController.Cadastrar(nome, idade, cpf):
            print('Cadastro efetuado com sucesso')
        else:
            print('Dados Inválidos...')

    if decisao == 2:
        print(PessoaDal.ler())


