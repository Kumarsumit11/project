import chess

def get_possible_moves(fen: str):
    board = chess.Board(fen)
    legal_moves = list(board.legal_moves)
    for move in legal_moves:
        print(move)
    
    return len(legal_moves)

fen_start = chess.STARTING_FEN
print(f"Possible moves from the starting position:")
possible_moves = get_possible_moves(fen_start)
print(f"Total possible moves: {possible_moves}")
