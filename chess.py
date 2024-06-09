import pygame

# تهيئة مكتبة pygame
pygame.init()

# إعداد ألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (139, 69, 19)
LIGHT_BROWN = (245, 222, 179)

# إعداد حجم النافذة
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# إعداد النافذة
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('لعبة الشطرنج')

# إعداد الخط
font = pygame.font.SysFont('Arial', 48)

# تعيين القطع بأحرف
pieces = {
    'bR': '♜', 'bN': '♞', 'bB': '♝', 'bQ': '♛', 'bK': '♚', 'bP': '♟',
    'wR': '♖', 'wN': '♘', 'wB': '♗', 'wQ': '♕', 'wK': '♔', 'wP': '♙'
}

# رسم لوحة الشطرنج
def draw_board(win):
    win.fill(LIGHT_BROWN)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, DARK_BROWN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# رسم القطع
def draw_pieces(win, board):
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != '--':
                text = font.render(pieces[piece], True, BLACK if piece[0] == 'b' else WHITE)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                win.blit(text, text_rect)

# الإعدادات الرئيسية
def main():
    board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['--', '--', '--', '--', '--', '--', '--', '--'],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
    ]

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_board(win)
        draw_pieces(win, board)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()