# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:58:03 2024

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


def multiplicacionMatrizSparse(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")

    if not isinstance(A, csr_matrix):
        A = csr_matrix(A)
    if not isinstance(B, csr_matrix):
        B = csr_matrix(B)

    A = A.astype(np.float64)
    B = B.astype(np.float64)

    m, n = A.shape
    n, p = B.shape

    # Inicializar la matriz resultante
    C_data = []
    C_indices = []
    C_indptr = [0]

    # Realizar la multiplicación
    for i in range(m):
        print(i)
        row_start_A = A.indptr[i]
        row_end_A = A.indptr[i+1]

        C_row = {}
        for idx_A in range(row_start_A, row_end_A):
            col_A = A.indices[idx_A]
            val_A = A.data[idx_A]

            row_start_B = B.indptr[col_A]
            row_end_B = B.indptr[col_A+1]

            for idx_B in range(row_start_B, row_end_B):
                col_B = B.indices[idx_B]
                val_B = B.data[idx_B]

                if col_B in C_row:
                    C_row[col_B] += val_A * val_B
                else:
                    C_row[col_B] = val_A * val_B

        C_data.extend(C_row.values())
        C_indices.extend(C_row.keys())
        C_indptr.append(len(C_data))

    return csr_matrix((C_data, C_indices, C_indptr), shape=(m, p))



imageMultiplied = multiplicacionMatrizSparse(sparseMatrixImage01, sparseMatrixImage02)

imageResulDense = imageMultiplied.toarray();

print("Matriz A:\n", sparseMatrixImage01.toarray())
print("Matriz B:\n", sparseMatrixImage02.toarray())
print("Matriz C (resultado de A * B):\n", imageResulDense)


