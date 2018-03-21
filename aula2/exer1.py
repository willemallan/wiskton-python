# nome utilizamos caracteres ex: número e letras
nome = input("Digite o nome: ")
# nota usamos float pois possuem . ex: 9.5
nota1 = float(input("Digite sua nota1: "))
nota2 = float(input("Digite sua nota2: "))
media = (nota1+nota2)/2
idade = 29
# idade podemos usar apenas números inteiros

if media >= 6:
	# print("Parabéns você passou! Sua nota final foi %s" % media)
	print("Olá {0}! Sua nota final foi {1}! Parabéns você passou!".format(nome, media))
	fwefwe
else:
print("Reprovado!")