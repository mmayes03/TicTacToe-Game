#!/usr/bin/env python
# coding: utf-8

# In[ ]:


k = ['k', '']
print(len(k[1])) #Used to determine if value already exists in grid


# In[ ]:


row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']


# In[ ]:


from IPython.display import clear_output
def display(row1, row2, row3): #Will always show updated rows no matter what, Note: Could possibly tweak to display differently
    clear_output() #will remove prev display of board
    print(' | ' + row1[0] + ' | ' + row1[1] + ' | ' +row1[2]+ ' | ')
    print(' ----------')
    print(' | '+ row2[0] + ' | ' + row2[1] + ' | ' +row2[2]+ ' | ')
    print(' -----------')
    print(' | ' + row3[0] + ' | ' + row3[1] + ' | ' +row3[2]+ ' | ')
    print(' -----------')


# In[ ]:


display(row1, row2, row3)


# In[ ]:


def reset_grid(a, b, c):
    a = ['', '', '']
    b = ['', '', '']
    c = ['', '', '']
    return a, b, c


# In[ ]:


def User_symbol(): #Should be done once for player one, returns user1 as x or o
    print("Hello player 1,\n")
    user1 = 'wrong'
    while user1 not in ['X', 'O']:
        user1 = input('Will you be X or O?: ').upper()
        
        if user1 not in ['X', 'O']:
            print('This is not X or O')
        else:
            break
    return user1 #could have established user2 here and return user1 and user2 based on user1's choice


# In[ ]:


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
            print("One of your values are not correct, try again.")
        else:
            
            if int(row) == 1:
                if len(row1[int(col)-1]) != 1:
                    turn+=1
                    row1[int(col)-1] = Mark
                   
                else:
                    print('There is already a value here')
                    row = 'wrong'
                    col = 'wrong'
            elif int(row) == 2:
                if len(row2[int(col)-1]) != 1:
                    turn+=1
                    row2[int(col)-1] = Mark
                    
                else:
                    print('There is already a value here')
                    row = 'wrong'
                    col = 'wrong'
            elif int(row) == 3:
                if len(row3[int(col)-1]) != 1:
                    turn+=1
                    row3[int(col) - 1] = Mark
                   
                else:
                    print('There is already a value here')
                    row = 'wrong'
                    col = 'wrong'
                    
    return row1, row2, row3
        


# In[ ]:


