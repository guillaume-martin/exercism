class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = [[int(r) for r in row.split(' ')] for row in matrix_string.splitlines()]
        nrow = len(self.rows)
        ncol = len(self.rows[0])
        self.columns = []
        for i in range(ncol):
            self.columns.append([self.rows[j][i] for j in range(nrow)])

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]


