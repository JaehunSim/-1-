# -*- coding: utf-8 -*-
boardList = [["CCBDE", "AAADE", "AAABF", "CCBBF"],	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]

def make_board(m,n):
    emptyBoard = [[" " for y in range(n)] for x in range(m)]
    return emptyBoard

def input_board(emptyBoard,board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            emptyBoard[i][j] = board[i][j]
    return emptyBoard

def delete_func(m,n,initial):
    deleteIndex = [0]
    count = 0
    
    while(len(deleteIndex) != 0):
        deleteIndex = []
        for i in range(m-1):
            for j in range(n-1):
                if initial[i][j] == " ":
                    break
                if initial[i][j] == initial[i][j+1]:
                    if initial[i][j] == initial[i+1][j]:
                        if initial[i][j] == initial[i+1][j+1]:
                            deleteIndex.append([i,j])
        for i in deleteIndex:
            if initial[i[0]][i[1]] == " ":
                count += -1
            if initial[i[0]+1][i[1]] == " ":
                count += -1
            if initial[i[0]][i[1]+1] == " ":
                count += -1
            if initial[i[0]+1][i[1]+1] == " ":
                count += -1
            initial[i[0]][i[1]], initial[i[0]+1][i[1]], initial[i[0]][i[1]+1], initial[i[0]+1][i[1]+1] = " "," "," "," "
            count += 4
        
        for i in range(m-1):
            for j in range(n):
                if initial[i+1][j] == " ":
                    initial[i][j], initial[i+1][j] = initial[i+1][j], initial[i][j]
                    
    return initial,count

def block_remove_count(board):
    m=len(board)
    n=len(board[0])
    emptyBoard = make_board(m,n)
    initial = input_board(emptyBoard,board)
    
    result,count = delete_func(m,n,initial)
    
    return count
    
w = block_remove_count(boardList[1])