def winner(row1, row2, row3, turn):
    #This will check if each row has a winner
    if (row1==['X','X','X'] or row2==['X','X','X'] or row3==['X','X','X']) or (row1 == ['O','O','O'] or row2 ==['O','O','O'] or row3==['O','O','O']):
        display(row1, row2, row3) #Display board to show winning move
        if turn%2 == 0:
            print("Player 2 has Won!")
        elif turn%2 != 0:
            print("Player 1 has won")
        #print('You have won!')
        return True
        
    #This will check if column 1 has a winner
    elif (row1[0]=='X' and row2[0]=='X' and row3[0] =='X') or (row1[0]=='O' and row2[0]=='O' and row3[0] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("Player 2 has Won!")
        elif turn%2 != 0:
            print("Player 1 has won")
        #print('You have won!')
        return True
        
    #This will check if column 2 has a winner
    elif (row1[1]== 'X' and row2[1]== 'X' and row3[1] == 'X') or (row1[1]=='O' and row2[1]=='O' and row3[1] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("Player 2 has Won!")
        elif turn%2 != 0:
            print("Player 1 has won")
        #print('You have won!')
        return True
        
    #This will check if column 3 has a winner
    elif (row1[2]== 'X' and row2[2]== 'X' and row3[2] == 'X') or (row1[2]=='O' and row2[2]=='O' and row3[2] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("Player 2 has Won!")
        elif turn%2 != 0:
            print("Player 1 has won")
        #print('You have won!')
        return True
        
    #This will check the first diagonal option
    elif (row1[0]== 'X' and row2[1]== 'X' and row3[2] == 'X') or (row1[0]=='O' and row2[1]=='O' and row3[2] =='O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("Player 2 has Won!")
        elif turn%2 != 0:
            print("Player 1 has won")
        #print('You have won!')
        return True
        
    #This will check the second diagonal option
    elif (row1[2]== 'X' and row2[1]== 'X' and row3[0] == 'X') or (row1[2]=='O' and row2[1]=='O' and row3[0] == 'O'):
        display(row1, row2, row3)
        if turn%2 == 0:
            print("Player 2 has Won!")
        elif turn%2 != 0:
            print("Player 1 has won")
        #print('You have won!')
        return True
        
    #This will determine if there is a tie. The 'all' method checks to see if each element in the list has a vale. '' = False
    elif ((all(row1) == True) and (all(row2) == True) and (all(row3) == True)):
        display(row1, row2, row3)
        print("It is a Tie!")
        return True
        
   
    else:
        #Game is not finished and there is no winner, return False
        return False
        
    


# In[ ]:


def continue_game2(): #Check to see is user wants to play again. returns boolian
    Play_button = 'wrong'
    restart_game = False
    
    while Play_button not in ['yes', 'no']:
        Play_button = input("Do you want to play again? ").lower()
        if Play_button not in ['yes', 'no']:
            print('Your choice does not seem to be yes or no')
        else:
            break
    if Play_button == 'yes':
        #User_symbol() #Change this to be the option to restart loop
        #reset_grid()
        restart_game = True
            
    elif Play_button == 'no':
        print('No more games! Thanks for Playing!')
        restart_game = False
   
    return restart_game


# In[ ]:


# Mayes Tic tac toe game, created to only take positions rather than X and O inputs. 
row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']
#Set turn at 1 to indicate who goes first
turn = 1
#Codition to continue loop/play game
play_game = True 
#Define initial users position Note: can set up to randomly you choose P1 or P2 and feed the rand loop to the position choice
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


#Validating User input


# In[ ]:


def user_choice():
    
    choice = 'Wrong'
    
    
    while choice.isdigit() == False:
        
        choice = input("Please enter a number (0-10): ")
        
        if choice.isdigit() == False:
            print("Sorry, that is not a digit: ")
            
        
    
    return int(choice)


# In[ ]:


user_choice()


# In[ ]:


result  = 'Wrong Value'


# In[ ]:


acceptable_values = [0,1,2]


# In[ ]:


result not in acceptable_values


# In[ ]:


def user_choice2():
    #Variables
    
    #initial 
    choice = 'Wrong'
    
    acceptable_range = range(0,10)
    within_range = False
    
    #Two conditions to check
    #digit or within range == false
    while choice.isdigit() == False or within_range == False:
        
        choice = input("Please enter a number (0-10): ")
        #Digit check
        if choice.isdigit() == False:
            print("Sorry, that is not a digit: ")
        #Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
        
    
    return int(choice)


# In[ ]:


user_choice2()


# In[ ]:


#Simple user interactive experience





game_list = [0,1,2]


# In[ ]:


def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


# In[ ]:


display_game(game_list)


# In[ ]:


def position_choice():
    choice = 'WRONG'
    
    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2): ")
        
        if choice not in ['0', '1', '2']:
            print("Sorry invalid choice!")
            
    return int(choice)


# In[ ]:


position_choice()


# In[ ]:


def replacement_choice(game_list, position):
    
    user_placement = input("Type a string to place a position: ")
    
    game_list[position] = user_placement
    
    return game_list


# In[ ]:


replacement_choice(game_list, position_choice())


# In[ ]:


def gameon_choice(): #Use Choice to maintane while loop
    choice = 'WRONG'
    
    while choice not in ['Y','N']:
        choice = input("Keep playing? (Y or N)")
        
        if choice not in ['Y','N']:
            print("Sorry, I don't understand. Please choose Y or N")
            
    if choice == 'Y':
        
        return True
    else:
        return False


# In[ ]:


gameon_choice()


# In[ ]:


game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list, position)
    
    display_game(game_list)
    
    game_on = gameon_choice()
    
    if game_on == True:
        game_list = [0,1,2]


# In[ ]:





# In[ ]:




