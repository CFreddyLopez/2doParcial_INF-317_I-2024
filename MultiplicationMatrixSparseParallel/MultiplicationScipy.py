# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:34:01 2024

@author: fredd
"""


#Usando scipy 

print("SCIPY")

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

sparseMatrixImageResultSCIPY = sparseMatrixImage01.dot(sparseMatrixImage02)

print("Matriz A:\n", sparseMatrixImage01.toarray())
print("Matriz B:\n", sparseMatrixImage02.toarray())
print("Matriz C (resultado de A * B):\n", sparseMatrixImageResultSCIPY.toarray())


