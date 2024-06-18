# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 00:39:00 2024

@author: fredd
"""

#Usando Multiprocessing

import multiprocessing as mp
from PIL import Image
import numpy as np
from scipy.sparse import csr_matrix

def partMatrixMultiplication(A_data, A_indices, A_indptr, B_data, B_indices, B_indptr, rows, shape):
    m, p = shape
    C_data = []
    C_indices = []
    C_indptr = [0]

    for i in rows:
        row_start_A = A_indptr[i]
        row_end_A = A_indptr[i + 1]

        C_row = {}
        for idx_A in range(row_start_A, row_end_A):
            col_A = A_indices[idx_A]
            val_A = A_data[idx_A]

            row_start_B = B_indptr[col_A]
            row_end_B = B_indptr[col_A + 1]

            for idx_B in range(row_start_B, row_end_B):
                col_B = B_indices[idx_B]
                val_B = B_data[idx_B]

                if col_B in C_row:
                    C_row[col_B] += val_A * val_B
                else:
                    C_row[col_B] = val_A * val_B

        C_data.extend(C_row.values())
        C_indices.extend(C_row.keys())
        C_indptr.append(len(C_data))

    return (C_data, C_indices, C_indptr)

def sparseMatrixMultiplicationParallel(A, B, num_processes=None):
    if A.shape[1] != B.shape[0]:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")

    if not isinstance(A, csr_matrix):
        A = csr_matrix(A)
    if not isinstance(B, csr_matrix):
        B = csr_matrix(B)

    A = A.astype(np.float64)
    B = B.astype(np.float64)

    m, _ = A.shape
    _, p = B.shape

    if num_processes is None:
        num_processes = mp.cpu_count()

    chunk_size = m // num_processes
    chunks = [range(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)]

    if m % num_processes != 0:
        chunks[-1] = range((num_processes - 1) * chunk_size, m)

    pool = mp.Pool(processes=num_processes)
    results = pool.starmap(partMatrixMultiplication, [(A.data, A.indices, A.indptr, B.data, B.indices, B.indptr, chunk, (m, p)) for chunk in chunks])
    pool.close()
    pool.join()

    C_data = []
    C_indices = []
    C_indptr = [0]

    for data, indices, indptr in results:
        C_data.extend(data)
        C_indices.extend(indices)
        C_indptr.extend([x + C_indptr[-1] for x in indptr[1:]])

    return csr_matrix((C_data, C_indices, C_indptr), shape=(m, p))


if __name__ == "__main__":
    print("\nMULTIPROCESSING\n")
    
    image01 = Image.open('HM_Terrain_01.png')
    image02 = Image.open('HM_Terrain_02.png') 

    grayImage01 = image01.convert('L')
    grayImage02 = image02.convert('L')

    image01Array=np.array(grayImage01)
    image02Array=np.array(grayImage02)

    sparseMatrixImage01 = csr_matrix(image01Array)
    sparseMatrixImage02 = csr_matrix(image02Array)
    sparseMatrixImageResultMULTIPROCESSING = sparseMatrixMultiplicationParallel(sparseMatrixImage01, sparseMatrixImage02)

    print("Matriz A:\n", sparseMatrixImage01.toarray())
    print("Matriz B:\n", sparseMatrixImage02.toarray())
    print("Matriz C (resultado de A * B):\n", sparseMatrixImageResultMULTIPROCESSING.toarray())