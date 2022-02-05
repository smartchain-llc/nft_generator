import json

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

    def parse_layout(self, layout):
        for trait, value in layout.items():
            self.attributes.append({"trait_type" : trait, "value" : value})
    
    def generate(self):
        data = json.dumps({
           "name" : self.name,
            "description" : self.description,
            "collection": self.collection,
            "symbol": self.symbol,
            "seller-fee-basis-points": self.seller_fee_basis_points,
            "attributes": self.attributes,
            "creators": self.creators
            })
        print(data)
class Trait():
    def __init__(self, _type = str, _value = str):
        self.trait_type = _type
        self.value = _value.split("#")[0]