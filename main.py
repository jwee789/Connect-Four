import pygame
from Board import *
import time
import math

#colors we'll be using
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0, 255, 0)

WIDTH = 700
HEIGHT = 600

#initiate pygame/screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect Four')

def draw(board, turn):
    screen.fill(WHITE)
    #draw lines
    for i in range(100, WIDTH, 100):
        pygame.draw.line(screen, BLACK, (i, 0), (i, HEIGHT))
    for i in range(100, HEIGHT, 100):
        pygame.draw.line(screen, BLACK, (0, i), (WIDTH, i))
    #draw circles
    for row in range(6):
        for col in range(7):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (col*100+50, row*100+50), 40)
            if board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, (col*100+50, row*100+50), 40)
    #write who's turn it is
    if turn == 1:
        color = 'Red'
    else:
        color = 'Blue'
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(color + "'s Turn", True, BLACK)
    screen.blit(text, (0, 0))

font = pygame.font.Font('freesansbold.ttf', 100)

def drawWinner(winner):
    if winner == 1:
        wColor = 'Red'
    else:
        wColor = 'Blue'
    text = font.render(wColor + ' wins!', True, BLACK)
    screen.blit(text, text.get_rect(center = (WIDTH/2, HEIGHT/2)))
    pygame.display.update()
    time.sleep(2)

def drawTie():
    text = font.render('Tie Game', True, BLACK)
    screen.blit(text, text.get_rect(center = (WIDTH/2, HEIGHT/2)))
    pygame.display.update()
    time.sleep(2)

def main():
    game = Game()
    clock = pygame.time.Clock()
    
    playerTurn = 1

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mousePos = pygame.mouse.get_pos()
                if game.move(playerTurn, math.floor(mousePos[0]/100)):
                    #switch turns
                    if playerTurn == 1:
                        playerTurn = 2
                    else:
                        playerTurn = 1
        
        draw(game.board, playerTurn)
        pygame.display.update()
        
        if game.isTie():
            drawTie()
            running = False

        if game.getWinner() != 0:
            drawWinner(game.getWinner())
            running = False

if __name__ == '__main__':
    main()