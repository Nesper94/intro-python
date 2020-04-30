#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mercurio.py
#
#  Copyright 2019 Juan C. Arboleda R. <electrolisis10@gmail.com>

'''
Funciones relacionadas con cálculos para la construcción de un barómetro de mercurio.
¡Así como el que usaba Humboldt!
'''

import math # Importamos el módulo math para usar funciones matemáticas

def mercurio(d,h,vxg=400):
	'''
	Calcula el precio del mercurio necesario para un barómetro con el radio y la altura especificados.
	
	d:	Diámetro de la columna barométrica en mm.
	h:	Altura de la columna barométrica en mm.
	vxg:	Valor en COP de un gramo de mercurio.
	'''
	r = d/2							# Definimos el radio como la mitad del diámetro.
	vol = math.pi*(r**2)*h			# Calculamos el volumen de un cilindro.
	gramosHg = vol*13.6				# Multiplicamos volumen por densidad para obtener masa.
	valor = gramosHg*vxg			# Multiplicamos masa por valor por gramo.
	print('$',int(valor),sep='')	# Imprimimos el resultado.

def radiobar(v,h=90,vxg=400):
	'''
	Calcula el radio de un barómetro usando solo el valor de mercurio especificado.
	
	v:	Valor del mercurio necesario.
	h:	Altura de la columna de mercurio en mm.
	vxg:	Valor en COP de un gramo de mercurio.
	'''

	r = math.sqrt(v/(13.6*h*math.pi*vxg))
	print(r*10,'mm')

print('Se importó el MÓDULO')
