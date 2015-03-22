class NQueensModel(object):
    def __init__(self, N=4):
        self.N = N
        self.solution_list = []
        self.number_of_solutions = 0

    def solve(self):
        for i in range(self.N):
            self.solution_list.append(i)
        self.number_of_solutions = 1
