
print("\n-------------Alalizador lexico-------------\n")
file=open('read.jf')
a=file.read()


date_type={"int":"tipo integer",
           "char":"tipo caracter",
           "float":"tipo flotante",
           "long":"long int"
}
date_type_keys=date_type.keys()

simbolo_puntuacion={':':"dos puntos",
                    ".":"punto",
                    ";":"punto y coma",
                    ",":"coma"
}

simbolo_puntuacion_keys=simbolo_puntuacion.keys()





identificador={"x":"id",
               "y":"id",
               "z":"id",
               "f":"id"
}
identificador_keys=identificador.keys()



operadores={
    "+":"op suma",
    "-":"op resta",
    "=":"op asignacion"
}
operadores_keys=operadores.keys()

print("------Codigo------")
print(a)
print("------------------\n")

program=a.split("\n")
#print(program)

c=1
for line in program:
    print("-------------------------Linea#",c,"-------------------------")
    print(line)
    print("----Propiedades----")
    c+=1

    tokens=line.split(" ")
    #print(tokens)

    for token in tokens:
        if token in date_type_keys:
            print(token," el tipo de dato es: ",date_type[token])

        if token in simbolo_puntuacion_keys:
            print(token," el simpolo de puntuacion es: ",simbolo_puntuacion[token])

        if token in identificador_keys:
            print(token," identidicador: ",identificador[token])

        if token in operadores_keys:
            print("El operador es: ",operadores[token])

    print("------------------------------------------------------------\n")