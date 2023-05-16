"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "sami_"
__version__ = "2022.06.29"

import rhinoscriptsyntax as rs
import math

path = []
nbPoints = nbPointsInLayer 
radius = initialRadius

vectors = []
for j in range(0, nbLayers):
    for i in range(0, nbPoints):
        angle = 360/nbPoints
        path.append(rs.CreatePoint(position.X + radius*math.cos(i*angle*math.pi/180), position.Y + radius*math.sin(i*angle*math.pi/180), position.Z+layerHeight*j))
   
