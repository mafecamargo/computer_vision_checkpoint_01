import cv2
import matplotlib.pyplot as plt 


#=========== bloco de funções para manipular a imagem

def carryImage(path):
    image = cv2.imread(path) # aqui estamos lendo a imagem
    ''' uma imagem é um tensor, seja ela colorida ou preta e branca '''
    if image is None:
        raise ValueError('Image not found!')
    return image

#==========================
# Conversor de cinza
#==========================

def greyConverter(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#==========================
# Definir a função do histograma
#==========================
def histogram(image):
    plt.hist(image.ravel(), bins=256, range=[0,256])
    plt.title("Intensity of the Histogram")
    plt.xlabel("Intensity")
    plt.ylabel("Quantity of pixels")
    plt.show()

#==========================
# Ajuste de brilho e contraste da imagem
#==========================
def ajusteBrilhoContraste(imagem, alpha=1.0, beta=0):
    return cv2.convertScaleAbs(imagem, alpha=alpha, beta=beta)

#==========================
# Equalização do histograma
#==========================
def equalizar_histograma(imagem):
    return cv2.equalizeHist(imagem)

#==========================
# Equalização do histograma
#==========================
def calcular_metricas(imagem):
    brilho = imagem.mean()
    contraste = imagem.std() # aqui a métrica será observada a partir do desvio padrão

    return brilho, contraste

#==========================
# Definir a função que exibe a imagem
#==========================
def showImage(image, title="Image"):
    plt.imshow(image, cmap='gray') 
    #imgshow() mostra a imagem
    #cmap = 'gray' indica que é escala de cinza
    plt.title(title)
    plt.axis("off")
    plt.show()

#==========================
# Aplicar threshold manual -> nosso limiar
#==========================

def applyThreshold(image, threshold=127):  
    _, imagem_binaria = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return imagem_binaria

#==========================
# Aplicar threshold Otsu automático
#==========================

def applyOtsu(image):
    _, binaryimage= cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binaryimage

#==========================
# Aplicar operação morfológica
#==========================

def applyMorphology(binaryimage):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    cleanimage = cv2.morphologyEx(binaryimage, cv2.MORPH_CLOSE, kernel)
    return cleanimage

#==========================
# Encontrar e detectar contornos externos
#==========================

def findContour(binaryimage):
    contour, _ = cv2.findContours(binaryimage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contour

#==========================
# Desenhar contornos na imagem
#==========================

def drawContour(image, contour):
    copiedimage = image.copy()
    cv2.drawContours(copiedimage, contour, -1, (0, 255, 0), 2)
    return copiedimage

#==========================
# Desenhar caixas que delimitam os contornos
#==========================

def drawLimitingBoxes(image, contour):
    copiedimage = image.copy()
    for contour in contour:
        x, y, l, a = cv2.boundingRect(contour)
        cv2.rectangle(copiedimage, (x, y), (x + l, y + a), (0, 255, 0), 2)
    return copiedimage

#==========================
# Função de filtro para área mínima de contornos
#==========================

def filterContour(contour, minimumarea=100):
    return [c for c in contour if cv2.contourArea(c) > minimumarea]

#==========================
# Função para usar no main
#==========================

if __name__ == "__main__":
    img = carryImage('image.jpg') 
    grey = greyConverter(img)
    showImage(grey, 'grey scale image')
    histogram(grey)


