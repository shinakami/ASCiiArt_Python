import cv2
import os
import numpy as np




# Resize Factor 
width_factor = 0.095
height_factor = 0.0421

def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


os.system('cls')
file_name = 'Image.png'  ### Input your Image
img = cv2.imread(file_name)
img = img[:,:,[2,1,0]]
re_width = int(img.shape[1] * width_factor)
re_height = int(img.shape[0] * height_factor)
img_re = cv2.resize(img, (re_width, re_height), interpolation=cv2.INTER_CUBIC)
gray_img = grayscale(img_re)
Li_index = gray_img/gray_img.max() * 10
Li_index = np.array(Li_index, dtype='int')
N_str = '@%$&^!+=-. '
output_file_path = 'output.txt'
with open(output_file_path, 'w') as file:
    for j in range(re_height):
        for i in range(re_width):
            num = Li_index[j, i]
            print(N_str[num], end='')
            file.write(N_str[num])
        print()
        file.write('\n')



os.system("pause")
