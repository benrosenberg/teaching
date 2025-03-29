import chess

import os

import pygame
pygame.init()
pygame.display.set_caption('chess')

clock = pygame.time.Clock()

square_size = 100
board_wh = 8
screen_wh = board_wh * square_size

dimensions = (screen_wh, screen_wh)
screen = pygame.display.set_mode(dimensions)

colors = {
    'white' : (255, 255, 255),
    'black' : (0, 0, 0),
    'red' : (255, 0, 0),
    'green' : (0, 255, 0),
    'blue' : (0, 0, 255),
    'light' : (240, 217, 181),
    'dark' : (181, 136, 99)
}

piece_path = os.path.join('.', 'pieces')
pieces = {}
for image_filename in os.listdir(piece_path):
    piece = image_filename.split('.')[0]
    piece = piece[1] if piece[0]=='b' else piece[1].upper()
    this_path = os.path.join(piece_path, image_filename)
    pieces[piece] = pygame.image.load(this_path)
    pieces[piece].convert()

def color(r, c):
    if r % 2 == 0:
        if c % 2 == 0:
            return colors['dark']
    elif c % 2 == 1:
        return colors['dark']
    return colors['light']

def square_from_coords(x, y):
    c = x // square_size
    r = -(y % (square_size * board_wh) // square_size + 1 - board_wh)
    return board_wh * r + c
    
BOARD = chess.Board()

mouse_click_down = False
selected_square = None
key_is_down = False

next_moves = []

running = True
while running:
    key_down_count = 0
    for event in pygame.event.get():
        current_square = square_from_coords(*pygame.mouse.get_pos())
        if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not mouse_click_down:
                mouse_click_down = True
                mouse_down_square = current_square
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click_down = False
            if current_square == mouse_down_square:
                # square click confirmed
                if selected_square is not None:
                    if selected_square == current_square:
                        # deselect square
                        selected_square = None
                    else:
                        # attempt piece move
                        try:
                            # find move
                            this_move = BOARD.find_move(selected_square, current_square)
                            BOARD.push(this_move)
                            # kill redo stack
                            next_moves = []
                            # deselect square
                            selected_square = None
                        except chess.IllegalMoveError:
                            # do nothing (ignore click)
                            pass
                else:
                    # selecting first square
                    if BOARD.piece_at(current_square):
                        if BOARD.color_at(current_square) == BOARD.turn:
                            # select square
                            selected_square = current_square
        if event.type == pygame.KEYDOWN:
            key_down_count += 1
            if key_is_down:
                continue
            if event.key == pygame.K_r:
                # reset
                BOARD = chess.Board()
                mouse_click_down = False
                selected_square = None
                next_moves = []
            if event.key == pygame.K_LEFT:
                mouse_click_down = False
                selected_square = None
                try:
                    next_moves.append(BOARD.pop())
                except IndexError:
                    # do nothing (ignore keypress)
                    pass
            if event.key == pygame.K_RIGHT:
                mouse_click_down = False
                selected_square = None
                if next_moves:
                    BOARD.push(next_moves.pop())

    if key_down_count == 0:
        key_is_down = False
        

    screen.fill(colors['white'])

    # squares
    for r in range(board_wh):
        for c in range(board_wh):
            square_number = board_wh * r + c
            if selected_square == square_number:
                this_color = colors['red']
            else:
                this_color = color(r, c)
            pygame.draw.rect(
                screen, 
                this_color,
                # (255 * (square_number/64),
                #  255 * (square_number/64),
                #  255 * (square_number/64)),
                pygame.Rect(
                    square_size * c,
                    square_size * (board_wh - r - 1),
                    square_size,
                    square_size
                ) 
            )
    
    # pieces
    for r in range(board_wh):
        for c in range(board_wh):
            square_number = board_wh * r + c
            this_piece = BOARD.piece_at(square_number)
            if not this_piece:
                continue
            screen.blit(
                pieces[this_piece.symbol()], 
                (square_size * c, square_size * (board_wh - r - 1))
            )

    # check for checkmate
    if BOARD.is_checkmate():
        if BOARD.turn: # white to move
            checkmate_color = colors['black']
        else: # black to move
            checkmate_color = colors['white']
        pygame.draw.rect(
            screen,
            checkmate_color,
            pygame.Rect(0, 0, *dimensions), 
            width=10
        )
    
    clock.tick(60)
    pygame.display.flip()




