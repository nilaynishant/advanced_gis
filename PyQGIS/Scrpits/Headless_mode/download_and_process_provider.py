"""
Model exported as python.
Name : Downloading_and_processing
Group : 
With QGIS : 32207
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSink
from qgis.core import QgsProcessingParameterFileDestination
import processing


class Downloading_and_processing(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('inputlayer', 'Input layer', defaultValue=None))
        self.addParameter(QgsProcessingParameterFeatureSink('Output', 'Output', type=QgsProcessing.TypeVectorAnyGeometry, createByDefault=True, defaultValue=None))
        self.addParameter(QgsProcessingParameterFileDestination('Output', 'output', fileFilter='PNG format (*.png *.PNG);;BMP format (*.bmp *.BMP);;CUR format (*.cur *.CUR);;HEIC format (*.heic *.HEIC);;HEIF format (*.heif *.HEIF);;ICNS format (*.icns *.ICNS);;ICO format (*.ico *.ICO);;JP2 format (*.jp2 *.JP2);;JPEG format (*.jpeg *.JPEG);;JPG format (*.jpg *.JPG);;PBM format (*.pbm *.PBM);;PGM format (*.pgm *.PGM);;PPM format (*.ppm *.PPM);;TIF format (*.tif *.TIF);;TIFF format (*.tiff *.TIFF);;WBMP format (*.wbmp *.WBMP);;WEBP format (*.webp *.WEBP);;XBM format (*.xbm *.XBM);;XPM format (*.xpm *.XPM)', createByDefault=True, defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(3, model_feedback)
        results = {}
        outputs = {}

        # Download file
        alg_params = {
            'DATA': '',
            'METHOD': 0,  # GET
            'OUTPUT': '/Users/nilay/Downloads/latest.zip',
            'URL': 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/shapes/zips/MODIS_C6_1_SouthEast_Asia_7d.zip'
        }
        outputs['DownloadFile'] = processing.run('native:filedownloader', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Extract by location
        alg_params = {
            'INPUT': '/vsizip//Users/nilay/Downloads/latest.zip',
            'INTERSECT': parameters['inputlayer'],
            'PREDICATE': [0],  # intersect
            'OUTPUT': parameters['Output']
        }
        outputs['ExtractByLocation'] = processing.run('native:extractbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Output'] = outputs['ExtractByLocation']['OUTPUT']

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Export print layout as image
        alg_params = {
            'ANTIALIAS': True,
            'DPI': None,
            'GEOREFERENCE': True,
            'INCLUDE_METADATA': True,
            'LAYERS': [outputs['ExtractByLocation']['OUTPUT'],'IndiaBoundary_4154bf02_d819_4ee6_bd23_30f649d5df7a'],
            'LAYOUT': 'print',
            'OUTPUT': parameters['Output']
        }
        outputs['ExportPrintLayoutAsImage'] = processing.run('native:printlayouttoimage', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        results['Output'] = outputs['ExportPrintLayoutAsImage']['OUTPUT']
        return results

    def name(self):
        return 'Downloading_and_processing'

    def displayName(self):
        return 'Downloading_and_processing'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return Downloading_and_processing()
