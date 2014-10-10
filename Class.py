class auto:
	"""Abstracion a objeto de un auto, e
	sta clase va a arrancar segun su nivel de gasolina"""
	def __init__(self, gasolina):
		self.gasolina= gasolina
		print "tenemos", gasolina, "Litros"

	def arrancar (self):
		if self.gasolina >0:
			print  "arranca"
		else:
			 print "NO arranca"
	def conducir(self):
		
	#while(self.gasolina>0):
		while self.gasolina>0:
			print "Quedan", self.gasolina, "Litros"
			self.gasolina -=1
		else:
			print "El auto no se mueve"


x=auto(10)
x.arrancar()
x.conducir()

#####

print x.gasolina


