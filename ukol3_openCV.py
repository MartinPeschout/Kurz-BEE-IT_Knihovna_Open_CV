"""Cvičení 3 - Binarizace Tetris kostiček
Spusťte skript v první buňce, který stáhne obrázek Tetris kostiček. 
Napište program, který binarizuje obrázek tetris kostiček.
Doporučuji si obrázek převést do odstínů šedi, vykreslit histogram a podle něj se rozhodnout o vhodné práhové hodnotě
a to takové, aby kostičky byly bílé a pozadí černé."""

# Nastavení matplotlib backendu, který nepotřebuje GUI
import matplotlib
matplotlib.use('Agg')  # musí být PŘED importem pyplot

# Import potřebných knihoven
import cv2
import matplotlib.pyplot as plt

# Načtení obrázku
img = cv2.imread("tetris.jpg")

# Převedení obrázku do odstínů šedi
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Histogram intenzit
plt.figure(figsize=(6, 4))
plt.hist(gray.ravel(), 256)
plt.title("Histogram")
plt.xlabel("Hodnota pixelu")
plt.ylabel("Počet pixelů")
plt.tight_layout()
plt.savefig("histogram.png")  # místo plt.show()
print("Histogram uložen jako histogram.png")

# Binarizace obrázku podle vhodného thresholdu (např. 75)
_, binary = cv2.threshold(gray,75, 255, cv2.THRESH_BINARY)

# Vykreslení originálu a binarizovaného obrázku
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # převod na RGB pro správné zobrazení
plt.title("Původní obrázek")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(binary, cmap="gray")
plt.title("Binarizovaný obrázek")
plt.axis("off")

plt.tight_layout()
plt.savefig("vystup_binarizace.png")  # místo plt.show()
print("Výstupní obrázky uloženy jako vystup.png")