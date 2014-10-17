mport click
import os
archivo=click.prompt('Ingrese nombre del archivo que quiere buscar: ')
def decorador(fn):
	def envolvedor(*args):
		print "Iniciando Programa de busqueda de archivos\n"
		fn(*args)
		print "Fin del programa"
	return envolvedor

@decorador	
def existe_archivo(archivo):
	if os.path.exists(archivo):
		print "Si existe"
		opcion=click.prompt('Desea A) Escribir en el archivo B) Leer el archivo')
		if (opcion=='A' or opcion=='a'):
			escritura=click.prompt("Coloque lo que quiere escribir en el archivo")
			f=open(archivo, 'a+')
			f.write(escritura)
			f.close()
			print "Es ha modificado el archivo" 
			
		elif (opcion=='B' or opcion=='b'):
			f=open(archivo)
			for linea in f:	
				print linea
			f.close()

	else:
		print "El archivo no existe"
		respuesta=click.prompt('Desea crear un archivo con ese nombre? (s/n): ')
		if (respuesta=="si"):	
			print "Creando un archivo en ese nombre..."
			f=open(archivo, 'a+')
			f.close()

if __name__== '__main__':
	existe_archivo(archivo)
