# -*- coding: utf-8 -*-
"""
Obtener la Matriz Diagonal D y el vector  L de la parte lineal 

            D = (P^T)*M*P       L =[4, 6]*P
    
de la transformada.   
    
Curso: MCA2 clases 23 y 25 marzo 2026. Notas 23 y 24 marzo 

Tema: Dada la Ec cuadrática (elipse)

              31x^2 - 24xy + 21y^2 + 4x + 6y = 25      
  
      y la matriz P de eigenvetores asociada a la matriz M de la parte
      cuadratica, obtener la matriz D= (P^T)*M*P  y  L = [4, 6]*P

         (z, w) (P^T)*M*P  (z)  + L (z)  = 25
                           (w)      (w) 
                           
      del sistema transformado.

                     
Referencias:
   
    - Roe (1993). Elementary Geometry, Oxford University Press p. 152


Software:
    Python 3.14.3
    IDE    Spyder 

@author:   Roberto Méndez Méndez
Creación:  23 marxo 2026
Editado:   9 abril 2026
"""

import numpy as np

P = np.array([[2,3], [3,-2]])
M= np.array([[31,-12], [-12,21]])

# Forma numpy 

D = P.T@M@P/13
print("La matriz diagonal es es: \n ", D)


d = np.array([4,6])
print("El vector para coordenadas x,y es: \n ", d@P)