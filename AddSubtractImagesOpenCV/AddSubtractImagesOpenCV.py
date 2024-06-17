# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:03:10 2024

@author: fredd
"""

import cv2

image1 = cv2.imread('HM_Terrain_01.jpg')
image2 = cv2.imread('HM_Terrain_02.jpg')

addImages = cv2.add(image1,image2)
cv2.imshow('Add Images',addImages)

subtractImages = cv2.subtract(image1,image2)
cv2.imshow('Subtract Images', subtractImages)

cv2.waitKey(0)
cv2.destroyAllWindows()
