# -*- coding: utf-8 -*-
import arcpy
import os

class Toolbox(object):
    def __init__(self):
        self.label = "Lab5 Toolbox"
        self.alias = ""
        self.tools = [BuildingProximity]


class BuildingProximity(object):
    def __init__(self):
        self.label = "Building Proximity"
        self.description = "Determine which buildings are near garages"
        self.canRunInBackground = False

    def getParameterInfo(self):

        param0 = arcpy.Parameter(
            displayName="Output GDB Folder",
            name="gdbFolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )

        param1 = arcpy.Parameter(
            displayName="Output GDB Name",
            name="gdbName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="garageCSV",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )

        param3 = arcpy.Parameter(
            displayName="Garage Layer Name",
            name="garageLayerName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param4 = arcpy.Parameter(
            displayName="Campus GDB",
            name="campusGDB",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input"
        )

        param5 = arcpy.Parameter(
            displayName="Buffer Distance (Meters)",
            name="bufferDistance",
            datatype="GPLong",
            parameterType="Required",
            direction="Input"
        )

        return [param0, param1, param2, param3, param4, param5]

    def execute(self, parameters, messages):

        folder_path = parameters[0].valueAsText
        gdb_name = parameters[1].valueAsText
        csv_path = parameters[2].valueAsText
        garage_layer_name = parameters[3].valueAsText
        campus_gdb = parameters[4].valueAsText
        buffer_distance = int(parameters[5].value)

        gdb_path = os.path.join(folder_path, gdb_name)

        # Create GDB
        arcpy.management.CreateFileGDB(folder_path, gdb_name)

        # Create garage points
        garages_layer = arcpy.management.MakeXYEventLayer(
            csv_path, "X", "Y", garage_layer_name
        )

        arcpy.management.CopyFeatures(
            garages_layer,
            os.path.join(gdb_path, garage_layer_name)
        )

        # Copy structures
        arcpy.management.CopyFeatures(
            os.path.join(campus_gdb, "Structures"),
            os.path.join(gdb_path, "Buildings")
        )

        # Project garages to match buildings
        spatial_ref = arcpy.Describe(
            os.path.join(gdb_path, "Buildings")
        ).spatialReference

        arcpy.management.Project(
            os.path.join(gdb_path, garage_layer_name),
            os.path.join(gdb_path, "Garage_Points_projected"),
            spatial_ref
        )

        # Buffer
        arcpy.analysis.Buffer(
            os.path.join(gdb_path, "Garage_Points_projected"),
            os.path.join(gdb_path, "Garage_Buffer"),
            buffer_distance
        )

        # Intersect
        arcpy.analysis.Intersect(
            [
                os.path.join(gdb_path, "Garage_Buffer"),
                os.path.join(gdb_path, "Buildings")
            ],
            os.path.join(gdb_path, "Garage_Building_Intersection")
        )

        arcpy.AddMessage("Tool executed successfully.")
