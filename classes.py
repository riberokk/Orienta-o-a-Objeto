import os

class Cachorro:
    def __init__(self, nome, raca, idade, nome_dono):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.nome_dono = nome_dono

    def getNome(self):
        return self.nome
    
    def getRaca(self):
        return self.raca
    
    def getIdade(self):
        return self.idade
    
    def getDono(self):
        return self.nome_dono
    
class Gato:
    def __init__(self, nome, raca, idade, nome_dono):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.nome_dono = nome_dono

    def getNome(self):
        return self.nome
    
    def getRaca(self):
        return self.raca
    
    def getIdade(self):
        return self.idade
    
    def getDono(self):
        return self.nome_dono
    
class Procedimento:
    def __init__(self, tipo, descricao, data, pet):
        self.tipo = tipo
        self.descricao = descricao
        self.data = data
        self.pet = pet

    def getTipo(self):
        return self.tipo

    def getDescricao(self):
        return self.descricao

    def getData(self):
        return self.data

    def getPet(self):
        return self.pet
    
