# -*- coding: utf-8 -*-
"""
Gráfica de Hypocycloid

Tema: Gráficas de funciones Paramétricas 

curso: MCA2

Autor: Roberto Méndez
Created  3 Mayo 2026
editado 10 Mayo 2026
"""

from sympy import symbols, cos, sin, pi
from sympy import plot_parametric

t = symbols('t')
def x(t):
  return (cos(t))**3
def y(t):
  return (sin(t))**3

plot_parametric(x(t), y(t), (t, 0, 2*pi), title= " Hypocycloid ", xlabel="x",
                ylabel="y")
