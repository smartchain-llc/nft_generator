from lib.utils.System import System
from lib.NFT import NFT
from lib.utils.Layers import Layers
from lib.utils.Menu import Menu

import lib.constants as c
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

    def parse_permutations(self):
        for nft_id in self.permutations:
            layers = []
            for i in range(len(self.indexes)):
                category = self.__get_layers_category_from_indexes(i)
                permutation = self.__get_layers_from_permutation_set(nft_id, i)
                layers.append(self.layers[category][permutation])
            self.nfts.append(NFT(nft_id, layers, self.categories, self.generation_order))

    def __get_layers_category_from_indexes(self, i):
        return self.categories[i]

    def __get_layers_from_permutation_set(self, nft_id, i):
        return self.permutations[nft_id][i]

    def run(self):
        for i in range(len(self.categories)):
            self.generation_order.append(Menu.select_generation_order(self.generation_order))
        self.generation_order = Menu.select_base_index(self.generation_order)

    def get_nfts_by_rarity(self):
        ret = {}
        for rarity in c.RARITY:
            ret[rarity] = []

        for nft in self.nfts:
            ret[c.RARITY[nft.rarity]].append(nft)

        return ret
