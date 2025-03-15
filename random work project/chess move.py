##program is not completed yet 
#example program h bss

import cv2
import pytesseract
import chess
import numpy as np

# Function to extract FEN from an image
def extract_fen_from_image(image_path='mere project/chesspsn.jpeg'):

    img = cv2.imread(image_path='mere project/chesspsn.jpeg')
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    text = pytesseract.image_to_string(thresh)
    
    return text.strip()

def get_possible_moves(fen: str):
    board = chess.Board(fen)
    

    legal_moves = list(board.legal_moves)
    
    return [board.san(move) for move in legal_moves]

def show_possible_moves(moves):
    if not moves:
        print("No legal moves detected.")
        return
    
    print("Possible moves:")
    for move in moves:
        print(move)

#yha s start
def main(image_path):
    # Step 1: Extract the FEN from the image
    fen = extract_fen_from_image(image_path)
    print(f"Extracted FEN: {fen}")
    
#2
    moves = get_possible_moves(fen)
    show_possible_moves(moves)

if __name__ == "__main__":
    image_path = "path_to_chess_image.jpg"  # Replace with the path to your image
    main(image_path)
