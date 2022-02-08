from concurrent.futures import process
from lib.utils.System import System
from lib.NFT import NFT
from lib.utils.Layers import Layers
from lib.utils.Menu import Menu
import random
import lib.constants as c
import math


class Generator():
    def __init__(self, total = Layers.get_max_permutations()):
        self.categories = Layers.get_categories()
        self.layers = Layers.get_all()
        self.indexes = Layers.get_indexed_layer_list(self.layers)
        self.permutations = Layers.get_permutations(self.indexes)
        self.all_possible_nfts = []
        self.final_nfts = []
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
            self.all_possible_nfts.append(NFT(nft_id, layers, self.categories, self.generation_order))

    def __get_layers_category_from_indexes(self, i):
        return self.categories[i]

    def __get_layers_from_permutation_set(self, nft_id, i):
        return self.permutations[nft_id][i]

    def run(self):
        self.__choose_amount_per_rarity()

        for i in range(len(self.categories)):
            self.generation_order.append(Menu.select_generation_order(self.generation_order))
        self.generation_order = Menu.select_base_index(self.generation_order)
    
    def __choose_amount_per_rarity(self):
        nfts_by_rarity = self.get_nfts_by_rarity()
        submitted = []

        for rarity in nfts_by_rarity:
            # if rarity == c.RARITY[1]:
            #     for nft in nfts_by_rarity[rarity]:
            #         self.final_nfts.append(nft)

            # elif rarity != c.RARITY[0]:
            if rarity != c.RARITY[0]:
                total = int(input(f"Input how many {rarity} to generate ({len(nfts_by_rarity[rarity])}): "))
                if total == 0 or total == len(nfts_by_rarity[rarity]):
                    total = len(nfts_by_rarity[rarity])
                    for i in range(0, total):
                        submitted.append(i)

                else:
                    for i in range(0, total):
                        r = random.randrange(0, len(nfts_by_rarity[rarity]) - 1)
                        while r in submitted:
                            r = random.randrange(0, len(nfts_by_rarity[rarity]) - 1)
                        submitted.append(r)

                for id in submitted:
                    self.final_nfts.append(nfts_by_rarity[rarity][id])
                submitted = []
        

    def get_nfts_by_rarity(self):
        ret = {}
        for rarity in c.RARITY:
            ret[rarity] = []

        for nft in self.all_possible_nfts:
            ret[c.RARITY[nft.rarity]].append(nft)

        return ret

    def split_nfts_for_processes(self, processor_count = 1):
        total_nfts = len(self.final_nfts)
        nfts_per_segment = total_nfts / processor_count
        segmented_nfts = []

        if total_nfts % processor_count != 0:
            for j in range(0, processor_count):
                new_list = []
                for i in range(0, total_nfts - processor_count, processor_count):
                    new_list.append(self.final_nfts[i + j])
                segmented_nfts.append(new_list)
        else:
            for i in range(0, processor_count):
                new_list = []
                _from = int(i * nfts_per_segment)
                _to = int((i + 1) * (nfts_per_segment - 1))
                new_list.append(self.final_nfts[_from : _to])
                segmented_nfts.append(new_list)
                
        return segmented_nfts