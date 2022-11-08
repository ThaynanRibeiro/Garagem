from time import sleep
def exibir_menu():
    print('''\033[1m\033[33mEscolha uma opção:\033[0;0m

    [1] Cadastrar um veículo
    [2] Listar veículos cadastrados
    [3] Procurar dados de um veículo
    [4] Finalizar programa
    ''')

def cadastrar(veículos):
    marca = input('Marca? ')
    nome = input('Nome? ')
    placa = input('Placa? ')
    quilometragem = leiaInt('Quilometragem? ')
    veículos.append((marca, nome, placa, quilometragem))

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        quilometragem = str(input(msg))
        if quilometragem.isnumeric():
            valor = int(quilometragem)
            ok = True
        else:
            print('\033[0;31mDigite um número inteiro válido!\033[m')
        if ok:
            break
    return valor

def listar(veículos):
    for veículo in veículos:
        marca, nome, placa, quilometragem = veículo
        print(f'Nome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}')

def buscar(veículos):
    marca_desejada = input('Marca? ')
    for veículo in veículos:
        marca, nome, placa, quilometragem = veículo
        if marca == marca_desejada:
          print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
        else:
            print(f'Veículo com marca {marca_desejada} não encontrada')
            break
    nome_desejado = input('Nome? ')
    for veículo in veículos:
        marca, nome, placa, quilometragem = veículo
        if nome == nome_desejado:
          print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
        else:
            print(f'Veículo com nome {nome_desejado} não encontrado')
            break
    quilometragem_desejada = input('Quilometragem? ')
    for veículo in veículos:
      marca, nome, placa, quilometragem = veículo
      if quilometragem == quilometragem_desejada:
        print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
      else:
        print(f'Veículo com quilometragem {quilometragem_desejada} não encontrado')
        break
    placa_desejada = input('Placa? ')
    for veículo in veículos:
        marca, nome, placa, quilometragem = veículo
        if placa == placa_desejada: 
          print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
        else:
            print(f'Veículo com placa {placa_desejada} não encontrado')
            break

def main():
    veículos = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(veículos)
            sleep(1)
        elif opcao == 2:
            listar(veículos)
            sleep(1)
        elif opcao == 3:
            buscar(veículos)
            sleep(1)
        elif opcao == 4:
            print('\n\033[0;31mPrograma Finalizado!\033[m\n\n\n') 
            sleep(1)
            exit()
        else:
            print('\033[0;31mDigite uma opção válida!\033[m')
            sleep(1)
main()
