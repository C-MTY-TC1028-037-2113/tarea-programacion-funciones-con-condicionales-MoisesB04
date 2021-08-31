def calcula_grado(grado):
    if grado < 0.0 or grado > 1.0: # Valores no válidos
        nota = "score incorrecto"
    elif grado > 0.9: # Valores con nota A
        nota = "A"
    elif grado > 0.8: # Valores con nota B
        nota = "B"
    elif grado > 0.7: # Valores con nota C
        nota = "C"
    elif grado > 0.6: # Valores con nota D
        nota = "D"
    else: # El resto de los valores con nota F
        nota = "F" 
    return nota


def main():
    #escribe tu código abajo de esta línea 
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
