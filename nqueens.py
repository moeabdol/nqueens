import board
import urwid

class NQueensModel(object):
    def __init__(self, N=4):
        self.N = N
        self.solution_list = []
        self.number_of_solutions = 0

    def solve(self):
        for i in range(self.N):
            self.solution_list.append(i)
        self.number_of_solutions = 1

class NQueensView(urwid.WidgetWrap):
    palette = [
        ('empty_black', 'black', 'black'),
        ('empty_white', 'white', 'white'),
        ('queen_on_black', 'light blue', 'black', 'standout'),
        ('queen_on_white', 'light blue', 'white', 'standout'),
        ('body', 'black', 'light gray', 'standout'),
        ('screen_edge', 'light blue', 'dark blue'),
        ('main_shadow', 'dark gray', 'black'),
        ('line', 'black', 'light gray', 'standout'),
        ('button', 'white', 'black', 'standout'),
    ]

    def __init__(self, controller, N=4):
        self.controller = controller
        self.N = N
        self.board = None
        self.controls = None
        super(NQueensView, self).__init__(self.main_window())

    def button(self, text, function):
        w = urwid.Button(text, function)
        w = urwid.AttrWrap(w, 'button')
        return w

    def control_panel(self):
        control_widgets = [
            urwid.Text('Number of queens: ' + str(self.N)),
            urwid.GridFlow([
                self.button('-', self.on_decrease_button),
                self.button('+', self.on_increase_button),
            ], cell_width=5, h_sep=2, v_sep=0, align='center'),
            urwid.Divider(),
            urwid.Text('Number of solutions: 0'),
            urwid.GridFlow([
                self.button('Solve', self.on_solve_button)
            ], cell_width=9, h_sep=0, v_sep=0, align='center'),
            urwid.Divider(),
            urwid.Text('Solution: 0', 'center'),
            urwid.GridFlow([
                self.button('Prev', self.on_prev_button),
                self.button('Next', self.on_next_button),
            ], cell_width=8, h_sep=2, v_sep=0, align='center'),
            urwid.Divider(),
            urwid.Divider(),
            urwid.Divider(),
            urwid.GridFlow([
                self.button('Quit', self.quit)
            ], cell_width=8, h_sep=0, v_sep=0, align='center'),
        ]
        w = urwid.ListBox(urwid.SimpleListWalker(control_widgets))
        return w

    def main_shadow(self, w):
        bg = urwid.AttrWrap(urwid.SolidFill(u'\u2592'), 'screen_edge')
        shadow = urwid.AttrWrap(urwid.SolidFill(u' '), 'main_shadow')
        bg = urwid.Overlay(shadow, bg,
            ('fixed left', 3), ('fixed right', 1),
            ('fixed top', 2), ('fixed bottom', 1))
        w = urwid.Overlay(w, bg,
            ('fixed left', 2), ('fixed right', 3),
            ('fixed top', 1), ('fixed bottom', 2))
        return w

    def main_window(self):
        self.board = board.Board(self.N)
        board_wrap = urwid.Filler(self.board, valign='top')
        vline = urwid.AttrWrap(urwid.SolidFill(u'\u2502'), 'line')
        self.controls = self.control_panel()
        w = urwid.Columns([
            board_wrap,
            ('fixed', 1, vline),
            ('fixed', 25, self.controls),
        ], dividechars=1, focus_column=2)
        w = urwid.Padding(w, ('fixed left', 1), ('fixed right', 0))
        w = urwid.AttrWrap(w, 'body')
        w = urwid.LineBox(w)
        w = urwid.AttrWrap(w, 'line')
        w = self.main_shadow(w)
        return w

    def on_solve_button(self, w):
        pass

    def on_decrease_button(self, w):
        if self.N > 1:
            self.N -= 1
            #self.controller.decrease_n()
            self.controls.body[0].set_text('Number of queens: ' + str(self.N))
            #self.board.decrease_n()

    def on_increase_button(self, w):
        self.N += 1
        #self.controller.increase_n()
        self.controls.body[0].set_text('Number of queens: ' + str(self.N))
        #self.board.increase_n()

    def on_prev_button(self, w):
        pass

    def on_next_button(self, w):
        pass

    def quit(self, w):
        raise urwid.ExitMainLoop()

def main():
    queens = NQueensView(None)
    urwid.MainLoop(queens, queens.palette).run()

if __name__ == '__main__':
    main()
