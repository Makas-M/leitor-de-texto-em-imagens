import pytesseract
import cv2

# ler a imagem
imagem = cv2.imread("imagem2.png")
# extrair o texto
caminho = r"C:\Users\Macaringue\AppData\Local\Programs\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem)

print(texto)