class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        row = list(map(int, self.matrix_string.split('\n')[index - 1].split(' ')))
        return row

    def column(self, index):
        column = list(map(int, [row.split(' ')[index -1] for row in self.matrix_string.split('\n')]))
        return column

