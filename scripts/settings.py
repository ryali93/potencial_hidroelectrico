import sys, os, arcpy
import pandas as pd

__author__ = 'Roy Marco Yali Samaniego, Leonardo Castillo Navarro'
__copyright__ = 'IMEFEN 2020'
__credits__ = ['Roy Yali S.', 'Leonardo Castillo N.']
__version__ = '1.0'
__maintainer__ = ['Roy Yali S.', 'Leonardo Castillo N.']
__mail__ = ['ryali93@gmail.com', 'leonardocastillo@uni.edu.pe']
__status__ = 'Production'

arcpy.env.overwriteOutput = True
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(32718)

ID_EVAL = "ID_EVAL"
TIPO = "TIPO"

# Folders
BASE_DIR = r'E:\2020\uni'
PROCESS_DIR = os.path.join(BASE_DIR, sys.argv[1])
# PROCESS_DIR = os.path.join(BASE_DIR, "process_ch_max")

path_cuenca = "{}".format(sys.argv[2])
# path_cuenca = "{}".format(1)

print "Corriendo la cuenca : {}".format(path_cuenca)
RASTER_DIR = os.path.join(PROCESS_DIR, path_cuenca)
SHP_DIR = os.path.join(PROCESS_DIR, path_cuenca, "shp")
XLS_DIR = os.path.join(PROCESS_DIR, path_cuenca, "xls")
