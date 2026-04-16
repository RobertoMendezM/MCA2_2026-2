# -*- coding: utf-8 -*-
"""
Resolución de un sistema ecuaciones lineal

            Ax = b
 
de la forma:
            
        6*x + 4*y + 13*z = -23
        2*x + y   -    z =   4
       -3*x + 6*y -    z =   8     

con dos esquemas:
        a.- Numérico:  numpy.linalg.solve
        b.- Simbólico: sympy.solve  
        
Curso:  MCA 2  2026-2     
        Notas Clase  12 Abril 2026       
         
Tema 1.7: Sistemas de Ecuaciones lineales         

@author: roberto Méndez Méndez
Creación: Mon Apr 13 08:34:44 2026
Edición:  16 Abril 2026
"""

import numpy as np

# Define la matriz de coeficientes (A) y el vector de resultados (b)
A = np.array([[6, 4, 13], [2, 1, -1], [-3, 6, - 1]])
b = np.array([-23, 4, 8])

# Solve the system
x = np.linalg.solve(A, b)
print(x) 


import sympy as sp

# 1. Define symbols
x, y, z = sp.symbols('x y z')

# 2. Define equations
eq1 = sp.Eq(6*x + 4*y + 13*z, -23)
eq2 = sp.Eq(2*x + y - z, 4)
eq3 = sp.Eq(-3*x + 6*y - z, 8)

# 3. Solve the system
solution = sp.solve((eq1, eq2, eq3), (x, y, z))

print(solution)
