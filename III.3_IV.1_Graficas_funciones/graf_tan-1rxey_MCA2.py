# -*- coding: utf-8 -*-
"""
Gráfica de 

                   f(x,y) = arcTan(√x / y)

Tema: Gráficas de funciones escalares de n variables

curso: MCA2


Autor:   Deepseek
Editor:  Roberto Méndez
Created  3 Mayo 2026
Editado 10 Mayo 2026
"""


import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x, y):
    """
    Calcula f(x,y) = arctan(√x / y) para y < 0 y x ≥ 0
    """
    # Crear máscara para valores válidos
    mascara_valida = (x >= 0) & (y < 0)
    
    # Inicializar resultado con NaN para valores fuera del dominio
    resultado = np.full_like(x, np.nan, dtype=float)
    
    # Calcular solo para valores válidos
    if np.any(mascara_valida):
        x_valid = x[mascara_valida]
        y_valid = y[mascara_valida]
        
        # Calcular √x / y (y siempre es negativo)
        argumento = np.sqrt(x_valid) / y_valid
        
        # Calcular arctan
        resultado[mascara_valida] = np.arctan(argumento)
    
    return resultado

# Crear malla de puntos
x = np.linspace(0, 100, 500)  # x ≥ 0 (evitamos exactamente 0 por la raíz)
y = np.linspace(-10, -0.01, 500)  # y < 0 (excluimos y=0)

X, Y = np.meshgrid(x, y)

# Calcular valores de la función
Z = f(X, Y)

# Crear figura con subplots
fig = plt.figure(figsize=(15, 5))

# 1. Gráfico 3D de superficie
ax1 = fig.add_subplot(131, projection='3d')
surf = ax1.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.8, 
                        linewidth=0, antialiased=True)
ax1.set_xlabel('x (x ≥ 0)', fontsize=10)
ax1.set_ylabel('y (y < 0)', fontsize=10)
ax1.set_zlabel('f(x,y)', fontsize=10)
ax1.set_title('Superficie 3D de f(x,y) = arctan(√x / y)', fontsize=12)
ax1.set_zlim(-np.pi/2, 0)  # arctan da valores negativos cuando y<0
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=5, label='f(x,y)')