from qgis.core import *
import utm
from PyQt5.QtCore import QVariant
import processing


def select_area(import_tif_path, output_shape_path, coordinates, grid_width, grid_height):
    

    raster_layer = QgsRasterLayer(import_tif_path, "TIFF_File")
    QgsProject.instance().addMapLayer(raster_layer)

    latitude = coordinates[0][0]
    longitude = coordinates[0][1]
    utm_coords = utm.from_latlon(latitude, longitude)
    epsg_code = f"EPSG:{326 if latitude >= 0 else 327}{utm_coords[2]}"
    QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(epsg_code))


    utm_points = [QgsPointXY(*utm.from_latlon(lat, lon)[:2]) for lat, lon in coordinates]
    layer = QgsVectorLayer(f"Polygon?crs={epsg_code}", "Polygon", "memory")
    dp = layer.dataProvider()
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPolygonXY([utm_points]))
    dp.addFeature(feature)
    QgsVectorFileWriter.writeAsVectorFormat(layer, output_shape_path, "UTF-8", layer.crs(), "ESRI Shapefile")
    QgsProject.instance().addMapLayer(layer)



    extent = layer.extent()
    width, height = grid_width, grid_height 
    grid_layer = QgsVectorLayer(f"Polygon?crs={epsg_code}", "Grid", "memory")
    grid_layer = QgsVectorLayer(f"Polygon?crs={layer.crs().authid()}", "GridLayer", "memory")
    dp = grid_layer.dataProvider()


    fields = QgsFields()
    fields.append(QgsField('id', QVariant.Int))
    dp.addAttributes(fields)
    grid_layer.updateFields()


    cols = int((extent.xMaximum() - extent.xMinimum()) / width)
    rows = int((extent.yMaximum() - extent.yMinimum()) / height)
    id_counter = 0
    for col in range(cols):
        x = extent.xMinimum() + col * width
        for row in range(rows):
            y = extent.yMaximum() - row * height - height
            vertices = [QgsPointXY(x, y), QgsPointXY(x + width, y), QgsPointXY(x + width, y + height), QgsPointXY(x, y + height)]
            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPolygonXY([vertices]))
            feature.setAttributes([id_counter])
            dp.addFeature(feature)
            id_counter += 1

    QgsProject.instance().addMapLayer(grid_layer)




def segment_all(output_folder): 
    
    project = QgsProject.instance()
    raster_layer = project.mapLayersByName('TIFF_File')[0]
    vector_layer = project.mapLayersByName('GridLayer')[0]

    for feature in vector_layer.getFeatures():
        plot_id = feature["id"]
        output_path = f'{output_folder}clip_{plot_id}.tif'
        
        params = {
            'INPUT': raster_layer, 
            'MASK': QgsProcessingFeatureSourceDefinition(
                vector_layer.id(), selectedFeaturesOnly=True, featureLimit=-1,
                geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),
            'SOURCE_CRS': raster_layer.crs(),
            'TARGET_CRS': raster_layer.crs(),
            'NODATA': None,
            'ALPHA_BAND': False,
            'CROP_TO_CUTLINE': True,
            'KEEP_RESOLUTION': True,
            'OUTPUT': output_path
        }
        vector_layer.selectByIds([feature.id()])
        processing.run("gdal:cliprasterbymasklayer", params)
        vector_layer.removeSelection()
        
        print(f"Plot {plot_id} clipped")










select_area('C:/Users/ft7b6/Downloads/sample.tif', 'C:/Users/ft7b6/Documents/polygon.shp', [(52.21365, 4.38088), (52.22465, 4.38088)], 2, 2)

segment_all("C:/Users/ft7b6/Downloads/")

