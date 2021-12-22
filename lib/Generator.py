from lib.utils.System import System
from lib.NFT import NFT
from lib.utils.Layers import Layers
from lib.utils.Menu import Menu
import math


class Generator():
    def __init__(self, total = Layers.get_max_permutations()):
        self.categories = Layers.get_categories()
        self.layers = Layers.get_all()
        self.indexes = Layers.get_indexed_layer_list(self.layers)
        self.permutations = Layers.get_permutations(self.indexes)
        self.nfts = []
        self.generation_order = []
        self.total = total
        self.rarity_limits = {}

    def populate_layers(self):
        return System.get_toplevel_layers()

    def parse_permutations(self):
        nfts = []
        for nft_id in self.permutations:
            layers = []
            for i in range(len(self.indexes)):
                layers.append(self.layers[self.categories[i]][self.permutations[nft_id][i]])
            nfts.append(NFT(nft_id, layers, self.categories, self.generation_order))

        return nfts

    def run(self):
        for i in range(len(self.categories)):
            self.generation_order.append(Menu.select_generation_order(self.generation_order))
        self.generation_order = Menu.select_base_index(self.generation_order)

        self.nfts = self.parse_permutations()

    def make_NFT(permutation):
        print("Making NFT")

