from lib.utils.System import System
import itertools as IT

class Layers:
    def get_categories():
        return System.get_toplevel_layers_list()

    def get_all():
        total_layers = {}
        for toplevel in Layers.get_categories():
            total_layers[toplevel] = System.get_sublevel_layers_from(toplevel)

        return total_layers

    def get_indexed_layer_list(layout):
        layer_selection_index = []
        for toplevel in layout:
            layer_selection_index.append(len(layout[toplevel]) - 1)

        return layer_selection_index

    def get_max_permutations():
        layers_dir = System.layers_directory_list()
        count = 1
        n = []

        for directory in layers_dir:
            files = System.layers_directory_list(directory)
            for file in files:
                if System.ignore(file):
                    files.pop(files.index(file))

            n.append(len(files))
        
        for i in n:
            count *= i

        return count
    
    def get_permutations(indexes):
        max_permutations = IT.product(range(max(indexes) + 1), repeat=len(indexes))
        stripped = {}
        count = 0
        for permutation in max_permutations:
            valid = True
            for i in range(len(permutation)):
                if permutation[i] > indexes[i]:
                    valid = False
                    break
            if valid:
                count += 1
                stripped[str(count)] = permutation
        
        return stripped