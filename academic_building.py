from classroom import *
from building import Building


class AcademicBuilding(Classroom, Building):
    """
    Stands for an academic building (where people study) with corpus, its address and a list of classrooms.
    """
    def __init__(self, corp, corp_address, classrooms, address):
        """
        (object, str, lst(object)) -> ()
        """
        super().__init__(address)
        self.corpus = corp
        self.address = corp_address
        self.classrooms = classrooms

    def total_equipment(self):
        """
        (object) -> (lst(tuple))
        """
        all_equipment, equipment = [], {}
        for room in self.classrooms:
            all_equipment += room.equipment
        for piece in all_equipment:
            if piece in equipment:
                equipment[piece] += 1
            else:
                equipment[piece] = 1
        form = [i for i in equipment.items()]
        return form

    def __str__(self):
        """
        (object) -> (str)
        Returns a string for print().
        """
        stri = str(self.address)
        for room in self.classrooms:
            stri += '\n'
            stri += str(room)
        return stri
