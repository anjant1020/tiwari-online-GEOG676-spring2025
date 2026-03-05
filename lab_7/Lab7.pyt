import arcpy
import os

# ===============================
# SET PATHS
# ===============================

base_path = r"D:\anjan\GISPROGRAMMING\Lab 7"
landsat_path = os.path.join(base_path, "landsat4")
dem_path = os.path.join(base_path, "dem")

arcpy.env.workspace = base_path
arcpy.env.overwriteOutput = True

# Check out extensions
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")

# ===============================
# COMPOSITE (Natural Color)
# ===============================

red = arcpy.sa.Raster(os.path.join(landsat_path, "red.tif"))
green = arcpy.sa.Raster(os.path.join(landsat_path, "green.tif"))
blue = arcpy.sa.Raster(os.path.join(landsat_path, "blue.tif"))
nir = arcpy.sa.Raster(os.path.join(landsat_path, "nir08.tif"))

output_composite = os.path.join(base_path, "composite_4band.tif")

arcpy.management.CompositeBands(
    [red, green, blue, nir],
    output_composite
)

print("Composite created.")

# ===============================
# HILLSHADE
# ===============================

dem_file = os.path.join(dem_path, "dem_30m.tif")
output_hillshade = os.path.join(base_path, "hillshade.tif")

arcpy.ddd.HillShade(
    dem_file,
    output_hillshade,
    315,
    45,
    "NO_SHADOWS",
    1
)

print("Hillshade created.")

# ===============================
# SLOPE
# ===============================

output_slope = os.path.join(base_path, "slope_degree.tif")

arcpy.ddd.Slope(
    dem_file,
    output_slope,
    "DEGREE",
    1
)

print("Slope created.")

print("All processing complete!")