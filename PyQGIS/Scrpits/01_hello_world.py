from qgis.core import QgsDistanceArea

new_delhi = (28.6139, 77.2090)
kolkata = (22.5726, 88.3639)

d = QgsDistanceArea()
d.setEllipsoid('WGS84')


lat1, lon1 = new_delhi
lat2, lon2 = kolkata
# Remember the order is X,Y
point1 = QgsPointXY(lon1, lat1)
point2 = QgsPointXY(lon2, lat2)

distance = d.measureLine([point1, point2])
print(distance/1000)
