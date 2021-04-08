from pprint import pprint
from random import randint


def printing_board(board):
    numbers = [f" {i} " for i in range(len(board))]
    print(" ","".join(numbers))

    for i in range(len(board)):
        print(i,"".join(board[i]))

def printing_board_after_game(board, cords_of_bomb):
    numbers = [f" {i} " for i in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if [i,j] in cords_of_bomb:
                board[i][j] = "|*|"

    print(" ","".join(numbers))

    for i in range(len(board)):
        print(i,"".join(board[i]))
        
    
    
def board_creator(size):    #tworzy plansze z roznymi trybami
    if size == "easy":
        board = [["|+|" for i in range(3)] for i in range(3)]
        return board
    if size == "mid":
        board = [["|+|" for i in range(4)] for i in range(4)]
        return board
    if size == "hard":
        board = [["|+|" for i in range(5)] for i in range(5)]
        return board


def planting_a_bomb(board, cords_of_bomb):      #funkcja generuje jedna 
                                                #bombe gdzies na planszy
    random_range = len(board)
    a = randint(0,random_range-1)   #losowe miejsce na planszy
    b = randint(0,random_range-1)

    if [a,b] in cords_of_bomb:               #jesli juz sa takie koordynaty to wywolaj
        planting_a_bomb(board, cords_of_bomb)   #jeszcze raz te funkcje
    else:
        cords_of_bomb.append([a,b])         #jesli takich nie ma to po prostu je dodaj
       # print("Bomba jest w :", a, b)
    return a,b


def is_there_any_hidden_box(board, cords_of_bomb):  #funkcja odpowiedzialna za
    is_there = False                                #sprawdzanie czy zostaly jeszcze
    amount_of_plus = 0                              #jakies nieokryte pola bez bomb        
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "|+|":

                amount_of_plus += 1     #licznik zlicza ile jest nieokrytych pol
                
    
    if amount_of_plus > len(cords_of_bomb): #jesli sa jeszcze jakies takie pola
        is_there = True
    elif amount_of_plus <= len(cords_of_bomb):  #jesli nie ma juz takich pol
        is_there = False

    return is_there
    

def game(board, cords_of_bomb, used):
    
    bomb_finded = False         #zmienna ktora sprawdza czy znaleziono bombe
    you_won = False             #zmienna sprawdza czy wygrales
    used = 0

    a = cords_of_bomb[0][0]        #koordynaty bomby
    b = cords_of_bomb[0][1]
    

    which_one = list(input("Które pole wybierasz? :"))
    print(which_one)
    if len(which_one) == 2:
        first = int(which_one[0])   #koordynaty wybrane
        sec = int(which_one[1])
    
    
        if first >= len(board) or first < 0 or sec >= len(board) or sec < 0:   #niepoprawne pole
            print(f"Zły indeks, wybieraj z zakresu: (0-{len(board)-1})")
            used = 1 #nie podbije licznika
            
        else:
            
            for i in cords_of_bomb:
                if first == i[0] and sec == i[1]:        # znaleziono bombe
                    board[first][sec] = "|*|"
                    bomb_finded = True

            if board[first][sec] == "|-|":    # zajete pole
                print("To pole jest już odkryte")
                used = 1
            
            elif board[first][sec] == "|+|":   # wybranie wolnego pola
                print("Try another one")
                board[first][sec] = "|-|"
                


            if is_there_any_hidden_box(board, cords_of_bomb) == False:  
                you_won = True                   #odpala funkcje ktora sprawdza ile zostalo
                                                #jeszcze nieodkrytych pol bez bomb
    else:
        print("Invalid amount of coordinates")
        used = 1

    return  used, bomb_finded, you_won         
                              

def endgame_lose():              # przegrana
    print("Gretulacje przegrales!")
  
def endgame_win():               # wygrana
    print("Gretulacje wygrales!")
    





#----------------------------Main-------------------------------#
print(""" 
      ##Wybierz wiekosc planszy:##
      #        1 = 3x3           #
      #        2 = 4x4           #
      #        3 = 5x5           #
      # ######################## #
""")

mode = int(input(""))
if mode == 1:            # tworzenie planszy
    board = board_creator("easy")
elif mode == 2:
    board = board_creator("mid")
else:
    board = board_creator("mid")

print(""" 
      ##Wybierz tryb gry:##
      #    1 = Easy(2)    #
      #    2 = Medium(4)  #
      #    3 = Hard(6)    #
      #    4 = Random     #
      # ###################
""")

level = int(input())
if level == 1:            # tilosc bomb
    amount_of_bombs = 2
elif level == 2:
    amount_of_bombs = 4
elif level == 3:
    amount_of_bombs = 6
else:
    amount_of_bombs = (len(board) * (len(board)-2))


   
print(""" 
      ###### Instrukcja ######
      #  Numery pól podawaj  #
      #  po prostu po kolei  #
      #  bez spacji i        #
      #  enteru, np: 01      #
      #  i raz enter oznacza #
      #  pole [0, 1]         #
      ########################
""")

cords_of_bomb = list()  #pozycje bomb
pack_of_info = list()   #infromacje zwracane z game 
                        #0-used, 1-bomb_finded, 2-you_won

licznik = 0
used = 0        #czy zwiekszyc licznik
you_won = False #czy wygrales



for i in range(randint(2, amount_of_bombs)):     #losowa liczba bomb
    planting_a_bomb(board, cords_of_bomb)



while(1):
    printing_board(board)       # rysuje plansze w terminalu
    pack_of_info = game(board, cords_of_bomb, used)     #wywoluje "gre"

    

    
    used = int(pack_of_info[0])     # sprawdza czy stalo sie tam cos takiego
    if used != 1:                   # przez co nie trzeba podnosic licznika
        licznik = licznik + 1

    print(f"Ilość wybranych: {licznik}")    #wypisuje ile juz pol wybralismy
    
    used = 0                # zeruje zmienna od licznika

    you_won = pack_of_info[2]           # koniec gry - wygrana
    if you_won == True:
        printing_board_after_game(board, cords_of_bomb)     #wypisuje plansze z bombami
        endgame_win()
        print(f"Wybrano: {licznik}")
        break


    if(pack_of_info[1] == True):        # koniec gry - przegrana
        printing_board_after_game(board, cords_of_bomb)     #wypisuje plansze z bombami
        endgame_lose()
        print(f"Po {licznik} próbach")
        break
    
    
    


