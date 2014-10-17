import click
import os
archivo=click.prompt('Ingrese nombre del archivo que quiere buscar: ')

def decorador(fn):
	def envolvedor(*args):
		print "Iniciando busqueda de archivo....\n"
		fn(*args)
		print "\nFin del programa"
	return envolvedor

@decorador	
def existe_archivo(archivo):
	if os.path.exists(archivo):
		print "Si existe\n"
		opcion=click.prompt('Desea A) Escribir en el archivo B) Leer el archivo')
		if (opcion=='A' or opcion=='a'):
			escritura=click.prompt("Coloque lo que quiere escribir en el archivo")
			f=open(archivo, 'a+')
			f.write(escritura)
			f.close()
			print "Se ha modificado el archivo" 
			
		elif (opcion=='B' or opcion=='b'):
			print "\nMostrando lo que hay en el archivo...\n"
			f=open(archivo)
			for linea in f:	
				print linea
			f.close()

	else:
		print "El archivo no existe"
		respuesta=click.prompt('\nDesea crear un archivo con ese nombre? (s/n): ')
		if (respuesta=="S" or respuesta=="s"):	
			print "\nCreando un archivo con ese nombre..."
			f=open(archivo, 'a+')
			f.close()

if __name__== '__main__':
	existe_archivo(archivo)
	
