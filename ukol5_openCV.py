"""Cvičení 5 - Morfologické operace
Proveďte v openCV následující morfologické operace nad binarizovaným obrázkem a zobrazte si výsledky. Morfologické operace:

Eroze - zvolte počet iterací 5
Dilatace - zvolte počet iterací 5
Otevření (eroze pak dilatace) - zvolte počet iterací 1
Uzavření (dilatace pak eroze) - zvolte počet iterací 2
Erozi a dilataci proveďte na obrázku tetris2.png.
Otevření a uzavření proveďte na obrázku otiskprstu.png."""

# Nastavení matplotlib backendu, který nepotřebuje GUI
import matplotlib
matplotlib.use('Agg')  # 👈 BEZ GUI

# Import potřebných knihoven
import cv2
import matplotlib.pyplot as plt

# Načtení obrázku
img_tetris = cv2.imread("tetris_blocks.png")
img_finger = cv2.imread("finger.png")


# Eroze
eroded = cv2.erode(img_tetris, None, iterations=5)

# Převedení na odstíny šedi
gray = cv2.cvtColor(eroded, cv2.COLOR_BGR2GRAY)

# Binarizace
_, binary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

# Vykreslení výsledku
plt.figure(figsize=(6, 4))
plt.imshow(binary, cmap="gray")
plt.title("Eroze")
plt.axis("off")
plt.tight_layout()
plt.savefig("vystup_erode.png")
print("Výstupní obrázek uložen jako vystup_erode.png")


# Dilatace
dilated = cv2.dilate(img_tetris, None, iterations=5)

# Převedení na odstíny šedi
gray = cv2.cvtColor(dilated, cv2.COLOR_BGR2GRAY)

# Binarizace
_, binary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

# Vykreslení výsledku
plt.figure(figsize=(6, 4))
plt.imshow(binary, cmap="gray")
plt.title("Dilatace")
plt.axis("off")
plt.tight_layout()
plt.savefig("vystup_dilate.png")
print("Výstupní obrázek uložen jako vystup_dilate.png")


# Otevření (eroze pak dilatace)
opened = cv2.morphologyEx(img_finger, cv2.MORPH_OPEN, None, iterations=1)

# Převedení na odstíny šedi
gray = cv2.cvtColor(opened, cv2.COLOR_BGR2GRAY)

# Binarizace
_, binary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

# Vykreslení výsledku
plt.figure(figsize=(6, 4))
plt.imshow(binary, cmap="gray")
plt.title("Otevření")
plt.axis("off")
plt.tight_layout()
plt.savefig("vystup_open.png")
print("Výstupní obrázek uložen jako vystup_open.png")


# Uzavření (dilatace pak eroze)
closed = cv2.morphologyEx(img_finger, cv2.MORPH_CLOSE, None, iterations=2)


# Převedení na odstíny šedi
gray = cv2.cvtColor(closed, cv2.COLOR_BGR2GRAY)

# Binarizace
_, binary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

# Vykreslení výsledku
plt.figure(figsize=(6, 4))

plt.imshow(binary, cmap="gray")
plt.title("Uzavření")
plt.axis("off")
plt.tight_layout()
plt.savefig("vystup_close.png")
print("Výstupní obrázek uložen jako vystup_close.png")


