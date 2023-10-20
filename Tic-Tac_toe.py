#!/usr/bin/env python
# coding: utf-8

# In[72]:


#Tic-Tac-Toe Game Based on Rows and Columns
from IPython.display import clear_output
import random


# In[73]:


def display(row1, row2, row3): #Will always show updated rows no matter what, Note: Could possibly tweak to display differently
    clear_output() #will remove prev display of board
    print(' | ' + row1[0] + ' | ' + row1[1] + ' | ' +row1[2]+ ' | ')
    print(' ----------')
    print(' | '+ row2[0] + ' | ' + row2[1] + ' | ' +row2[2]+ ' | ')
    print(' -----------')
    print(' | ' + row3[0] + ' | ' + row3[1] + ' | ' +row3[2]+ ' | ')


# In[74]:


def reset_grid(a, b, c):
    a = ['', '', '']
    b = ['', '', '']
    c = ['', '', '']
    return a, b, c


# In[75]:


def User_symbol(): #Should be done once for player one, returns user1 as x or o
    print("Hello player 1,\n")
    user1 = 'wrong'
    while user1 not in ['X', 'O']:
        user1 = input('Will you be X or O?: ').upper()
        
        if user1 not in ['X', 'O']:
            print("WRONG INPUT! The value you choose must be an 'X' or an 'O'")
        else:
            break
    return user1 #could have established user2 here and return user1 and user2 based on user1's choice


# In[76]:


def User_position(row1, row2, row3, Mark,turn): #will control positions picked on grid and only output new positions
    print("Pick a position on the grid by row and column!\n")
    display(row1, row2, row3) #can include in final loop to show results
    row = 'wrong'
    col = 'wrong'
    
    while row and col not in ['1', '2', '3']:
        if turn%2 == 0:
            print("Player 2's turn")
        elif turn%2 != 0:
            print("Player 1's turn")
        row = input("What row do you choose? ")
        col = input("What column do you choose? ")
        if row and col not in ['1', '2', '3']:
            print("Row and Column Values must be '1','2', or '3. Try again.\n")
        else:
            
            if int(row) == 1:
                if len(row1[int(col)-1]) != 1:
                    turn+=1
                    row1[int(col)-1] = Mark
                   
                else:
                    print('There is already a value here. Try a different Row and Column.\n')
                    row = 'wrong'
                    col = 'wrong'
            elif int(row) == 2:
                if len(row2[int(col)-1]) != 1:
                    turn+=1
                    row2[int(col)-1] = Mark
                    
                else:
                    print('There is already a value here. Try a different Row and Column.\n')
                    row = 'wrong'
                    col = 'wrong'
            elif int(row) == 3:
                if len(row3[int(col)-1]) != 1:
                    turn+=1
                    row3[int(col) - 1] = Mark
                   
                else:
                    print('There is already a value here. Try a different Row and Column.\n')
                    row = 'wrong'
                    col = 'wrong'
                    
    return row1, row2, row3


# In[77]:


