class Classroom(object):
    """
    Stands for a classroom
    """
    def __init__(self, class_num, capacity, equipment):
        self.class_num = class_num
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, class_num):
        """
        (object.property) -> (bool)
        Checks if the classroom capacity is larger than the classroom in the argument, returns True if it is.
        """
        if self.capacity > class_num.capacity:
            return True
        return False

    def equipment_differences(self, class_num):
        """
        (object.property) -> (lst)
        Return the difference in equipment between the first and the second classroom.
        """
        return list(set(self.equipment) - set(class_num.equipment))

    def __str__(self):
        """
        (object) -> (str)
        Prints information about a classroom.
        """
        return "Classroom {} has a capacity of {} persons and has the " \
               "following equipment: {}.".format(self.class_num, str(self.capacity), ', '.join(self.equipment))

    def __repr__(self):
        """
        (object) -> (str)
        """
        return "[{}('{}', {}, {})]".format(str(type(self))[17:-2], self.class_num,
                                           str(self.capacity), str(self.equipment))
