class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding spices to {self.type} chai...")

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("ginger")
    
    def serve(self):
        print(f"Serving {self.chai.type} chai...")
        self.chai.prepare()        

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai



shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()

