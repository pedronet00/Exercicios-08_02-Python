lista_tuplas = []
for i in range(4):
    val1 = int(input(f"Digite o primeiro valor da {i+1}ª tupla: "))
    val2 = int(input(f"Digite o segundo valor da {i+1}ª tupla: "))
    val3 = int(input(f"Digite o terceiro valor da {i+1}ª tupla: "))
    lista_tuplas.append((val1, val2, val3))

lista_tuplas_sem_repeticao = [tupla for tupla in lista_tuplas if len(set(tupla)) > 1]

print(lista_tuplas_sem_repeticao)