# CheckPoint 01:
- João Pedro Borsato da Cruz - 559402
- Maria Fernanda Vieira de Camargo - 97956

-----
## Pipeline do nosso projeto:
O nosso projeto manipula a imagem fazendo as seguintes coisas:
1. Mudamos a escala da imagem original (image.jpg) para cinza
2. Ajustamos o brilho e o contraste
3. Calculamos as suas métricas
4. Aplicamos os Thresholds manual e pelo Otsu (que realiza de forma automática)
5. Aplicamos também uma operação morfológica
6. Detectamos, encontramos e desenhamos o contorno da imagem
7. Desenhamos caixas que delimitam a área mínima da imagem
8. Aplicamos depois uma função de filtro para área mínima para o uso dos contornos

-----
### Para que a aplicação funcione da forma correta, precisamos nos certificar que:
1. A biblioteca do matplotlib está instalado -> _pip install matplotlib_
2. A biblioteca do OpenCV está instalado - _pip install opencv-python_
3. Entramos no arquivo _main.py_ para rodar o código
