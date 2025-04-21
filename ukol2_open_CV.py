"""Cvičení 2 - Datová augmentace
Všechny následující úkony proveďte jedním programem v pythonu.

Vytvořte adresář rotace pokud neexistuje
Načtěte obrázek do pythonu
Napište cyklus, kterým zrotujte obrázek vždy o 10 stupňů a takto upravený obrázek uložte do složky rotace
Program skončí, jakmile byl obrázek zrotován o celých 360 stupňů"""


# Import potřebných knihoven
import cv2
import os
from os import path
import numpy as np

# Adresář pro uložení obrázků
adresar = 'rotace'
if not path.exists(adresar):
    os.makedirs(adresar)

# Načtení obrázku
img = cv2.imread("Mona_Lisa.jpg")

# Získání středu obrázku pro rotaci
(h, w) = img.shape[:2]
stred = (w // 2, h // 2)

# Rotace po 10 stupních
for uhel in range(0, 361, 10):
    # Vytvoření rotační matice
    matice = cv2.getRotationMatrix2D(stred, uhel, 1.0)
    # Aplikace rotace na obrázek
    rotace = cv2.warpAffine(img, matice, (w, h))

    # Uložení a zobrazení
    cv2.imwrite(f"{adresar}/rotace_{uhel}.jpg", rotace)
    cv2.imshow("Rotace", rotace)
    cv2.waitKey(100)  # Zobraz každou rotaci krátce
    cv2.destroyAllWindows()