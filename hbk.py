import sys

class ChessPiece(object):
    """
    Base ChessPiece class
    Keeps position info

    Base ChessPiece is allowed to any number
    Each piece would need to implement find_moves function
    """

    def __init__(self):
        self._position = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def find_moves(self, from_position):
        return [0,1,2,3,4,5,6,7,8,9]

    def can_move_to(self, curr_pos):
        """
        This function will return a list of allowed moves from
        the given position list
        """
        moves = []
        if type(curr_pos) == list:
            for pos in curr_pos:
                next_moves = self.find_moves(pos)
                for move in next_moves:
                    moves.append(move)
            return moves
        else:
            return self.find_moves(curr_pos)

class Knight(ChessPiece):

    allowed_moves = {'1': [8,6],
                     '2': [7,9],
                     '3': [8,4],
                     '4': [0,3,9],
                     '6': [0,1,7],
                     '7': [2,6],
                     '8': [1,3],
                     '9': [2,4],
                     '0': [4,6]}

    def find_moves(self, from_position):
        key = str(from_position)
        if key in self.allowed_moves:
            return self.allowed_moves[key]
        return []


class Tree(object):
    """
    Basic tree class to keep track of the data structure
    It is a list of lists where tree holds multiples levels and each level
    can have multiple nodes
    """

    def __init__(self):
        self.levels = []

    def add_nodes(self, nodes):
        self.levels.append(nodes)

    def get_level(self, level):
        if level > self.depth():
            return []
        return self.levels[level]

    def depth(self):
        return len(self.levels)

def find_phone_count(piece):
    """
    Build a tree with root as allowed number. So we cant have a tree with
    root 0 or 1

    it will build a tree with 7 levels. The number of nodes in the last level
    is the number of phone numbers we are interested in
    """
    chess_piece_map = {'knight': Knight}
    if not piece.lower() in chess_piece_map:
        return None
    piece = chess_piece_map[piece.lower()]()
    total_count = 0
    for start in [3,4,5,6,7,8,9]:
        tree = Tree()
        tree.add_nodes([start])
        for i in xrange(1,7):
            next_positions = piece.can_move_to(tree.get_level(i-1))
            if len(next_positions) == 0:
                break
            tree.add_nodes(next_positions)
        if tree.depth() == 7:
            total_count += len(tree.get_level(-1))
    return total_count

def main():
    phone_count = find_phone_count('knight')
    print phone_count

if __name__ == "__main__":
    sys.exit(main())
