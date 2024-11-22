medida = float(input("Informe a medida em metros: "))
unidade = input("Informe a unidade a ser convertida: ")
resultado = 0

match unidade:
    case 'cm':
        print(f"{medida}m é equivalente cm²:{medida*100}")
    case 'mm':
        print(f"{medida}m é equivalente mm²:{medida*1000}")
    case 'km':
        print(f"{medida}m é equivalente km²:{medida/1000}")
    case _:
        print("Informe uma unidade de medida válida.")