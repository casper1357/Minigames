'''
Main
'''

# Libraries
import pygame, sys
from pygame.locals import *
from settings import *
from loadImages import *
import random

mainClock = pygame.time.Clock()

# Initialize pygame
pygame.init()

# Images and title
pygame.display.set_caption(gameTitle)

# Create screen
win = pygame.display.set_mode((standardResWidth, standardResHeight))

# Font
font = pygame.font.SysFont(None, 20)



# Text function
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:

        win.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), win, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                hangman()

        pygame.draw.rect(win, (255, 0, 0), button_1)
        pygame.draw.rect(win, (255, 0, 0), button_2)
        pygame.draw.rect(win, (255, 0, 0), button_3)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        win.fill((0, 0, 0))

        draw_text('game', font, (255, 255, 255), win, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        win.fill((0, 0, 0))

        draw_text('options', font, (255, 255, 255), win, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def hangman():
    running = False
    ani = 0
    click = False
    word = hangman_create_word(words)
    word_lst = word[1]
    hidden_word_lst = ["" for i in word_lst]
    print(hidden_word_lst)
    print(word)
    xpos = 650
    ypos = 300
    xchange = 0
    print(xchange)
    space = 30
    ychange = 150

    xdashes = []
    ydashes = []
    for i in range(len(word_lst)):
        if xpos+xchange <= standardResWidth - 300:
            xdashes.append(xpos+xchange)
            ydashes.append(ypos)
            xchange += dashpicsize[0] + space
        else:
            xchange = 0
            ypos += ychange


    while not running:
        win.blit(hangmanstartmenu, (0, 0))
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # Checks if mousepos is inside start button
        if hangmanbutton[0][0] < mx < hangmanbutton[0][1] and hangmanbutton[1][0] < my < hangmanbutton[1][1]:
            if click:
                running = True
        pygame.display.update()
        mainClock.tick(60)

    aKey = False
    bKey = False
    cKey = False
    dKey = False
    eKey = False
    fKey = False
    gKey = False
    hKey = False
    iKey = False
    jKey = False
    kKey = False
    lKey = False
    mKey = False
    nKey = False
    oKey = False
    pKey = False
    qKey = False
    rKey = False
    sKey = False
    tKey = False
    uKey = False
    wKey = False
    vKey = False
    xKey = False
    yKey = False
    zKey = False

    while running:
        # Cycles through the hangman images
        win.blit(hangmanAni[ani], (0, 0))
        # Creates all the dashes
        for i in range(len(xdashes)):
            win.blit(dash, (xdashes[i], ydashes[i]))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # All different keys get set to True if in the word
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_a:
                    aKey = True
                    hidden_word_lst = change_hidden("a", word_lst, hidden_word_lst)
                if event.key == K_b:
                    bKey = True
                    hidden_word_lst = change_hidden("b", word_lst, hidden_word_lst)
                if event.key == K_c:
                    cKey = True
                    hidden_word_lst = change_hidden("c", word_lst, hidden_word_lst)
                if event.key == K_d:
                    dKey = True
                    hidden_word_lst = change_hidden("d", word_lst, hidden_word_lst)
                if event.key == K_e:
                    eKey = True
                    hidden_word_lst = change_hidden("e", word_lst, hidden_word_lst)
                if event.key == K_f:
                    fKey = True
                    hidden_word_lst = change_hidden("f", word_lst, hidden_word_lst)
                if event.key == K_g:
                    gKey = True
                    hidden_word_lst = change_hidden("g", word_lst, hidden_word_lst)
                if event.key == K_h:
                    hKey = True
                    hidden_word_lst = change_hidden("h", word_lst, hidden_word_lst)
                if event.key == K_i:
                    iKey = True
                    hidden_word_lst = change_hidden("i", word_lst, hidden_word_lst)
                if event.key == K_j:
                    jKey = True
                    hidden_word_lst = change_hidden("j", word_lst, hidden_word_lst)
                if event.key == K_k:
                    kKey = True
                    hidden_word_lst = change_hidden("k", word_lst, hidden_word_lst)
                if event.key == K_l:
                    lKey = True
                    hidden_word_lst = change_hidden("l", word_lst, hidden_word_lst)
                if event.key == K_m:
                    mKey = True
                    hidden_word_lst = change_hidden("m", word_lst, hidden_word_lst)
                if event.key == K_n:
                    nKey = True
                    hidden_word_lst = change_hidden("n", word_lst, hidden_word_lst)
                if event.key == K_o:
                    oKey = True
                    hidden_word_lst = change_hidden("o", word_lst, hidden_word_lst)
                if event.key == K_p:
                    pKey = True
                    hidden_word_lst = change_hidden("p", word_lst, hidden_word_lst)
                if event.key == K_q:
                    qKey = True
                    hidden_word_lst = change_hidden("q", word_lst, hidden_word_lst)
                if event.key == K_r:
                    rKey = True
                    hidden_word_lst = change_hidden("r", word_lst, hidden_word_lst)
                if event.key == K_s:
                    sKey = True
                    hidden_word_lst = change_hidden("s", word_lst, hidden_word_lst)
                if event.key == K_t:
                    tKey = True
                    hidden_word_lst = change_hidden("t", word_lst, hidden_word_lst)
                if event.key == K_u:
                    uKey = True
                    hidden_word_lst = change_hidden("u", word_lst, hidden_word_lst)
                if event.key == K_w:
                    wKey = True
                    hidden_word_lst = change_hidden("w", word_lst, hidden_word_lst)
                if event.key == K_v:
                    vKey = True
                    hidden_word_lst = change_hidden("v", word_lst, hidden_word_lst)
                if event.key == K_x:
                    xKey = True
                    hidden_word_lst = change_hidden("x", word_lst, hidden_word_lst)
                if event.key == K_y:
                    yKey = True
                    hidden_word_lst = change_hidden("y", word_lst, hidden_word_lst)
                if event.key == K_z:
                    zKey = True
                    hidden_word_lst = change_hidden("z", word_lst, hidden_word_lst)

        n = 0
        for i in hidden_word_lst:
            if i != "":
                pass
            if i == "a":
                win.blit(aImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "b":
                win.blit(bImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "c":
                win.blit(cImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "d":
                win.blit(dImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "e":
                win.blit(eImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "f":
                win.blit(fImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "g":
                win.blit(gImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "h":
                win.blit(hImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "i":
                win.blit(iImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "j":
                win.blit(jImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "k":
                win.blit(kImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "l":
                win.blit(lImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "m":
                win.blit(mImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "n":
                win.blit(nImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "o":
                win.blit(oImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "p":
                win.blit(pImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "q":
                win.blit(qImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "r":
                win.blit(rImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "s":
                win.blit(sImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "t":
                win.blit(tImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "u":
                win.blit(uImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "w":
                win.blit(wImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "v":
                win.blit(vImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "x":
                win.blit(xImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            if i == "y":
                win.blit(yImage, (xpos + (dashpicsize[0] + space) * n, ypos-50))
            if i == "z":
                win.blit(zImage, (xpos + (dashpicsize[0] + space) * n, ypos-100))
            n+=1

        pygame.display.update()
        mainClock.tick(60)

def change_hidden(key, word_lst, hidden_word_lst):
    if key in word_lst:
        ind = [i for i in range(len(word_lst)) if key in word_lst[i]]
        print(ind)
        for i in ind:
            hidden_word_lst[i] = key
    return hidden_word_lst

def hangman_create_word(words):
    chosen_word = random.choice(words)
    chosen_word_lst = list(chosen_word)
    return [chosen_word, chosen_word_lst]

def check_if_in_word(key, word_lst):
    index = [i for i in range(len(word_lst)) if key in word_lst[i]]
    return index

main_menu()

