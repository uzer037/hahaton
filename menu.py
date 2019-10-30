import pygame
maxbtn = 4
def create(screen, xsz, ysz):
    maxbtn = 4
    status = 0 #0=ok,-1=exit
    width = 5
    height = 2
    step_lim = -1
    time_lim = -1
    enem = 0

    bg = pygame.image.load('menu_bg.png')
    logo = pygame.image.load('logo.png')

    bupr = pygame.image.load('btn.png')
    bpr = pygame.image.load('btn_pressed.png')

    
    mx = max(xsz, ysz)
    ms = min(xsz,ysz)
    bg = pygame.transform.scale(bg,(mx,mx))
    
    side = ms // 18
    

    btn = 0 #curr btn
    done = False

    

    font = pygame.font.Font('PoiretOne-Regular.ttf', 25)

    txt = [font.render('начать', False, (255,255,255)), font.render('очки', False, (255,255,255)), font.render('настройки', False, (255,255,255)), font.render('выйти', False, (255,255,255))]
    font.set_bold(1)
    txtb = [font.render('начать', False, (255,255,255)), font.render('очки', False, (255,255,255)), font.render('настройки', False, (255,255,255)), font.render('выйти', False, (255,255,255))]
    
    logo = font.render('THE EXPEDITION', True, (255,255,255))
    logo = pygame.transform.scale(logo,(side*7,side))

    b = [txt[0]]*maxbtn

    for i in range(maxbtn):
        b[i] = txt[i]


    b[btn] = txtb[btn]
    bg.scroll(dx=((xsz - mx)//2), dy=((ysz - mx)//2))
    screen.blit(bg, (0,0))
    screen.blit(logo, (side,side*7))
    screen.blit(b[0], (side,side*9))
    screen.blit(b[1], (side,side*10))
    screen.blit(b[2], (side,side*11))
    screen.blit(b[3], (side,side*12))
    
    pygame.display.flip()
    while not done:
        maxbtn = 4

        screen.blit(bg, (0,0))
        screen.blit(logo, (side,side*7))
                
        screen.blit(b[0], (side,side*9))
        screen.blit(b[1], (side,side*10))
        screen.blit(b[2], (side,side*11))
        screen.blit(b[3], (side,side*12))
                
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                for i in range(maxbtn):
                    b[i] = txt[i]
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    btn = up(btn)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    btn = dn(btn)

                b[btn] = txtb[btn]
                if event.key == pygame.K_SPACE or event.key == 13: #13 = K_KP_ENTER (BECAUSE REASONS)
                    if(btn == 0): #start game
                        return (0, width, height, step_lim, time_lim, enem)
                    if(btn == 1): #scores
                        print("scores")
                    if(btn == 2): #settings game
                        print("settings")
                        width, height, step_lim, time_lim, enem = settings(screen, width, height, step_lim, time_lim, enem, bg, side)
                    if(btn == 3): #exit game
                        return (-1, 0,0,0,0)


def up(btn):
    btn = btn - 1
    while(btn >= maxbtn):
        btn = btn - maxbtn
    while(btn < 0):
        btn = btn + maxbtn
    return btn

def dn(btn):
    btn = btn + 1
    while(btn >= maxbtn):
        btn = btn - maxbtn
    while(btn < 0):
        btn = btn + maxbtn
    return btn

def settings(screen, width, height, step_lim, time_lim, enem, bg, side):
    font = pygame.font.Font('PoiretOne-Regular.ttf', 25)

    maxbtn = 6
    btn = 0
    done = False
    while not done:
        font.set_bold(True)
        sett = font.render('Настройки:', False, (255,255,255))
        font.set_bold(False)
        pos = font.render('Размер поля:', False, (255,255,255))
        if(btn == 0):
            font.set_bold(True)
        else:
            font.set_bold(False)
        w = font.render('  X:'+ str(width), False, (255,255,255))

        if(btn == 1):
            font.set_bold(True)
        else:
            font.set_bold(False)
        h = font.render('  Y:'+ str(height), False, (255,255,255))

        if(btn == 2):
            font.set_bold(True)
        else:
            font.set_bold(False)
        if(step_lim > 0):
            sl = font.render('Лимит шагов:' + str(step_lim), False, (255,255,255))
        else:
            sl = font.render('Лимит шагов:ОТКЛЮЧЕНО', False, (255,255,255))
                
        if(btn == 3):
            font.set_bold(True)
        else:
            font.set_bold(False)
        if(time_lim > 0):
            tl = font.render('Лимит времени:' + str(time_lim) + 'c', False, (255,255,255))
        else:
            tl = font.render('Лимит времени:ОТКЛЮЧЕНО', False, (255,255,255))

        if(btn == 4):
            font.set_bold(True)
        else:
            font.set_bold(False)
        if(enem > 0):
            en = font.render('Подвижных айсбергов:' + str(enem), False, (255,255,255))
        else:
            en = font.render('Подвижных айсбергов:ОТКЛЮЧЕНО', False, (255,255,255))

        if(btn == 5):
            font.set_bold(True)
        else:
            font.set_bold(False)
        ex = font.render('Выйти', False, (255,255,255))

        screen.blit(bg, (0,0))
        screen.blit(sett, (side,side//2))
        screen.blit(pos, (side,side*1.5))
        screen.blit(w, (side,side*4))
        screen.blit(h, (side,side*6))
        screen.blit(sl, (side,side*8))
        screen.blit(tl, (side,side*10))
        screen.blit(en, (side,side*12))
        screen.blit(ex, (side,side*14))
                
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    btn = btn - 1
                    while(btn >= maxbtn):
                        btn = btn - maxbtn
                    while(btn < 0):
                        btn = btn + maxbtn
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    btn = btn + 1
                    while(btn >= maxbtn):
                        btn = btn - maxbtn
                    while(btn < 0):
                        btn = btn + maxbtn

                if event.key == pygame.K_SPACE or event.key == 13:
                    if btn == 5:
                        return (width, height, step_lim, time_lim, enem)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if btn == 0:
                        if(width - 1 > 0):
                            width -= 1
                    if btn == 1:
                        if(height - 1 > 0):
                            height -= 1
                    if btn == 2:
                        if(step_lim - 1 >= 0):
                            step_lim -= 1
                        if(step_lim == 0):
                            step_lim = -1
                    if btn == 3:
                        if(time_lim - 1 >= 0):
                            time_lim -= 1
                        if(time_lim == 0):
                            time_lim = -1
                    if btn == 4:
                        if(enem - 1 >= 0):
                            enem -= 1
                        if(enem == 0):
                            enem = -1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if btn == 0:
                        width += 1
                    if btn == 1:
                        height += 1
                    if btn == 2:
                        step_lim += 1
                        if(step_lim == 0):
                            step_lim = 1
                    if btn == 3:
                        time_lim += 1
                        if(time_lim == 0):
                            time_lim = 1
                    if btn == 4:
                        enem += 1
                        if(enem == 0):
                            enem = 1

    