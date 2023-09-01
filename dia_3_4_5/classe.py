from abc import ABC, abstractmethod

class IAnimal(ABC):

    @abstractmethod
    def falar(self):
        """Defina na classe filha"""
    
    def andar(self):
        """Defina na classe filha"""

class Cachorro(IAnimal):

    def falar(self):
        print("Au Au Au")
    
    def andar(self):
        print("Ando com 4 patas.")

class Pessoas:
    def _init_(self, nome, idade):
        self._nome = nome
        self.idade = idade
        self._humano = True

        print("Falando")
    
pingo = Cachorro()
pingo.falar = falar()
pingo.andar = andar()

