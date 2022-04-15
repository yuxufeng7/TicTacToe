import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND = (66,191,244)
BOARD_COLOR = (255,0,0)
CIRCLE_COLOR = (0,255,0)
CROSS_COLOR = (0,255,0)
TURN_COLOR = (0,0,0)
WINNER_COLOR = (0,0,0)
FPS = 60
stepCounter = 0
pieceSize = 35
piecePosition = [[(175, 175),(325, 175),(475, 175)],
                 [(175, 325),(325, 325),(475, 325)],
                 [(175, 475),(325, 475),(475, 475)]]
cellStates = [['idle', 'idle', 'idle'],
              ['idle', 'idle', 'idle'],
              ['idle', 'idle', 'idle']]
cellLen = 150
winner = 'None'
players = ['circle', 'cross']
whosTurn = random.choice(players)
gameState = 'start'

def isInBox(center, position):
    length = cellLen
    if (position[0]<center[0]+length/2) and (position[0]>center[0]-length/2) and (position[1]<center[1]+length/2) and (position[1]>center[1]-length/2):
        return True
    return False

def drawBoard():
    board = pygame.Surface(SIZE)
    board.fill(BACKGROUND)
    pygame.draw.line(board, BOARD_COLOR, (250, 100), (250, 550))
    pygame.draw.line(board, BOARD_COLOR, (400, 100), (400, 550))
    pygame.draw.line(board, BOARD_COLOR, (100, 250), (550, 250))
    pygame.draw.line(board, BOARD_COLOR, (100, 400), (550, 400))
    return board

def indicateTurn(whosTurn):
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    turnString = "Turn: {}".format(whosTurn.upper())
    turnIndcator = my_font.render(turnString, True, TURN_COLOR)
    return turnIndcator

def indicateWinner(winner):
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 50)
    winnerString = "{} Win(s)!".format(winner.upper())
    winnerIndcator = my_font.render(winnerString, True, WINNER_COLOR)
    return winnerIndcator

def placePiece(player, board, position):
    if player == players[0]:
        pygame.draw.circle(board, CIRCLE_COLOR, position, pieceSize, 3)
    if player == players[1]:
        pygame.draw.line(board, CROSS_COLOR, position,
                         (position[0]+pieceSize*math.sin(math.pi*1/4), position[1]+pieceSize*math.cos(math.pi*1/4)), 3)
        pygame.draw.line(board, CROSS_COLOR, position,
                         (position[0]+pieceSize*math.sin(math.pi*3/4), position[1]+pieceSize*math.cos(math.pi*3/4)), 3)
        pygame.draw.line(board, CROSS_COLOR, position,
                         (position[0]+pieceSize*math.sin(math.pi*5/4), position[1]+pieceSize*math.cos(math.pi*5/4)), 3)
        pygame.draw.line(board, CROSS_COLOR, position,
                         (position[0]+pieceSize*math.sin(math.pi*7/4), position[1]+pieceSize*math.cos(math.pi*7/4)), 3)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    global gameState
    global whosTurn
    global cellStates
    global stepCounter
    global winner
    clickPos = (0,0)

    running = True
    while running:
        clock.tick(FPS)

        if gameState == 'start':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    clickPos = pygame.mouse.get_pos()
                    if isInBox(piecePosition[0][0], clickPos):
                        if cellStates[0][0]=='idle':
                            cellStates[0][0] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[0][1], clickPos):
                        if cellStates[0][1]=='idle':
                            cellStates[0][1] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[0][2], clickPos):
                        if cellStates[0][2]=='idle':
                            cellStates[0][2] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[1][0], clickPos):
                        if cellStates[1][0]=='idle':
                            cellStates[1][0] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[1][1], clickPos):
                        if cellStates[1][1]=='idle':
                            cellStates[1][1] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[1][2], clickPos):
                        if cellStates[1][2]=='idle':
                            cellStates[1][2] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[2][0], clickPos):
                        if cellStates[2][0]=='idle':
                            cellStates[2][0] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[2][1], clickPos):
                        if cellStates[2][1]=='idle':
                            cellStates[2][1] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    elif isInBox(piecePosition[2][2], clickPos):
                        if cellStates[2][2]=='idle':
                            cellStates[2][2] = whosTurn
                            whosTurn = players[(players.index(whosTurn)+1)%2]
                            stepCounter += 1
                    # check gameover
                    for i in range(len(cellStates)):
                        if (cellStates[i][0] == cellStates[i][1]) and (cellStates[i][0] == cellStates[i][2]):
                            if cellStates[i][0] != 'idle':
                                winner = cellStates[i][0]
                                break
                    for j in range(len(cellStates[0])):
                        if (cellStates[0][j] == cellStates[1][j]) and (cellStates[0][j] == cellStates[2][j]):
                            if cellStates[0][j] != 'idle':
                                winner = cellStates[0][j]
                                break
                    if (cellStates[0][0] == cellStates[1][1]) and (cellStates[1][1] == cellStates[2][2]):
                        if cellStates[1][1] != 'idle':
                            winner =  cellStates[1][1]
                    if (cellStates[0][2] == cellStates[1][1]) and (cellStates[1][1] == cellStates[2][0]):
                        if cellStates[1][1] != 'idle':
                            winner =  cellStates[1][1]
                    if (winner == 'None') and (stepCounter == 9):
                        winner = 'both'

            board = drawBoard()
            for i in range(len(cellStates)):
                for j in range(len(cellStates[i])):
                    if cellStates[i][j] != 'idle':
                        placePiece(cellStates[i][j], board, piecePosition[i][j])
            turnIndcator = indicateTurn(whosTurn)
            screen.blit(board, (0, 0))
            screen.blit(turnIndcator, (575, 100))
            pygame.display.flip()

            if winner != 'None':
                gameState = 'end'
                clickRestart = False
                continue

        if gameState == 'end':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    clickRestart = True
            if clickRestart == True:
                    cellStates = [['idle', 'idle', 'idle'],
                                  ['idle', 'idle', 'idle'],
                                  ['idle', 'idle', 'idle']]
                    winner = 'None'
                    gameState = 'start'
                    stepCounter = 0
                    whosTurn = random.choice(players)
                    continue

            winnerIndcator = indicateWinner(winner)
            screen.fill(BACKGROUND)
            screen.blit(winnerIndcator, (250, 250))
            pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    main()