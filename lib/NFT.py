from typing_extensions import Concatenate
from lib.utils.System import System
import lib.constants as static
from PIL import Image

class NFT():
    def __init__(self, id, layers, categories, generation_order):
        self.layers = layers
        self.categories = categories
        self.layout = self.generate_layout(self.layers, self.categories)
        self.rarity = 0
        self.base = "Bird.png"
        self.id = id
        self.dna = ""
        self.meta_data = ""
        self.imgs = []
        self.generation_order = generation_order

    def generate_layout(self, layers, categories):
        ret = dict.fromkeys(categories)
        layer = 0
        for key in ret:
            ret[key] = layers[layer]
            layer += 1
        
        return ret

    def generate_image(self):
        
        base_img = self.imgs[0]
        for layer in self.imgs[1:]:
            base_img.paste(layer, (0,0), layer)
        
        base_img.save(static.NFT_OUTPUT_DIR + self.id + ".png", "PNG")
        del self.imgs

    def get_layer_uri(self, category, layer):
        return static.BASE_LAYERS_DIR + category + "/" + layer

    def get_base_uri(self):
        return System.get_base_file(self.base)

    def populate_imgs(self):
        for i in range(len(self.generation_order)):
            if self.generation_order[i] == 'base':
                self.imgs.append(Image.open(self.get_base_uri()))
            else:
                self.imgs.append(Image.open(self.get_layer_uri(self.categories[self.categories.index(self.generation_order[i])], self.layers[self.categories.index(self.generation_order[i])])))

