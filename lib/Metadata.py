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
        self.creators = [{"address": "1234", "share" : 50}, {"address" : "5678", "share" : 50}]
        self.external_url = ""

    def append_attribute(self, _input = dict):
        for trait, value in _input.items():
            self.attributes.append(Trait({"trait_type" : trait, "value" : value}))
        
    def generate(self, filename):
        data = json.dumps({
           "name" : self.name,
            "description" : self.description,
            "collection": self.collection,
            "symbol": self.symbol,
            "seller-fee-basis-points": self.seller_fee_basis_points,
            "attributes": self.attributes,
            "creators": self.creators
            })
        output_file = open(c.META_OUTPUT_DIR + filename + ".json", "a")
        output_file.write(data)
        output_file.close
class Trait():
    def __init__(self, _type, _value):
        self.trait_type = str(_type)
        if type(_value) == str:
            self.value = _value.split("#")[0]
        else:
            self.value = _value

        return {"trait_type": self.trait_type, "value" : self.value}
