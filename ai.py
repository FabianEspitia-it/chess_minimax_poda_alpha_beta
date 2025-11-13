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

king_endgame_eval = [
    [-5.0, -4.0, -3.0, -2.0, -2.0, -3.0, -4.0, -5.0],
    [-3.0, -2.0, -1.0,  0.0,  0.0, -1.0, -2.0, -3.0],
    [-3.0, -1.0,  2.0,  3.0,  3.0,  2.0, -1.0, -3.0],
    [-3.0, -1.0,  3.0,  4.0,  4.0,  3.0, -1.0, -3.0],
    [-3.0, -1.0,  3.0,  4.0,  4.0,  3.0, -1.0, -3.0],
    [-3.0, -1.0,  2.0,  3.0,  3.0,  2.0, -1.0, -3.0],
    [-3.0, -3.0,  0.0,  0.0,  0.0,  0.0, -3.0, -3.0],
    [-5.0, -3.0, -3.0, -3.0, -3.0, -3.0, -3.0, -5.0]
]


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


def count_material(board):
    
    material = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type != chess.KING:
            if piece.piece_type == chess.QUEEN:
                material += 9
            elif piece.piece_type == chess.ROOK:
                material += 5
            elif piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT:
                material += 3
            elif piece.piece_type == chess.PAWN:
                material += 1
    return material


def is_endgame(board):
    
    return count_material(board) < 20


def evaluate_mobility(board):
    
    original_turn = board.turn
    
    board.turn = chess.WHITE
    white_mobility = len(list(board.legal_moves))
    
    board.turn = chess.BLACK
    black_mobility = len(list(board.legal_moves))
    
    board.turn = original_turn
    
    return (white_mobility - black_mobility) * 0.1


def evaluate_king_safety(board):
   
    safety_score = 0
    
    for color in [chess.WHITE, chess.BLACK]:
        king_square = board.king(color)
        if king_square is None:
            continue
            
       
        king_file = chess.square_file(king_square)
        king_rank = chess.square_rank(king_square)
        
        pawn_shield = 0
        for file_offset in [-1, 0, 1]:
            for rank_offset in [1, 2] if color == chess.WHITE else [-1, -2]:
                f = king_file + file_offset
                r = king_rank + rank_offset
                if 0 <= f < 8 and 0 <= r < 8:
                    square = chess.square(f, r)
                    piece = board.piece_at(square)
                    if piece and piece.piece_type == chess.PAWN and piece.color == color:
                        pawn_shield += 0.5
        
        multiplier = 1 if color == chess.WHITE else -1
        safety_score += pawn_shield * multiplier
    
    return safety_score


def evaluate_pawn_structure(board):
  
    score = 0
    
    for color in [chess.WHITE, chess.BLACK]:
        pawns = board.pieces(chess.PAWN, color)
        multiplier = 1 if color == chess.WHITE else -1
        
       
        files = {}
        for pawn in pawns:
            f = chess.square_file(pawn)
            files[f] = files.get(f, 0) + 1
        
        for count in files.values():
            if count > 1:
                score -= 0.5 * multiplier
        
      
        for pawn in pawns:
            f = chess.square_file(pawn)
            r = chess.square_rank(pawn)
            is_passed = True
            
            for enemy_pawn in board.pieces(chess.PAWN, not color):
                enemy_f = chess.square_file(enemy_pawn)
                enemy_r = chess.square_rank(enemy_pawn)
                
                if abs(enemy_f - f) <= 1:
                    if color == chess.WHITE and enemy_r > r:
                        is_passed = False
                        break
                    elif color == chess.BLACK and enemy_r < r:
                        is_passed = False
                        break
            
            if is_passed:
                advance = r if color == chess.WHITE else (7 - r)
                score += (0.5 + advance * 0.2) * multiplier
    
    return score


def evaluate_piece_coordination(board):
 
    score = 0
    
   
    for color in [chess.WHITE, chess.BLACK]:
        bishops = board.pieces(chess.BISHOP, color)
        if len(bishops) >= 2:
            multiplier = 1 if color == chess.WHITE else -1
            score += 0.5 * multiplier
    
    return score


def evaluate_center_control(board):
  
    center_squares = [chess.E4, chess.E5, chess.D4, chess.D5]
    extended_center = [chess.C3, chess.C4, chess.C5, chess.C6,
                       chess.D3, chess.D6, chess.E3, chess.E6,
                       chess.F3, chess.F4, chess.F5, chess.F6]
    
    score = 0
    
    for square in center_squares:
        piece = board.piece_at(square)
        if piece:
            value = 0.3
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
        

        white_attacks = len(board.attackers(chess.WHITE, square))
        black_attacks = len(board.attackers(chess.BLACK, square))
        score += (white_attacks - black_attacks) * 0.1
    
    for square in extended_center:
        piece = board.piece_at(square)
        if piece:
            value = 0.1
            if piece.color == chess.WHITE:
                score += value
            else:
                score -= value
    
    return score


def evaluate_board(board):
   
    if board.is_checkmate():
        return -10000 if board.turn == chess.WHITE else 10000
    
    if board.is_stalemate() or board.is_insufficient_material():
        return 0
    

    total_value = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            x, y = divmod(square, 8)
            
       
            if piece.piece_type == chess.KING and is_endgame(board):
                multiplier = 1 if piece.color == chess.WHITE else -1
                king_val = 900 + king_endgame_eval[y][x]
                total_value += king_val * multiplier
            else:
                total_value += get_piece_value(piece, x, y)
    
    
    total_value += evaluate_mobility(board) * 1.5
    total_value += evaluate_king_safety(board) * 2.0
    total_value += evaluate_pawn_structure(board) * 1.0
    total_value += evaluate_piece_coordination(board) * 1.0
    total_value += evaluate_center_control(board) * 0.8
    
    
    if board.is_check():
        total_value += 0.5 if board.turn == chess.BLACK else -0.5
    
    return total_value


def order_moves(board, moves):
   
    def move_priority(move):
        score = 0
        
        
        if board.is_capture(move):
            captured = board.piece_at(move.to_square)
            attacker = board.piece_at(move.from_square)
            if captured and attacker:
                
                victim_value = [0, 1, 3, 3, 5, 9, 0][captured.piece_type]
                attacker_value = [0, 1, 3, 3, 5, 9, 0][attacker.piece_type]
                score += 10 * victim_value - attacker_value
        
        if move.promotion:
            score += 8
        
    
        board.push(move)
        if board.is_check():
            score += 5
        board.pop()
        
        
        if move.to_square in [chess.E4, chess.E5, chess.D4, chess.D5]:
            score += 2
        
        return score
    
    return sorted(moves, key=move_priority, reverse=True)


def minimax_alphabeta(board, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    legal_moves = list(board.legal_moves)
    legal_moves = order_moves(board, legal_moves)
    
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


def make_ai_move(board, depth=3):
    _, best_move = minimax_alphabeta(
        board, depth, float('-inf'), float('inf'), board.turn)

    if best_move is not None:
        board.push(best_move)
        return best_move
    return None