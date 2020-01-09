## @file game_grid.py
#  @author Tim Choy
#  @game_grid
#  @date Jan 8, 2020

class game_grid:

    x = 0
    y = 0
    cell = set()

    # s is a 2D grid of size x * y
    s = []

    def init(self, x, y):
        if (x <= 0 or y <= 0):
            raise IndexError

        self.x = x
        self.y = y

        self.s = [[False] * y for i in range(x)]

    def get_rows(self):
        return self.x

    def get_cols(self):
        return self.y

    def get_num_cell(self):
        return len(self.cell)

    def get_cell(self, x, y):
        return self.s[x][y]

    def add_cell(self, x, y):
        if (x >= self.x or x < 0 or y >= self.y or y < 0):
            raise IndexError

        self.s[x][y] = True
        self.cell.add((x, y))

    def move(self):
        new_cells = self.__cell_value()
        self.cell = set()

        self.s = [[False] * self.y for i in range(self.x)]

        for i in new_cells:
            self.add_cell(i[0], i[1])

    def check_end(self):
        next_set = self.__cell_value()
        if (next_set == self.cell or self.get_num_cell() == 0):
            return True
        return False

    def print_board(self):
        for i in self.s:
            print(i)

    def __cell_value(self):
        adj_cells = 0
        new_cells = set()

        for i in range(self.x):
            for j in range(self.y):
                if (i == 0):
                    if (j == 0):
                        adj_cells = self.__tl_cell()
                    elif (j == self.y - 1):
                        adj_cells = self.__tr_cell()
                    else:
                        adj_cells = self.__t_cell(j)

                elif (i == self.x - 1):
                    if (j == 0):
                        adj_cells = self.__bl_cell()
                    elif (j == self.y - 1):
                        adj_cells = self.__br_cell()
                    else:
                        adj_cells = self.__b_cell(j)

                else:
                    if (j == 0):
                        adj_cells = self.__l_cell(i)
                    elif (j == self.y - 1):
                        adj_cells = self.__r_cell(i)
                    else:
                        adj_cells = self.__c_cell(i, j)

                if ((self.s[i][j] and (adj_cells == 2 or adj_cells == 3)) or (not self.s[i][j] and adj_cells == 3)):
                    new_cells.add((i, j))
        return new_cells

    def __tl_cell(self):
        count = 0
        if self.s[0][1]: count += 1
        if self.s[1][0]: count += 1
        if self.s[1][1]: count += 1
        return count

    def __t_cell(self, j):
        count = 0
        if self.s[0][j - 1]: count += 1
        if self.s[0][j + 1]: count += 1
        if self.s[1][j - 1]: count += 1
        if self.s[1][j]: count += 1
        if self.s[1][j + 1]: count += 1
        return count

    def __tr_cell(self):
        count = 0
        if self.s[0][self.y - 2]: count += 1
        if self.s[1][self.y - 2]: count += 1
        if self.s[1][self.y - 1]: count += 1
        return count

    def __l_cell(self, i):
        count = 0
        if self.s[i - 1][0]: count += 1
        if self.s[i + 1][0]: count += 1
        if self.s[i - 1][1]: count += 1
        if self.s[i][1]: count += 1
        if self.s[i + 1][1]: count += 1
        return count

    def __c_cell(self, i, j):
        count = 0
        if self.s[i - 1][j - 1]: count += 1
        if self.s[i][j - 1]: count += 1
        if self.s[i + 1][j - 1]: count += 1
        if self.s[i - 1][j]: count += 1
        if self.s[i + 1][j]: count += 1
        if self.s[i - 1][j + 1]: count += 1
        if self.s[i][j + 1]: count += 1
        if self.s[i + 1][j + 1]: count += 1
        return count

    def __r_cell(self, i):
        count = 0
        if self.s[i - 1][self.y - 1]: count += 1
        if self.s[i + 1][self.y - 1]: count += 1
        if self.s[i - 1][self.y - 2]: count += 1
        if self.s[i][self.y - 2]: count += 1
        if self.s[i + 1][self.y - 2]: count += 1
        return count

    def __bl_cell(self):
        count = 0
        if self.s[self.x - 2][0]: count += 1
        if self.s[self.x - 2][1]: count += 1
        if self.s[self.x - 1][1]: count += 1
        return count

    def __b_cell(self, j):
        count = 0
        if self.s[self.x - 2][j - 1]: count += 1
        if self.s[self.x - 2][j]: count += 1
        if self.s[self.x - 2][j + 1]: count += 1
        if self.s[self.x - 1][j - 1]: count += 1
        if self.s[self.x - 1][j + 1]: count += 1
        return count

    def __br_cell(self):
        count = 0
        if self.s[self.x - 1][self.y - 2]: count += 1
        if self.s[self.x - 2][self.y - 2]: count += 1
        if self.s[self.x - 2][self.y - 1]: count += 1
        return count