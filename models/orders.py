class Order():
    """_summary_
    """
    # Class initializer. It has 2 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, metal_id, size_id, style_id):
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.metal = None
        self.style = None
        self.size = None