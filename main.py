import pygame
import chess
from board import draw_board, draw_pieces, load_pieces, get_square_under_mouse
from ai import make_ai_move


pygame.init()


WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')


pieces = load_pieces(SQUARE_SIZE)


board = chess.Board()


selected_square = None
turn = chess.WHITE


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and turn == chess.WHITE:
            square = get_square_under_mouse(SQUARE_SIZE)
            if selected_square:
                move = chess.Move(selected_square, square)
                if move in board.legal_moves:
                    board.push(move)
                    turn = chess.BLACK
                selected_square = None
            else:
                selected_square = square if board.piece_at(square) else None

    if turn == chess.BLACK:
        make_ai_move(board)
        turn = chess.WHITE

    draw_board(window, SQUARE_SIZE)
    draw_pieces(window, board, pieces, SQUARE_SIZE)
    pygame.display.flip()

pygame.quit()
