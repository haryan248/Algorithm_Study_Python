# import sys
# sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
# empty = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j]==0]

# def checkNumber(y, x):
#     checklist= [ x for x in range(1, 10)]
#     # 같은 행 열 검사
#     for i in range(9):
#         if sudoku[y][i] in checklist:
#             checklist.remove(sudoku[y][i])
#         if sudoku[i][x] in checklist:
#             checklist.remove(sudoku[i][x])
    
#     # 3 * 3 사각형 검사
#     # 시작 위치 조정
#     y = y//3
#     x = x//3
#     for i in range(y*3, (y+1)*3):
#         for j in range(x*3, (x+1)*3):
#             if sudoku[i][j] in checklist:
#                 checklist.remove(sudoku[i][j])
#     return checklist


# def Sudoku(count):
#     if count == len(empty):
#         for s in sudoku:
#             print(*s)
#         return
    
#     (i, j) = empty[count]
#     numbers = checkNumber(i, j)
#     for number in numbers:
#         sudoku[i][j] = number
#         Sudoku(count+1)
#         sudoku[i][j] = 0


# Sudoku(0)

import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
emptySpace = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def checkNumber(y, x):  # 빈칸에 들어갈 수 있는 숫자 후보 : 스도쿠 규칙에 따라 가로,세로,3x3 칸 내에 겹치는 숫자가 없어야 함
      numbers = [i for i in range(1, 10)]
      for k in range(9):
          # 행 검사
            if sudoku[y][k] in numbers:
                numbers.remove(sudoku[y][k])
            # 열 검사
            if sudoku[k][x] in numbers:
                numbers.remove(sudoku[k][x])
            # 3x3 사각형 검사
            if sudoku[(y//3) * 3 + (k // 3)][(x//3) * 3 + (k % 3)] in numbers:
                numbers.remove(sudoku[(y//3) * 3 + k // 3][(x//3) * 3 + k % 3] )
  
      return numbers


def Sudoku(count):
      if count == len(emptySpace):
            for i in range(9):
                print(' '.join(map(str,sudoku[i])))
            exit()
      
      (i, j) = emptySpace[count]
      candi = checkNumber(i, j)  # 빈칸에 들어갈 수 있는 숫자 후보
      for num in candi:
          sudoku[i][j] = num
          Sudoku(count+1)
          sudoku[i][j] = 0


Sudoku(0)
