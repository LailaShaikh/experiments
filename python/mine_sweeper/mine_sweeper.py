"""
1. By Default 3X3 grid 
2. 2 mines are created in the grid at random position


"""


import random
import sys

CATEGORY_MARKS = {'mine': 'f', 'open': 'O', 'predict':'**'}

class Mine(object):
    def __init__(self, num_grids=3):
        print "Creating %s grid mine." %str(num_grids)
        self.num_grids = num_grids
      
    def initiate_mine(self):
        self.create_grid()
        self.fill_random_mines()
        self.fill_random_mines()

    def create_grid(self):
        self.grid = []
        for i in range(self.num_grids):
            self.grid.append(range(self.num_grids))
        return self.grid

    def fill_random_mines(self):
        pos1 = random.randrange(self.num_grids)
        pos2 = random.randrange(self.num_grids)

        self.mark('mine',pos = (pos1, pos2,))

    def check_extension(self, pos):
        pos1, pos2 = pos
        possible_adj = []
        count = 0

        def calculate_pos(pos, operator='add'):
            if operator == 'add':
                pos += 1
            elif operator == 'sub':
                pos -= 1
            return (True,pos) if pos < self.num_grids and pos >= 0 else (False, pos)

        def find_possible_pos(pos, var_pos=1, operator='add'):
            flag, temp_pos = calculate_pos(pos, operator=operator)
            print flag, temp_pos
            co_ord = (temp_pos, pos2) if var_pos == 1 else (pos1, temp_pos)
            print co_ord
            return 1 if flag and self.is_mine(co_ord) else 0

        count += find_possible_pos(pos1, var_pos=1, operator="add")
        count += find_possible_pos(pos1, var_pos=1, operator="sub")
        count += find_possible_pos(pos2, var_pos=2, operator="add")
        count += find_possible_pos(pos2, var_pos=2, operator="sub")

        return count

    def mark(self, _category, pos):
        print _category
       
        if _category == 'mine' or _category == 'predict':
            self.grid[pos[0]][pos[1]] = CATEGORY_MARKS.get(_category, 'x')
        else:
            adj_mine_count = self.check_extension(pos)
            self.grid[pos[0]][pos[1]] = str(adj_mine_count)+'M'
       
        print "marking - %s - %s" %(_category, pos)
        self.print_grid()
        
        self.is_game_over()

    def is_game_over(self):
        values_to_check = CATEGORY_MARKS.values()
        values_to_check.remove('**')
        for i in self.grid:
            for k in i:
                if k not in values_to_check:
                    print "Doing Good! Go ahead!"
                    self.print_grid()
                    return False
        print "Game over"
        return True
        
    def is_mine(self, pos):
        return True if self.grid[pos[0]][pos[1]] == 'f' else False

    def print_grid(self):
        print "O = Opened, f = mine \n"
        print "\t\t (Actual Grid)"
        for i in self.grid:
            print ' '.join([str(i) for i in i])
        print '*' * 10

        print "\t\t (Fuzzy Grid)"

        for j in self.grid:
            f = lambda x: x if x == 'O' or 'M' in x or '*' in x else 'x'
            print ' '.join([f(str(i)) for i in j])

class Player(object):
    def __init__(self, name="ThoughtWorker"):
        self.name = name
        
    def initiate_game(self):
        print "%s Starts his new game" %self.name
        self.mine = Mine(num_grids=3)
        self.mine.initiate_mine()
        self.process_the_grid()

    def open_the_grid(self):
        pos1 = input("Enter Position 1:")
        pos2 = input("Enter Position 2:")
        ft = raw_input("Flag Type:")

        return (pos1, pos2, ft)
      
    def process_the_grid(self):
        
        def do_mark():
            pos1, pos2, ft = self.open_the_grid()
            if self.mine.is_mine((pos1, pos2,)) and ft != 'P':
                print "Oops! You pressed the bomb, Game is over.."
                sys.exit(0)
                #return 
            else:
                if ft == 'P':
                    self.mine.mark('predict', (pos1, pos2, ))
                else:
                    self.mine.mark('open', (pos1, pos2, ))

        while not self.mine.is_game_over():
            do_mark()

        print "##"*15
        print "Oh! Sweet %s! you won the game; Thanks for playing the game..bye bye!" %self.name


def start_mine():
    #m = Mine()
    player = Player()
    player.initiate_game()

if __name__ == '__main__':
    start_mine()
