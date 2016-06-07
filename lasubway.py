"""
This is a general starting file for LASubway

TODO:
    Get the full path for Base dir in metro
"""

class LASDataObject(object):
    """
    Base object for all other LASDataObjects (metro, metro line, station)
    """
    def __init__(self, init_data):
        self.name = init_data['name']
        self.base_directory = init_data['base_dir']
        self.comments = init_data['comments']

    def export_diagram(self):
        """
        Returns a ascii table of the data object
        """
        raise NotImplementedError

    @staticmethod
    def create_box(width, title, body):
        """
        Creates a box with a title body and a specified width
        """
        pass #TODO Left off here


class Metro(LASDataObject):
    """
    """
    def __init__(self, init_data):
        super.__init__(self, init_data)
        self.required_pacakges = init_data['required_pacakges']

    def load_metro(self):
        pass


class Station(LASDataObject):
    """
    """
    def __init__(self, init_data):
        super.__init__(self, init_data)
        self.in_stream = init_data['in']   #TODO Consider multiple streams for one station
        self.out_stream = init_data['out'] #
        self.cmd = init_data['cmd']

class Box(object):
    """ASCII box drawing class"""

    def __init__(self, width, title, body):
        """Sets up class variables and creates box"""

        self.box_lines = []
        self.width = width
        self.title = title
        self.body = body
        self.build_box()

        #Iterator variable
        self.iter_index = 0

    def build_box(self):
        """Creates the box by populating the box_lines list"""

        self.box_lines = []
        boxend = '+{}+'.format(self.repeat_char('-', self.width-2))
        self.box_lines.append(boxend)
        self.format_box_string(self.title) #Add title
        self.box_lines.append('+{}+'.format(self.repeat_char('=', self.width-2)))
        self.format_box_string(self.body)  #Add body
        self.box_lines.append(boxend)


    def resize_width(self, new_width):
        """Resizes the box"""
        self.width = new_width
        self.build_box()

    def print_box(self):
        """Prints box"""
        for line in self.box_lines:
            print(line)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            line = self.box_lines[self.iter_index]
        except IndexError:
            raise StopIteration
        self.iter_index += 1
        return line

    def box_to_string(self):
        """Returns box as one string"""
        return '\n'.join(self.box_lines)

    def format_box_string(self, string):
        """adds a multiline string to the box"""

        string.lstrip() #Remove begining whitespace
        while len(string) > self.width-2:
            try:
                self.format_box_line(string[:self.width-2])
                string = string[(self.width-2):].lstrip()
            except IndexError:
                self.format_box_line(string)
        self.format_box_line(string)

    def format_box_line(self, string):
        """Adds one line to the box"""
        self.box_lines.append('|{}{}|'.format(string, self.repeat_char(' ', self.width-len(string)-2)))

    @staticmethod
    def repeat_char(char, ntimes):
        """returns a string of chars repeated ntimes"""
        s = ""
        for i in range(ntimes):
            s += char
        return s

class Structure(Box):
    """A box that can contain a linear set of boxes from the BOX class"""

    def __init__(self, width, title, body):
        super().__init__(width, title, body)

        self.inside_box_width = width - 4
        self.box_list = []

    def add_box(self, box):
        """Adds a Box object to the ordered list of boxes"""
        if isinstance(box, Box):
            box.resize_width(self.inside_box_width)
            self.box_list.append(box)
        else:
            raise TypeError

    def print_structure(self):
        """prints the entire structure to the console"""
        for line in self.box_lines:
            print(line)

        for line in self.format_boxes():
            print(line)

    def format_boxes(self):
        """Yiels the raw string lines of each box in the box list"""
        box_len = len(self.box_list)
        for count, box in enumerate(self.box_list):
            for line in box:
                yield '| {} |'.format(line)

            #Create arrow at then end off the box
            if count < box_len:
                arrow_index = self.width//2

                tmp = list('|{}|'.format(self.repeat_char(' ', self.width-2)))
                tmp[arrow_index] = '|'
                yield "".join(tmp)
                yield "".join(tmp)

                tmp[arrow_index] = 'V'
                yield "".join(tmp)

        #Add box end line
        #TODO fix arrow for last box in struct
        yield '+{}+'.format(self.repeat_char('-', self.width-2))



if __name__ == '__main__':
    width = 20
    title = "Test Box Title 1"
    body = "How about this box formatting? Its lookin alright. Could use some word parsing when splitting strings across multiple lines"
    tbox = Box(width, title, body)

    title2 = "Test Box Title 2"
    body2 = "I need some words to fill up this space so I can get a feel for what this will look like."
    tbox2 = Box(width, title2, body2)

    tstruct = Structure(50, "test_struct", "test struct_body")
    tstruct.add_box(tbox)
    tstruct.add_box(tbox2)
    """
    """

    tstruct.print_structure()

