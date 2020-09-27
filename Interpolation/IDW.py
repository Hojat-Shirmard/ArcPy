#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Name: IDW_3d_Ex_02.py
# Description: Interpolate a series of point features onto a
#    rectangular raster using Inverse Distance Weighting (IDW).
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outRaster = "C:/output/idwout01"
cellSize = 2000.0
power = 2
searchRadius = 150000

# Check out the ArcGIS 3D Analyst extension license
arcpy.CheckOutExtension("3D")

# Execute IDW
arcpy.Idw_3d(inPointFeatures, zField, outRaster, cellSize, 
             power, searchRadius)

