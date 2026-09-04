class NumeroModular:
    """Implementa as operações fundamentais em espaços modulares."""
    
    def __init__(self, num: int, mod: int):
        self.num_mod = num % mod
        self.num = num
        self.mod = mod

class OperacoesModulares:
    """Implementa operações modulares básicas: soma, subtração e multiplicação."""
    
    @staticmethod
    def somar(a: NumeroModular, b: NumeroModular) -> int:
    
        if (a.mod != b.mod) :
            raise ValueError("Os módulos devem ser iguais para a operação.")
    
        """Realiza a soma modular: (a + b) mod m"""
        return (a.num_mod + b.num_mod) % a.mod

    @staticmethod
    def subtrair(a: NumeroModular, b: NumeroModular) -> int:
    
        if (a.mod != b.mod) :
            raise ValueError("Os módulos devem ser iguais para a operação.")
    
        """Realiza a subtração modular: (a - b) mod m"""
        return (a.num_mod - b.num_mod) % a.mod

    @staticmethod
    def multiplicar(a: NumeroModular, b: NumeroModular) -> int:
    
        if (a.mod != b.mod) :
            raise ValueError("Os módulos devem ser iguais para a operação.")
    
        """Realiza a multiplicação modular: (a * b) mod m"""
        return (a.num_mod * b.num_mod) % a.mod

