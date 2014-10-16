import click

@click.command()
@click.option('--contar', defaul=1, help=u"Numero de saludos")

@click.option('--nombre', prompt='Tu nombre', help='la persona a saludar')

def hello(contar, nombre):
	for x in range(contar):
		click.echo('hola %s!' %nombre)

if ___name__=='__main__':
	hello()