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


def draw_highlights(window, board, selected_square, square_size):

    if selected_square is None:
        return

    select_color = (255, 215, 0)
    capture_color = (230, 60, 60)
    move_color = (255, 235, 59)

    sel_col, sel_row = chess.square_file(selected_square), chess.square_rank(selected_square)
    sel_x, sel_y = sel_col * square_size, (7 - sel_row) * square_size

    pygame.draw.rect(
        window,
        select_color,
        pygame.Rect(sel_x, sel_y, square_size, square_size),
        width=4
    )

    legal_moves = [m for m in board.legal_moves if m.from_square == selected_square]

    for move in legal_moves:
        to_square = move.to_square
        to_col, to_row = chess.square_file(to_square), chess.square_rank(to_square)
        x, y = to_col * square_size, (7 - to_row) * square_size

        if board.is_capture(move):
            pygame.draw.rect(
                window,
                capture_color,
                pygame.Rect(x, y, square_size, square_size),
                width=4
            )
        else:
            center = (x + square_size // 2, y + square_size // 2)
            radius = max(6, square_size // 7)
            pygame.draw.circle(window, move_color, center, radius)