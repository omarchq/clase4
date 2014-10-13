class clase(object):
	 no_instansiada=0
    def __init__ (self):
	   clase.no_instansiada=no_instansiada + 1
    @classmethod
	  def tomar_instancia (cls_obj):
	    return cls_obj.no_instansiada


