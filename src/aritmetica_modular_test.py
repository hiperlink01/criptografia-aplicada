from aritmetica_modular import NumeroModular as nMod, OperacoesModulares as opMod

mod = 7

a = nMod(5, mod)
b = nMod(3, mod)

soma = opMod.somar(a, b)
print(f"A soma modular em {mod} de {a.num_mod} e {b.num_mod} é: {soma}")  # Saída: A soma modular de 5 e 3 é: 1

sub = opMod.subtrair(a, b)
print(f"A subtração modular em {mod} de {a.num_mod} e {b.num_mod} é: {sub}")  # Saída: A subtração modular de 5 e 3 é: 2

mul = opMod.multiplicar(a, b)
print(f"A multiplicação modular em {mod} de {a.num_mod} e {b.num_mod} é: {mul}")  # Saída: A multiplicação modular de 5 e 3 é: 1

div = opMod.dividir(a, b)
print(f"A divisão modular em {mod} de {a.num_mod} e {b.num_mod} é: {div}")  # Saída: A divisão modular de 5 e 3 é: 1
