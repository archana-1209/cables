from data import ROW_Dict,cable,COL_Dict	
length=10
customerkwpreqirement=110
structure="with structure"
structure1="without structure"
typeofroof="RCC"

typeofROOFstructure1="newballast"

dataloggeritips=['radiationsensor']

def findcables(request,length,wp,structure,typeofroof,typeofroofstructure,dataloggeritips):

        cabledc=cable[ROW_Dict[wp]][COL_Dict[length]]
        dcacloading=0.85#fetch from MMSY18
        max_dc=50.8#fetch from MMSY19
        if customerkwpreqirement>max_dc:
        	response={'error':'inverter undersize MAX DC allowed','value':max_dc,'dcac':dcacloading}
        	return response
        elif dcacloading<0.78:
        	response={'error':'inverter overrated decrease inverter size','dcac':dcacloading}
            return response
        else:
        	response={'dcac':dcacloading}
        	return response
def bom(request,length,wp,structure,typeofroof,typeofroofstructure,dataloggeritips):
	






