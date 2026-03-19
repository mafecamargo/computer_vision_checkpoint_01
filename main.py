# Este é o arquivo principal da aplicação -> entry point
# Para excutar as funções definidas no outro arquivo, precisamos importar os recursos

from leitura_conversao import(
    carryImage,
    greyConverter,
    histogram,
    showImage,
    ajusteBrilhoContraste,
    equalizar_histograma,
    calcular_metricas,
    applyThreshold,
    applyOtsu,
    applyMorphology,
    findContour,
    drawContour,
    drawLimitingBoxes,
    filterContour
)

if __name__ =='__main__':
    # carregar imagem
    img = carryImage('image.jpg')
    print("Shape imagem colorida: ", img.shape)

    # converter a imagem em cinza
    grey = greyConverter(img)
    print('Shape imagem escala de cinza: ', grey.shape)

    showImage(grey, 'Imagem Original(GREY)')
    histogram(grey)

    brilho, contraste = calcular_metricas(grey)

    print('\n ------ METRICAS ORIGINAIS ------')
    print('Brilho Médio: ', brilho)
    print('Contraste (obtido a partir do desvio padrão): ', contraste)

    # ajuste de brilho e contraste
    ajuste = ajusteBrilhoContraste(grey, alpha=1.2, beta=30)

    showImage(ajuste, 'Brilho e contraste ajustados')
    histogram(ajuste)

    brilho_aj, contraste_aj = calcular_metricas(ajuste)
    print('\n ------ METRICAS APOS O AJUSTE ------')
    print('Brilho Médio: ', brilho_aj)
    print('Contraste (obtido a partir do desvio padrão): ', contraste_aj)

    # equalizando o histograma
    equalizar = equalizar_histograma(ajuste)
    
    showImage(equalizar, 'Imagem equalizada - a partir do brilho e contraste')
    histogram(equalizar)

    brilho_eq, contraste_eq = calcular_metricas(equalizar)
    print('\n ------ METRICAS APOS EQUALIZACAO  ------')
    print('Brilho Médio: ', brilho_eq)
    print('Contraste (obtido a partir do desvio padrão): ', contraste_eq)

    # threshold manual
    img_thr_manual = applyThreshold(grey)
    showImage(img_thr_manual, "Threshold Manual")
    histogram(img_thr_manual)
   
    # threshold Otsu 
    img_thr_otsu = applyOtsu(grey)
    showImage(img_thr_otsu, "Threshold Otsu")
    histogram(img_thr_otsu)

    # morfologia
    img_limpa = applyMorphology(img_thr_otsu)
    showImage(img_limpa, "Imagem Após Morfologia")
    histogram(img_limpa)

    # detecção de Contornos
    contornos = findContour(img_limpa)
    print("Quantidade de objetos detectados:", len(contornos))

    # desenho dos Contornos
    img_contornos = drawContour(img, contornos)
    showImage(img_contornos, "Contornos Detectados")

    # desenho de bounding boxes
    img_caixas = drawLimitingBoxes(img, contornos)
    showImage(img_caixas, "Bounding Boxes")

    # filtro por Área
    contornos_filtrados = filterContour(contornos, minimumarea=500)
    print("Quantidade de objetos detectados (filtrados):", len(contornos_filtrados))

    img_contornos_bonus = drawContour(img, contornos_filtrados)
    showImage(img_contornos_bonus, "Contornos Filtrados")

    img_caixas_bonus = drawLimitingBoxes(img, contornos_filtrados)
    showImage(img_caixas_bonus, "Bounding Boxes Filtrados")
