import chess

pawn_eval_white = [
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
    [0.5,  1.0,  1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
]


pawn_eval_black = pawn_eval_white[::-1]

knight_eval = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]


bishop_eval_white = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]


bishop_eval_black = bishop_eval_white[::-1]


rook_eval_white = [
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]


rook_eval_black = rook_eval_white[::-1]


queen_eval = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]


king_eval_white = [

    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
    [2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
]


king_eval_black = king_eval_white[::-1]


def get_piece_value(piece, x, y):
    if piece is None:
        return 0

    piece_type = piece.piece_type
    is_white = piece.color == chess.WHITE

    def get_absolute_value(piece_type, is_white, x, y):
        if piece_type == chess.PAWN:
            return 10 + (pawn_eval_white[y][x] if is_white else pawn_eval_black[y][x])
        elif piece_type == chess.ROOK:
            return 50 + (rook_eval_white[y][x] if is_white else rook_eval_black[y][x])
        elif piece_type == chess.KNIGHT:
            return 30 + knight_eval[y][x]
        elif piece_type == chess.BISHOP:
            return 30 + (bishop_eval_white[y][x] if is_white else bishop_eval_black[y][x])
        elif piece_type == chess.QUEEN:
            return 90 + queen_eval[y][x]
        elif piece_type == chess.KING:
            return 900 + (king_eval_white[y][x] if is_white else king_eval_black[y][x])
        else:
            return 0

    row, col = divmod(x, 8)

    absolute_value = get_absolute_value(piece_type, is_white, col, row)
    return absolute_value if is_white else -absolute_value


def evaluate_board(board):
    total_value = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            x, y = divmod(square, 8)
            total_value += get_piece_value(piece, x, y)
    return total_value


def minimax_alphabeta(board, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or board.is_game_over():

        return evaluate_board(board), None

    legal_moves = list(board.legal_moves)

    best_move = None

    if is_maximizing_player:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval, _ = minimax_alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()

            if eval > max_eval:
                max_eval = eval
                best_move = move

            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move

    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval, _ = minimax_alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()

            if eval < min_eval:
                min_eval = eval
                best_move = move

            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def make_ai_move(board, depth=1):
    _, best_move = minimax_alphabeta(
        board, depth, float('-inf'), float('inf'), board.turn)

    if best_move is not None:
        board.push(best_move)
