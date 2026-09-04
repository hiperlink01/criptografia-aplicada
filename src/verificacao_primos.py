import random

class VerificaPrimos:
    """Implementa métodos para verificação e geração de números primos."""
    
    @staticmethod
    def simples(n: int) -> bool:
        """
        Verificação determinística (Divisão por tentativa).
        Recomendado apenas para fins didáticos e números pequenos.
        """
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def miller_rabin(n: int, k: int = 40) -> bool:
        """
        Verificação probabilística de Miller-Rabin.
        Padrão da indústria para chaves criptográficas reais.
        
        Args:
            n: Número a ser testado.
            k: Número de rodadas de teste (40 garante margem de erro desprezível).
        """

        if n == 2 or n == 3: return True
        if n <= 1 or n % 2 == 0: return False

        # Fatora n - 1 na forma d * 2^r
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2

        # Executa k rodadas de teste
        for _ in range(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            
            if x == 1 or x == n - 1:
                continue
                
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                # Se não quebrou o loop interno, é composto
                return False
                
        return True