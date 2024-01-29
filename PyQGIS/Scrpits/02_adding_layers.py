import os
data_dir = 'z:\\PyQGIS_Masterclass\data'

filename = 'dem.tif'
srtm = os.path.join(data_dir, filename)
iface.addRasterLayer(srtm, 'srtm dem', 'gdal')

results = processing.runAndLoadResults("native:hillshade", 
    {'INPUT': srtm, 
    'Z_FACTOR':2,
    'AZIMUTH':300,
    'V_ANGLE':40,
    'OUTPUT': 'TEMPORARY_OUTPUT'})


filename = 'SK_state_boundary.shp'
uri = os.path.join(data_dir, filename)
iface.addVectorLayer(uri, 'state boundary', 'ogr')



