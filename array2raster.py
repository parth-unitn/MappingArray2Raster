
## METHOD - 1 

import gdal, ogr, os, osr
import numpy as np


def array2raster(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array):

    cols = array.shape[1]
    rows = array.shape[0]
    originX = rasterOrigin[0]
    originY = rasterOrigin[1]

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Byte)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    outband = outRaster.GetRasterBand(1)
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference()
    outRasterSRS.ImportFromEPSG(__)
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()


def main(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array):
    reversed_arr = array[::-1] # reverse array so the tif looks like the array
    array2raster(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,reversed_arr) # convert array to raster


if __name__ == "__main__":
    rasterOrigin = (,)
    pixelWidth = 10
    pixelHeight = 10
    newRasterfn = 'test.tif'
    array = np.array()


    main(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array)

## METHOD - 2 

import rasterio as rio    

with rio.open('other_file.tif') as src:     ## Requires a slave raster to extract geometry and meta-data
    ras_data = src.read()
    ras_meta = src.profile

# make any necessary changes to raster properties:

ras_meta['dtype'] = "int32"
ras_meta['nodata'] = -99

with rio.open('outname.tif', 'w', **ras_meta) as dst:
    dst.write(numpy_array, 1)
