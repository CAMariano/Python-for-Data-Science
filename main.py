import numpy as np
import matplotlib.pyplot as plt
import imageio

from skimage import data

# importação de bibliotecas 'científicas'

photo_data = imageio.imread('./gearbox_thermographic.png')  # leitura de imagens pelos pixels

# print(photo_data.shape)
# print(photo_data)

# O formato de ndarray mostra uma matriz de três camadas.
# Os primeiros dois conjuntos de números representam o comprimento e a largura, respectivamente,
# e o terceiro número é para  R (0), G (1), B(2).

#  print(photo_data.size)  # Tamanho do vetor nd_array
#  print(photo_data.min(), photo_data.max())  #  Valor máximo e mínimo dos vetores, no caso valores RGB
#  print(photo_data.mean())  # Média dos valores dos pixels

#  Pixel on the 150th Row and 250th Column
#  print(photo_data[150, 250, 1])

#  Modificar o pixel da imagem, impossível ver
#  photo_data[150, 250] = 0
#  plt.figure(figsize=(10, 10))
#  plt.imshow(photo_data)
#  plt.show()

#  Modificar um intervalo (range) de pixels
#  photo_data = imageio.imread('./wifire/sd-3layers.jpg')
#  photo_data[200:800, :] = 255
#  plt.figure(figsize= (10, 10))
#  plt.imshow(photo_data)
#  plt.show()


# RED MASK, BLUE MASK, GREEN MASK - Filtro de acordo com as cores do padrão RGB

# Verifica se o valor de R (0 - Padrão RGB) no pixel é menor que 200, indicando um vermelho menos intenso.
red_mask = photo_data[:, :, 0] < 200
# blue_mask = photo_data[:,:,2] <150
# green_mask = photo_data[:,:,1] <150

# print(red_mask)

photo_data[red_mask] = 0  # Atribui o preto para estes valores
# photo_data[blue_mask] = 0
# photo_data[green_mask] = 0

# COMBINED MASKS

# red_mask = photo_data[:, :, 0] < 150
# green_mask = photo_data[:, :, 1] > 100
# blue_mask = photo_data[:, :, 2] < 100

# final_mask = np.logical_and(red_mask, green_mask, blue_mask)
# photo_data[final_mask] = 0

plt.figure(figsize=(15, 15))
plt.imshow(photo_data)
plt.show()
