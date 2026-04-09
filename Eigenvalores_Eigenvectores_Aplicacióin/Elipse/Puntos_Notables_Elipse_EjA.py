# -*- coding: utf-8 -*-
"""
Obtener los pùntos notables de la elipse, centro y vertice
en su espacio original (rotado), usando la relación

       (x,  y)^T = P*(z, w)^T
       
donde el sistema coordenado (z, w) es en el que por una transformación
se elininó el término mixto 2Bxy       


Curso: MCA2 clases 23 y 25 marzo 2026. Notas 23 y 24 marzo

Tema: Ecuación cuadrática original (elipse)

              31x^2 - 24xy + 21y^2 + 4x + 6y = 25      
  
      transformada (rotada)
             
              z^2 + 2z/raiz(13) + 3w^2 = 25/13

Referencias:
    - https://docs.sympy.org/latest/modules/matrices/matrices.html
    - Roe (1993). Elementary Geometry, Oxford University Press p. 152


Software:
    Python 3.14.3
    IDE    Spyder
    
@author: Roberto Méndez / Web
Created  Sun 23 Marzo 2026
"""

import numpy as np


P = np.array([[2, 3], 
              [3, -2]]*1/np.sqrt(13))

# Centro C y un vértice de la transformada
C = np.array([-1/np.sqrt(13), 0])
V2 = np.array([(np.sqrt(26)-1)/np.sqrt(13), 0])

# Imprime el centro y un vértice de la elipse (ecuación) original
print("Centro rotado", np.dot(P, C))
print("Vertice 2 rotado", np.dot(P, V2))







