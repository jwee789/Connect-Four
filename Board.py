import numpy as np
from copy import copy, deepcopy
import random

class Game:
    #0 will represent empty
    #1 will represent player 1
    #2 will represent player 2

    def __init__(self):
        self.board = np.zeros((6, 7))

    def move(self, playerNum, col):
        #check if column completely filled
        if self.board[0][col] != 0:
            return False
        #start at bottom and check for the first empty grid in the column, place it there
        row = 5
        while (self.board[row][col] != 0):
            row -= 1
        self.board[row][col] = playerNum
        return True
    
    def isTie(self):
        for r in range(6):
            for c in range(7):
                if self.board[r][c] == 0:
                    return False
        return True
        
    def getWinner(self):
        for r in range(3):
            for c in range(4):
                if self.board[r][c] != 0:
                    if self.fourDown(r,c) == 4 or self.fourRight(r,c) == 4 or self.negDiagonal(r,c) == 4:
                        return self.board[r][c]
        for r in range(3, 6):
            for c in range(4):
                if self.board[r][c] != 0 and self.posDiagonal(r, c) == 4:
                    return self.board[r][c]
        for r in range(3, 6):
            for c in range(4):
                if self.board[r][c] != 0 and self.fourRight(r,c) == 4:
                    return self.board[r][c]
        for r in range(3):
                for c in range(4, 7):
                    if self.board[r][c] != 0 and self.fourDown(r,c) == 4:
                        return self.board[r][c]
        return 0

    def fourDown(self, row, col):
        count = 1;
        if self.board[row][col] == self.board[row+1][col]:
            count += 1
        if self.board[row][col] == self.board[row+2][col]:
            count += 1
        if self.board[row][col] == self.board[row+3][col]:
            count += 1
        return count
    
    def fourRight(self, row, col):
        count = 1;
        if self.board[row][col] == self.board[row][col+1]:
            count += 1
        if self.board[row][col] == self.board[row][col+2]:
            count += 1
        if self.board[row][col] == self.board[row][col+3]:
            count += 1
        return count
    
    def negDiagonal(self, row, col):
        count = 1;
        if self.board[row][col] == self.board[row+1][col+1]:
            count += 1
        if self.board[row][col] == self.board[row+2][col+2]:
            count += 1
        if self.board[row][col] == self.board[row+3][col+3]:
            count += 1
        return count

    def posDiagonal(self, row, col):
        count = 1;
        if self.board[row][col] == self.board[row-1][col+1]:
            count += 1
        if self.board[row][col] == self.board[row-2][col+2]:
            count += 1
        if self.board[row][col] == self.board[row-3][col+3]:
            count += 1
        return count

#ai portion
    def evaluateBoard(self, player):
        player2 = 1
        if player == 1:
            player2 == 2

        score = 0
        if (self.getFours() == player):
            score += 1000
        if (self.getFours() == player2):
            score -= 1000
        score += self.getThrees(player) * 100
        score -= self.getThrees(player2) * 100
        score += self.getThrees(player) * 10
        score -= self.getThrees(player2) * 10
        score += self.centerPieces(player)

    

    

        
