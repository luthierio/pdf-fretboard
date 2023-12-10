# Copyright (c) 2023 Simon Daron
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


from reportlab.pdfgen import canvas
from math import pow
import sys
import os 

def calculate_fret_position(scale_length, fret_number):
    return scale_length - (scale_length / pow(2, fret_number / 12))

def mm_to_points(mm):
    # Conversion de millimètres à points (1 point ≈ 0.352778 mm)
    return mm / 0.352778

def draw_fretboard(pdf_file, num_frets, scale_length, width, nut_width, line_width, font_size):
    # Dimensions du PDF en millimètres
    pdf_width_mm = scale_length + nut_width
    pdf_height_mm = width

    # Conversion des dimensions en points
    pdf_width = mm_to_points(pdf_width_mm)
    pdf_height = mm_to_points(pdf_height_mm)

    # Création d'un objet Canvas pour dessiner sur le PDF
    c = canvas.Canvas(pdf_file, pagesize=(pdf_width, pdf_height))
    c.setAuthor("Simon Daron @ La Fabrique du Silence")
    c.setTitle("Fretboard: "+str(scale_length)+"mm")
    # Position initiale du diapason
    nut_position_mm = nut_width
    nut_position = mm_to_points(nut_position_mm)

    # Définir la taille de la ligne
    c.setLineWidth(line_width)

    # Définir la taille de police du texte
    c.setFont("Helvetica", mm_to_points(font_size))

    # Dessiner la frette 0
    c.line(nut_position, pdf_height, nut_position, 0)

    # Dessiner les frettes, leurs numéros et les distances
    for fret in range(0, num_frets + 1):
        fret_position_mm = calculate_fret_position(scale_length, fret) 
        fret_position = mm_to_points(fret_position_mm+nut_position_mm)
        distance_to_nut = fret_position
        c.line(fret_position, pdf_height, fret_position, 0)

        # Dessiner le numéro de la frette de bas en haut
        c.saveState()
        c.rotate(90)
        c.drawCentredString(3 * pdf_height / 4, -fret_position + mm_to_points(1), str(fret))

        # Afficher la distance entre la frette X et la frette 0 depuis le bord du dessin
        c.drawCentredString(pdf_height / 4, -fret_position + mm_to_points(1), f"{fret_position_mm:.2f}")
        c.restoreState()

    # Dessiner le diapason
    c.line(nut_position, pdf_height / 2, fret_position, pdf_height / 2)

    # Enregistrez le fichier PDF
    c.save()
    print(f"Diapason imprimé: {scale_length}")

# Script principal
if __name__ == "__main__":


    num_frets = 24
    scale_length = 650
    
    if len(sys.argv) == 2:
        scale_length = float(sys.argv[1])
        
    elif len(sys.argv) == 3:
        scale_length = float(sys.argv[1])
        num_frets = int(sys.argv[2])
    else:
        print("Usage: python fretboard.py [<scale_length> <num_frets>]")
        sys.exit(1)

    # checking if the directory build
    # exist or not. 
    if not os.path.exists("dist"):           
        os.makedirs("dist") 
        
    width = 80
    nut_width = 10
    line_width = 0.5
    font_size = 5
    pdf_filename = f"dist/{scale_length}mm_{num_frets}.pdf"
    
    draw_fretboard(pdf_filename, num_frets, scale_length, width, nut_width, line_width, font_size)

