"""Cvičení 5 - Spočítejte počet mincí, které se nacházejí v následujícím obrázku
Existuje několik variant jak problém řešit:

Binarizovat obrázek, oddělit od sebe objekty a spočítat počet hranic (kontur)
Využít zaplavovací algoritmus Watershed, který spočíta počet vrcholů v propojených v objektech záplavou prostoru
využít nacvičení vyhledávač
Návod na variantu 1:

Binarizujte obrázek a ponechte mince bílé
Odstraňte šum (například operací uzavření)
Odtrhněte mince od sebe (operace eroze)
Spočítejte počet kontur funkcí cv2.findCountours
Spočítejte velikost seznamu nalezených kontur"""

import matplotlib
matplotlib.use('Agg')

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Načtení a převod na šedotónový
img = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Otsu binarizace s inverzí – mince bílé
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morfologické otevření – odstraní šum
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# Určení jistého pozadí
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Distance transform → určí „vrchol“ každé mince
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.5 * dist_transform.max(), 255, 0)

# Zóna neznámého (hranice mezi mincemi)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Označíme komponenty
_, markers = cv2.connectedComponents(sure_fg)

# Zvýšíme indexy, aby pozadí mělo 1 místo 0
markers = markers + 1
markers[unknown == 255] = 0

# Watershed algoritmus
img_ws = img.copy()
markers = cv2.watershed(img_ws, markers)

# Hranice (rozhraní mezi mincemi) budou -1
img_ws[markers == -1] = [255, 0, 0]

# Mince = unikátní čísla větší než 1
unique_labels = np.unique(markers)
coin_labels = [label for label in unique_labels if label > 1]
print("Počet mincí (watershed):", len(coin_labels))

# Vykreslení + číslování
output = img.copy()
for label in coin_labels:
    mask = np.uint8(markers == label)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        cnt = contours[0]
        cv2.drawContours(output, [cnt], -1, (255, 0, 0), 2)
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.putText(output, str(label - 1), (cx - 10, cy + 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Uložení
plt.figure(figsize=(9, 9))
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title(f"Detekováno {len(coin_labels)} mincí (watershed)")
plt.axis("off")
plt.tight_layout()
plt.savefig("vystup_watershed_final.png")
print("Výstup uložen jako vystup_watershed_final.png")
