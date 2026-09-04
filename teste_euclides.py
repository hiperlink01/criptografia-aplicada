from euclides_estendido import euclides_estendido, inverso_multiplicativo

mdc, x, y = euclides_estendido(7, 3)

print("MDC:", mdc)
print("x:", x)
print("y:", y)

inverso = inverso_multiplicativo(3, 7)

print("inverso multiplicativo:", inverso)

inverso = inverso_multiplicativo(6, 9)

print("inverso de 6 modulo 9:", inverso)