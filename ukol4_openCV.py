"""Cvičení 4 - Nalezení hran Tetris kostiček
Spusťte skript v první buňce, který stáhne obrázek Tetris kostiček.
Napište program, který najde hrany těchto kostiček a zobrazí obrázek s vyznačenými hranami.
Doporučuji si napřed převést obrázek do černobílého."""

# Nastavení matplotlib backendu, který nepotřebuje GUI
import matplotlib
matplotlib.use('Agg')  # musí být PŘED importem pyplot

# Import potřebných knihoven
import cv2
import matplotlib.pyplot as plt

# Načtení obrázku
img = cv2.imread("tetris.jpg")

# Převedení obrázku na černobílý
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarizace obrázku podle vhodného thresholdu (např. 75)
_, binary = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)

# Nalezení hran pomocí Cannyho detektoru
edges = cv2.Canny(binary, 100, 200)

# Vykreslení hran   
plt.figure(figsize=(6, 4))
plt.imshow(edges, cmap="gray")  # převod na RGB pro správné zobrazení
plt.title("Nalezené hrany")
plt.axis("off") 

plt.tight_layout()  
plt.savefig("vystup_hrany.png")  # místo plt.show()
print("Výstupní obrázky uloženy jako vystup.png")