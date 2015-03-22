import tile
import urwid

class Board(urwid.BoxAdapter):
    def __init__(self, N=4):
        self.N = N
        cells = []
        for i in range(self.N):
            for j in range(self.N):
                if i % 2 == 0:
                    if j % 2 == 0:
                        cells.append(tile.Tile(queen=False, color='white'))
                    else:
                        cells.append(tile.Tile(queen=False, color='black'))
                else:
                    if j % 2 == 0:
                        cells.append(tile.Tile(queen=False, color='black'))
                    else:
                        cells.append(tile.Tile(queen=False, color='white'))
        self.grid = urwid.GridFlow(cells, cell_width=6, h_sep=0, v_sep=0, align='left')
        self.pad = urwid.Padding(self.grid, width=self.N * 6)
        self.fill = urwid.Filler(self.pad, valign='top')
        super(Board, self).__init__(self.fill, height=self.N * 3)