#list of list for board
board=[]


#make
#A1 B1 C1 D1 E1 F1 G1 H1 I1 J1    
#A2 B2 C2 D2 E2 F2 G2 H2 I2 J2    
#A3 B3 C3 D3 E3 F3 G3 H3 I3 J3    
#A4 B4 C4 D4 E4 F4 G4 H4 I4 J4    
#A5 B5 C5 D5 E5 F5 G5 H5 I5 J5    
#A6 B6 C6 D6 E6 F6 G6 H6 I6 J6    
#A7 B7 C7 D7 E7 F7 G7 H7 I7 J7    
#A8 B8 C8 D8 E8 F8 G8 H8 I8 J8    
#A9 B9 C9 D9 E9 F9 G9 H9 I9 J9    


for i in range(9):
   row=[]
   for j in range(9): #remove []
       row.append(".")
   board.append(row)


#convert empty space list into a string
#True is Rock turn, false is Peble turn
rock=True
while True:
   print("Board:")
   for row in board:
       print("".join(row))
   if rock:
       print("\nPlayer 1 turn, rock. \nFormat: Capital Letter Number Ex: A3 B6 I9")
       move=input("Where would you like to place your stone?:")
   else:
       print("\nPlayer 2 turn, pebble.\nFormat: Capital Letter Number Ex: A3 B6 I9")
       move=input("Where would you like to place your stone?:")


   
   if move == "stop":
       print("Game over")
       break
   letter=(move[0])
   num=int(move[1])
   #ord function convert letter to column #
   column=ord(letter) - ord('A')
   #num to row
   row=int(num) - 1
   #check empty
   if board[row][column]==".":
       if rock:
           board[row][column]="O"
       else:
           board[row][column]="o"
       #rock to pebble to pebble to rock
       rock=not rock
   else:
       print("Space taken")
#print game
print("\nFinal board: ")
for row in board:
   print("".join(row))
