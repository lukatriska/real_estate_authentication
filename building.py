class Building:
    """
    Stands for a building.
    """
    def __init__(self, address):
        self.address = address


class House(Building):
    """
    Stands for a house with flats.
    """
    def __init__(self, list_of_flats, address):
        super().__init__(address)
        self.list_of_flats = list_of_flats
