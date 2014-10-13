class auto():
	gasolina=0
	"""Abstracion a objeto de un auto, e
	sta clase va a arrancar segun su nivel de gasolina"""
	def __init__(self,gasolina):
		slef.gasolina= gasolina
		print "tenemos", gasolina, "Litros"
	@staticmethod
	def arrancar (gasolina):
		if gasolina >0:
			print  "arranca"
		else:
			 print "NO arranca"
			 
	@staticmethod		 
	def conducir(gasolina):
		
	#while(self.gasolina>0):
		while gasolina>0:
			print "Quedan", gasolina, "Litros"
			gasolina -=1
		else:
			print "El auto no se mueve"
			

