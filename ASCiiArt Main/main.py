import os
import Shit

if __name__ == '__main__':
    os.system("clear")
    #data_file = Shit.image_to_ascii('TestGraph.png', width_factor=0.8, height_factor=0.8)
    data_file = Shit.image_to_asciiColorful('TestGraph.png', width_factor=0.21, height_factor=0.608)
    #Shit.ascii_to_image(data_file, 'reconstructed_image.png')