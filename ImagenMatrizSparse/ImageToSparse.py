# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 23:05:40 2024

@author: fredd
"""

from PIL import Image
import numpy as np
from scipy.sparse import csr_matrix


image01 = Image.open('HM_Terrain_01.png')
image02 = Image.open('HM_Terrain_02.png') 

grayImage01 = image01.convert('L')
grayImage02 = image02.convert('L')

image01Array=np.array(grayImage01)
image02Array=np.array(grayImage02)

sparseMatrixImage01 = csr_matrix(image01Array)
sparseMatrixImage02 = csr_matrix(image02Array)

print(sparseMatrixImage01)
print(sparseMatrixImage02)
