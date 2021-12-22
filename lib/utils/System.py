import os
import lib.constants as static
# Class that holds utiliy functions related to the operatin systems and files
class System:
    def count_layers_l():
        return len(os.listdir(static.BASE_LAYERS_DIR))

    def layers_directory_list(_path = ""):
        path = static.BASE_LAYERS_DIR + _path
        return os.listdir(path)

    def ignore(file):
        return file in static.IGNORE

    def get_toplevel_layers_list():
        return os.listdir(static.BASE_LAYERS_DIR)
    def get_toplevel_layers_count():
        return len(os.listdir(static.BASE_LAYERS_DIR))

    def get_sublevel_layers_from(layer):
        layers = os.listdir(static.BASE_LAYERS_DIR + layer)
        for item in static.IGNORE:
            if item in layers:
                layers.remove(item)
        
        return layers

    def touch(file_uri):
        file = open(file_uri, "r+b")
        file.close()

    def get_base_file(filename):
        files = os.listdir(static.BASE_IMG_DIR)
        if filename in files:
            return static.BASE_IMG_DIR + filename