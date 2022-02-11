import json
import lib.constants as c
class Metadata():
    def __init__(self):
        self.collection = ""
        self.name = ""
        self.symbol = ""
        self.description = ""
        self.seller_fee_basis_points = 0
        self.image = ""
        self.attributes = []
        self.creators = [{"address": "2pvaisL7eFbYLQtkZf2rQxUWQa6Rx3idNuTiiyK1w35d", "share" : 50}, {"address" : "3mHFWGLeyGmogch3DuadjfKfTL2cJB6y3vmFZoGKFXM1", "share" : 50}]
        self.external_url = ""

    def append_attribute(self, _input = dict):
        for trait, value in _input.items():
            self.attributes.append({"trait_type" : trait, "value" : self.__format_value_string(value)})
        
    def generate(self, filename):
        data = json.dumps({
           "name" : self.name,
            "description" : self.description,
            "collection": self.collection,
            "symbol": self.symbol,
            "image" : self.image,
            "seller-fee-basis-points": self.seller_fee_basis_points,
            "attributes": self.attributes,
            "properties" : {
            "creators": self.creators
            }
            })
        output_file = open(c.META_OUTPUT_DIR + filename + ".json", "a")
        output_file.write(data)
        output_file.close
    
    def __format_value_string(self, value):
        ret = value.split("#")[0]
        return ret
        
class Trait():
    def __init__(self, trait = dict):
        self.trait_type = str(trait["trait_type"])
        if type(trait["value"]) == str:
            self.value = trait["value"].split("#")[0]
        else:
            self.value = trait["value"]

        return {"trait_type": self.trait_type, "value" : self.value}
