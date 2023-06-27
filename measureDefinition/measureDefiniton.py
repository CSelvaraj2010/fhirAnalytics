class MeasureDefiniton:
    """ Class to hold the definition of a measure. """

    def __init__(self, name, description, unit):
        """ Constructor. """

        self.name = name
        self.description = description
        self.unit = unit

    def __str__(self):
        """ String representation. """

        return self.name + " (" + self.unit + ")"

    def __repr__(self):
        """ Representation. """

        return self.__str__()