class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = [[int(r) for r in row.split(' ')] for row in matrix_string.splitlines()]
        self.columns = [list(tpl) for tpl in list(zip(*self.rows))]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]