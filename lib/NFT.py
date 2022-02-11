
from random import Random, random
from lib.Metadata import Metadata
from lib.utils.System import System
import lib.constants as static
import math
from PIL import Image

class NFT():
    def __init__(self, id, layers, categories, generation_order):
        self.layers = layers
        self.categories = categories
        self.layout = self.__generate_layout(self.layers, self.categories)
        self.rarity = self.__calculate_rarity_from_layout()
        self.base = "Bird.png"
        self.id = id
        self.dna = ""
        self.imgs = []
        self.generation_order = generation_order
        self.metadata = Metadata()

    def __generate_layout(self, layers, categories):
        ret = dict.fromkeys(categories)
        layer = 0
        for key in ret:
            ret[key] = layers[layer]
            layer += 1
        
        return ret

    def __calculate_rarity_from_layout(self):
        rarity = 0
        for category in self.layout:
            rarity += System.get_rarity_from_file(self.layout[category])
        return math.floor(rarity / 5)

    def generate_image(self):
        base_img = self.imgs[0]
        for layer in self.imgs[1:]:
            base_img.paste(layer, (0,0), layer)
        filename = static.NFT_OUTPUT_DIR + self.id + ".png"
        base_img.save(filename, "PNG")
        self.__tag_img(filename)
        del self.imgs

    def __tag_img(self, filename):
        img = open(filename, "rb+")
        fileData = img.read()
        data = []
        for char in fileData:
            data.append(char)
        for char in static.TAG:
            data.append(char)
        img.seek(0)
        img.write(bytes(data))
        img.close()
        del(data)
        del(img)

    def generate_metadata(self):
        self.metadata.name = static.COLLECTION_NAME + " #" + self.id
        self.metadata.description = "Think of something funny"
        self.metadata.symbol = static.SYMBOL
        self.metadata.image = self.id + ".png"
        self.metadata.append_attribute(self.layout)
        self.metadata.append_attribute({"rarity": static.RARITY[self.rarity]})
        self.metadata.generate(self.id)

    def __get_layer_uri(self, category, layer):
        return static.BASE_LAYERS_DIR + category + "/" + layer

    def __get_base_uri(self):
        return System.get_base_file(self.base)

    def populate_imgs(self):
        for i in range(len(self.generation_order)):
            if self.generation_order[i] == 'base':
                self.imgs.append(Image.open(self.__get_base_uri()))
            else:
                self.imgs.append(Image.open(self.__get_layer_uri(self.categories[self.categories.index(self.generation_order[i])], self.layers[self.categories.index(self.generation_order[i])])))
