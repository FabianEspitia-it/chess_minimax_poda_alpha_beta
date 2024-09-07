import pygame
import chess
import os

WHITE = (255, 255, 255)
BLACK = (105, 146, 62)


PIECE_SYMBOLS = {
    'p': 'pawn',
    'n': 'knight',
    'b': 'bishop',
    'r': 'rook',
    'q': 'queen',
    'k': 'king'
}


def draw_board(window, square_size):

    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, pygame.Rect(
                col * square_size, row * square_size, square_size, square_size))


def load_pieces(square_size):

    pieces = {}
    for color in ['white', 'black']:
        for piece in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            image = pygame.image.load(
                os.path.join(f'pieces/{color}_{piece}.png'))
            image = pygame.transform.scale(image, (square_size, square_size))
            pieces[f'{color}_{piece}'] = image
    return pieces


def draw_pieces(window, board, pieces, square_size):

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_color = 'white' if piece.color == chess.WHITE else 'black'
            piece_name = PIECE_SYMBOLS[piece.symbol().lower()]
            piece_image = pieces[f'{piece_color}_{piece_name}']
            col, row = chess.square_file(square), chess.square_rank(square)
            window.blit(piece_image, (col * square_size,
                        (7 - row) * square_size))


def get_square_under_mouse(square_size):

    mouse_pos = pygame.mouse.get_pos()
    col = mouse_pos[0] // square_size
    row = mouse_pos[1] // square_size
    return chess.square(col, 7 - row)
