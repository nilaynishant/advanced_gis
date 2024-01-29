from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', referenced_columns=[])
def unique(value1, feature, parent):
    li = list(value1.split(","))
    list_set = set(li)
    unique_list = (list(list_set))
    
    return unique_list[0]