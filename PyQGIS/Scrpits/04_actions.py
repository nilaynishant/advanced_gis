from qgis.utils import iface

feature_id = [%$id%]
layer_id = '[%@layer_id%]'
field_name = 'Checked'

layer = QgsProject().instance().mapLayer(layer_id)
field = layer.fields().lookupField(field_name)

with edit(layer):
    layer.changeAttributeValue(feature_id, field, 'Y')
    iface.messageBar().pushInfo('Success', 'Field Value Updated')