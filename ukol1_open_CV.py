"""Cvičení 1 - Zvýraznění okrajů ROI
Načtěte obrázek a najděte si v něm souřadnice, kde se zhruba nachází něco, co vás zajímá (například obličej).
Napište kód, kterým tento region zvýrazníte tak, že okraje tohoto ROI budou sytě zeleně obarveny."
K vykresleni si muzete pomoct metodou cv2.rectangle."""

# Import potřebných knihoven
import cv2

# Načtení obrázku
img = cv2.imread("Mona_Lisa.jpg")

# Výřez regionu zájmu (ROI) - souřadnice x, y, šířka, výška
x, y, w, h = 360, 200, 250, 360

# Použití cv2.rectangle pro vykreslení obdélníku kolem ROI
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Vykreslení regionu zájmu (ROI) na obrázku
cv2.imshow("ROI", img)
cv2.waitKey(0)
cv2.destroyAllWindows()