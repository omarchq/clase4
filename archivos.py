

def decorador(fn):
	def envoltorio():
		print"Abriendo archivo...."
		print " "
		fn()
		print "Archivo cerrado"


	return envoltorio




@decorador
def leer():

	f=open("archivo.txt")
	for linea in f:
		print linea
	f.close()


leer()
