# -*- coding: utf-8 -*-
"""
Gráfica de "Espiral cónica"

Tema: Gráficas de funciones Paramétricas 

curso: MCA2

Autor: Gemini IA
Editor: Roberto Méndez
Creado   6 Mayo 2026
editado 10 Mayo 2026
"""

import matplotlib.pyplot as plt
import numpy as np

# 1. Definir el parámetro t
t = np.linspace(0, 20, 100) # 100 puntos entre 0 y 20

# 2. Definir las ecuaciones paramétricas
x = t*np.cos(t)
y = t
z = t*np.sin(t)

# 3. Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 4. Graficar la curva
ax.plot(x, y, z, label='Espiral cónica')

# 5. Personalizar el gráfico
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Gráfica Parametrizada en 3D')
ax.legend()

# 6. Mostrar el gráfico
plt.show()
