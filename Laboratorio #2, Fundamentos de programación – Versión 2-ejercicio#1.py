# comentario de entrada
infracciones = int(input("ingresa la cantidad de infraciones en el mes: "))

infracciones_diarias = infracciones / 30

inf_matutinas = infracciones_diarias * 0.20
inf_vespertino = infracciones_diarias * 0.35
inf_nocturnas = infracciones_diarias * 0.45
# aqui se imprimira el total de multas 
print("el promedio diario matutino de infraciones es de:", inf_matutinas)
print("el promedio diario vespertino de infraciones es de:", inf_vespertino)
print("el promedio diario nocturnas de infraciones es de:", inf_nocturnas)