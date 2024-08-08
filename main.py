import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройка окна
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sound Player")

# Загрузка звуков
sounds = {
    pygame.K_f: pygame.mixer.Sound('letters/а.wav'),
    pygame.K_COMMA: pygame.mixer.Sound('letters/б.wav'),
    pygame.K_d: pygame.mixer.Sound('letters/в.wav'),
    pygame.K_u: pygame.mixer.Sound('letters/г.wav'),
    pygame.K_l: pygame.mixer.Sound('letters/д.wav'),
    pygame.K_t: pygame.mixer.Sound('letters/е.wav'),
    pygame.K_SEMICOLON: pygame.mixer.Sound('letters/ж.wav'),
    pygame.K_p: pygame.mixer.Sound('letters/з.wav'),
    pygame.K_b: pygame.mixer.Sound('letters/и.wav'),
    pygame.K_q: pygame.mixer.Sound('letters/й.wav'),
    pygame.K_r: pygame.mixer.Sound('letters/к.wav'),
    pygame.K_k: pygame.mixer.Sound('letters/л.wav'),
    pygame.K_v: pygame.mixer.Sound('letters/м.wav'),
    pygame.K_y: pygame.mixer.Sound('letters/н.wav'),
    pygame.K_j: pygame.mixer.Sound('letters/о.wav'),
    pygame.K_g: pygame.mixer.Sound('letters/п.wav'),
    pygame.K_h: pygame.mixer.Sound('letters/р.wav'),
    pygame.K_c: pygame.mixer.Sound('letters/с.wav'),
    pygame.K_n: pygame.mixer.Sound('letters/т.wav'),
    pygame.K_e: pygame.mixer.Sound('letters/у.wav'),
    pygame.K_a: pygame.mixer.Sound('letters/ф.wav'),
    pygame.K_LEFTBRACKET: pygame.mixer.Sound('letters/х.wav'),
    pygame.K_w: pygame.mixer.Sound('letters/ц.wav'),
    pygame.K_x: pygame.mixer.Sound('letters/ч.wav'),
    pygame.K_i: pygame.mixer.Sound('letters/ш.wav'),
    pygame.K_o: pygame.mixer.Sound('letters/щ.wav'),
    pygame.K_RIGHTBRACKET: pygame.mixer.Sound('letters/ъ.wav'),
    pygame.K_s: pygame.mixer.Sound('letters/ы.wav'),
    pygame.K_m: pygame.mixer.Sound('letters/ь.wav'),
    pygame.K_QUOTE: pygame.mixer.Sound('letters/э.wav'),
    pygame.K_PERIOD: pygame.mixer.Sound('letters/ю.wav'),
    pygame.K_z: pygame.mixer.Sound('letters/я.wav'),
}

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in sounds:
                sounds[event.key].play()

    screen.fill((255, 255, 255))  # Очистка экрана
    font = pygame.font.Font(None, 36)
    text = font.render("Нажимайте на клавиши!", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 150))
    screen.blit(text, text_rect)
    pygame.display.flip()