def winner(row1, row2, row3, turn):
    #This will check if each row has a winner
    if (row1==['X','X','X'] or row2==['X','X','X'] or row3==['X','X','X']) or (row1 == ['O','O','O'] or row2 ==['O','O','O'] or row3==['O','O','O']):
        display(row1, row2, row3) #Display board to show winning move
        if turn%2 == 0:
            print("PLAYER 2 WINS!")
        elif turn%2 != 0:
            print("PLAYER 1 WINS!")
        #print('You have won!')
        return True
        
    #This will check if column 1 has a winner
    elif (row1[0]=='X' and row2[0]=='X' and row3[0] =='X') or (row1[0]=='O' and row2[0]=='O' and row3[0] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("PLAYER 2 WINS!")
        elif turn%2 != 0:
            print("PLAYER 1 WINS!")
        #print('You have won!')
        return True
        
    #This will check if column 2 has a winner
    elif (row1[1]== 'X' and row2[1]== 'X' and row3[1] == 'X') or (row1[1]=='O' and row2[1]=='O' and row3[1] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("PLAYER 2 WINS!")
        elif turn%2 != 0:
            print("PLAYER 1 WINS!")
        #print('You have won!')
        return True
        
    #This will check if column 3 has a winner
    elif (row1[2]== 'X' and row2[2]== 'X' and row3[2] == 'X') or (row1[2]=='O' and row2[2]=='O' and row3[2] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("PLAYER 2 WINS!")
        elif turn%2 != 0:
            print("PLAYER 1 WINS!")
        #print('You have won!')
        return True
        
    #This will check the first diagonal option
    elif (row1[0]== 'X' and row2[1]== 'X' and row3[2] == 'X') or (row1[0]=='O' and row2[1]=='O' and row3[2] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("PLAYER 2 WINS!")
        elif turn%2 != 0:
            print("PLAYER 1 WINS!")
        #print('You have won!')
        return True
        
    #This will check the second diagonal option
    elif (row1[2]== 'X' and row2[1]== 'X' and row3[0] == 'X') or (row1[2]=='O' and row2[1]=='O' and row3[0] == 'O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("PLAYER 2 WINS!")
        elif turn%2 != 0:
            print("PLAYER 1 WINS!")
        #print('You have won!')
        return True
        
    #This will determine if there is a tie. The 'all' method checks to see if each element in the list has a vale. '' = False
    elif ((all(row1) == True) and (all(row2) == True) and (all(row3) == True)):
        display(row1, row2, row3)
        print("It's a TIE!")
        return True
        
   
    else:
        #Game is not finished and there is no winner, return False
        return False


# In[78]:


def continue_game2(): #Check to see is user wants to play again. returns boolian
    Play_button = 'wrong'
    restart_game = False
    
    while Play_button not in ['yes', 'no']:
        Play_button = input("Would you like to play again?\n").lower()
        if Play_button not in ['yes', 'no']:
            print('Your INPUT must be yes or no. Try again.')
        else:
            break
    if Play_button == 'yes':
        #User_symbol() #Change this to be the option to restart loop
        #reset_grid()
        restart_game = True
            
    elif Play_button == 'no':
        print('GAME OVER! Thanks for Playing!')
        restart_game = False
   
    return restart_game


# In[79]:


def who_goes_first():
    player_list = ['heads','tails']
    who_goes = random.choice(player_list)
    p_choise = ''
    while p_choise not in player_list:
        p_choise = input("Pick 'Heads' or 'Tails' to determine which player you will be.").lower()
        if p_choise not in player_list:
            print("Your INPUT must be 'Heads' or 'Tails'. Try again.\n")
        else:
            break
    if who_goes == 'heads':
        print("You will Go first as Player1!\n")
    else:
        print("You will Go Second as Player2!\n")


# In[71]:


# Mayes Tic tac toe game, created to only take X and O Positions. 
row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']
#Set turn at 1 to Keep track of who goes
turn = 1
#Condition to continue loop/play game
play_game = True 
#Who goes First 
who_goes_first()
#Define Players
player1 = User_symbol()
player2 = ''

while play_game: #can substitute with True and use break instead
    if player1 == 'X': #Set conditions for user2 in while loop
        player2 = 'O'
    elif player1 == 'O':
        player2 ='X'
    #print("\nPlayer one's turn: ")
    one = User_position(row1, row2, row3, player1, turn) #Get player one's position, symbol, and current turn
    A = winner(row1, row2, row3,turn) #Check if user 1 has won
    turn += 1 #Update turn after the winner is checked
    
    #---------------------------------------------------------------------#
    #restart_game = continue_game(A) #If they have won, run restart, if not continue to play game
    if A == True:
        #not here, but can display board here instead
        restart_game = continue_game2()
        if restart_game == True:
            #Reset Board, reset player 1's choice, restart loop
            who_goes_first()
            row1, row2, row3 = reset_grid(row1, row2, row3)
            player1 = User_symbol()
            turn = 1 #reset turn if player wants to play again
            play_game = True
        else:
            play_game = False
    else:
        #continue game
        play_game = True
        
    #-----set up for player two to choose position. Could possibly do without 'if A != True', but this condition prevents player2 from going when player1 no longer wants to play
    if A != True:
        #print("\nPlayer two's turn: ")
        two = User_position(row1, row2, row3, player2, turn) #Get Player two's position
        B = winner(row1, row2, row3,turn)
        turn += 1
        if B == True:
            restart_game = continue_game2()
            if restart_game == True:
                #Reset Board, reset player 1's choice, restart loop
                who_goes_first()
                row1, row2, row3 = reset_grid(row1, row2, row3)
                player1 = User_symbol()
                turn = 1
                play_game = True
            else:
                play_game = False
        else:
            #Continue Game
            play_game = True
            


# In[ ]:




