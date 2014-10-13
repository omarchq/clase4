class auto():
	gasolina=0
	"""Abstracion a objeto de un auto, e
	sta clase va a arrancar segun su nivel de gasolina"""
	def __init__(self,gasolina):
		auto.gasolina= gasolina
		print "tenemos", gasolina, "Litros"
	@classmethod
	def arrancar (cls,gasolina):
		if gasolina >0:
			print  "arranca"
		else:
			 print "NO arranca"
			 
	@classmethod		 
	def conducir(cls,gasolina):
		
	#while(self.gasolina>0):
		while gasolina>0:
			print "Quedan", gasolina, "Litros"
			gasolina -=1
		else:
			print "El auto no se mueve"
			





"""x=auto(10) 
x.arrancar()
x.conducir()"""