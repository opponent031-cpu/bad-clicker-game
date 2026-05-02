import pygame, sys, time

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ---------------- STATE ----------------
global_clicks = 0
multiplier = 1
level = 1

click_times = []

# ---------------- LEVEL 1 ----------------
next_lvl1 = 750

# ---------------- LEVEL 2 ----------------
lvl2_clicks = 0
lvl2_threshold = 6500

circle_color = (255, 60, 60)

# ---------------- LOOP ----------------
running = True
while running:

    screen.fill((0, 0, 0))
    now = time.time()

    # CPS
    click_times = [t for t in click_times if now - t <= 1]
    cps = len(click_times)

    # 💥 100 CPS = crash
    if cps >= 100:
        screen.fill((0, 0, 0))
        txt = font.render("THATS IT!", True, (0, 120, 255))
        screen.blit(txt, (WIDTH//2 - 120, HEIGHT//2))
        pygame.display.flip()
        time.sleep(1.2)
        pygame.quit()
        sys.exit()

    # ---------------- LEVEL SWITCH ----------------
    if global_clicks >= 50000 and level == 1:
        level = 2
        multiplier = 2
        global_clicks = 0
        lvl2_clicks = 0
        circle_color = (0, 255, 0)

    # ---------------- INPUT ----------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            global_clicks += multiplier
            click_times.append(now)

            # ---------------- LEVEL 1 ----------------
            if level == 1:
                if global_clicks >= next_lvl1:
                    multiplier += 2
                    next_lvl1 += 750

            # ---------------- LEVEL 2 ----------------
            if level == 2:
                lvl2_clicks += multiplier

                if lvl2_clicks >= lvl2_threshold:
                    lvl2_clicks -= lvl2_threshold
                    multiplier += 4
                    lvl2_threshold += 6500

    # ---------------- DRAW ----------------
    pygame.draw.circle(screen, circle_color,
                       (WIDTH//2, HEIGHT//2),
                       120)

    screen.blit(font.render(f"Clicks: {global_clicks}", True, (255,255,255)), (30, 30))
    screen.blit(font.render(f"Multiplier: x{multiplier}", True, (200,200,200)), (30, 80))
    screen.blit(font.render(f"CPS: {cps}", True, (150,150,150)), (30, 130))
    screen.blit(font.render(f"Level: {level}", True, (120,120,120)), (30, 180))

    # ---------------- CPS TEXTS (ВОССТАНОВЛЕНО 100%) ----------------

    if cps >= 12:
        screen.blit(font.render("Thats pretty fast! Good job :)", True, (0,255,0)),
                    (120, HEIGHT//2 - 160))

    if cps >= 35:
        screen.blit(font.render("Uhm... Are you cheating?", True, (255,255,0)),
                    (160, HEIGHT//2 - 120))

    if cps >= 50:
        screen.blit(font.render("Slow down bro!", True, (255,0,0)),
                    (260, HEIGHT//2 - 80))

    if cps <= 2:
        screen.blit(font.render("lame bro you can do better bruh", True, (180,180,180)),
                    (90, HEIGHT//2 - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()