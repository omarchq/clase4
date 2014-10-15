import os
archivo="creando.txt"
def decorador(fn):
	def envoltorio():
		print"Abriendo archivo...."
		print " "
		fn()
		print "Archivo cerrado"


	return envoltorio

@decorador
def leer():
	x=15 + 23
	f=open("archivo.txt", 'a+')
	
	
	f.write("Hola como estas?\n")
	f.write("Todo bien y tu?\n")
	f.write("Todo bien\n")
	f.write(str(x))

	#print f.readline()
	#for linea in f:	
	#	print linea
	f.close()

def existe_archivo(archivo):
	if os.path.exists(archivo):
		print "Si existe"
	else:
		print "No puede encontrarlo"
		print "Creando un archivo en ese nombre."
		f=open("creando.txt", 'a+')
		f.write("Hola\n")
		f.close()

#leer()
existe_archivo(archivo)





	
		