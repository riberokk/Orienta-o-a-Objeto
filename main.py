from classes import *
import os

lista_procedimentos = []
lista_cachorros = []
lista_gatos = []

def cadastrar_procedimento():
    os.system("cls")
    print("---- Cadastro de Procedimento ----")
    print()
    nome_pet = input("Nome do Pet:\n>> ")

    # Procurar o pet na lista de cachorros
    pet_encontrado = None
    for cachorro in lista_cachorros:
        if cachorro.getNome().lower() == nome_pet.lower():
            pet_encontrado = cachorro
            break

    # Procurar o pet na lista de gatos se não encontrado na lista de cachorros
    if not pet_encontrado:
        for gato in lista_gatos:
            if gato.getNome().lower() == nome_pet.lower():
                pet_encontrado = gato
                break

    if pet_encontrado:
        tipo = input("Tipo de Procedimento (Ex: Vacinação, Cirurgia):\n>> ")
        descricao = input("Descrição do Procedimento:\n>> ")
        data = input("Data do Procedimento (dd/mm/yyyy):\n>> ")
        procedimento = Procedimento(tipo, descricao, data, pet_encontrado)
        pet_encontrado.adicionarProcedimento(procedimento)
        lista_procedimentos.append(procedimento)
        print(f"Procedimento adicionado com sucesso para {pet_encontrado.getNome()}!")
    else:
        print("Pet não encontrado!")

while True:
    os.system("cls")
    print("---- SenaiVet ----")
    print()
    print("O que você gostaria de fazer? ")
    print()
    print("01 - Cadastrar PET")
    print("02 - Verificar Pacientes")
    print("03 - Criar Procedimento")
    escolha = input(">>> ")

    if escolha == "1":
        os.system("cls")
        print("Cadastro de PET")
        print()
        tipo = input("Tipo de Pet (Cachorro = 1 | Gato = 2)\n>> ")
        dono = input("Nome do Dono\n>> ")
        nome = input("Nome do Pet\n>> ")
        raca = input("Raça do Pet\n>> ")
        idade = input("Idade do Pet\n>> ")
        if tipo == "1":
            cachorro = Cachorro(nome, raca, idade, dono)
            lista_cachorros.append(cachorro)
        elif tipo == "2":
            gato = Gato(nome, raca, idade, dono)
            lista_gatos.append(gato)
        else:
            print("Tipo de Pet inválido!")

    elif escolha == "2":
        os.system("cls")
        print(f"---- Lista de Pacientes ----")
        print()
        print(f"----      Cachorros     ----")
        print()
        for cachorro in lista_cachorros:
            print(f"Nome do Dono: {cachorro.getDono()}")
            print(f"Nome do Cachorro: {cachorro.getNome()}")
            print(f"Raça: {cachorro.getRaca()}")
            print(f"Idade: {cachorro.getIdade()}")
            print()
            for procedimento in cachorro.listarProcedimentos():
                print(f"  - Tipo: {procedimento.getTipo()}, Data: {procedimento.getData()}, Descrição: {procedimento.getDescricao()}")
            print()
        print("----        Gatos       ----")
        print()
        for gato in lista_gatos:
            print(f"Nome do Dono: {gato.getDono()}")
            print(f"Nome do Gato: {gato.getNome()}")
            print(f"Raça: {gato.getRaca()}")
            print(f"Idade: {gato.getIdade()}")
            print()
            for procedimento in gato.listarProcedimentos():
                print(f"  - Tipo: {procedimento.getTipo()}, Data: {procedimento.getData()}, Descrição: {procedimento.getDescricao()}")
            print()
        os.system("pause")

    elif escolha == "3":
        cadastrar_procedimento()
    
    else:
        print("Opção Inválida. Tente novamente.")



