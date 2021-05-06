matrix = [
    [2,3,5,11], #row index 0
    [2,6,7,13], #row index 1
    [9,4,1,80], #row index 2
    ]

#this below gives 3 because it counts row index from 0
total_rows = len(matrix) # so total_rows will = 3

#this below makes col start at 0 & end at range of row 0
#so the first row which is 0, has 4 elements
for col in range(0, len(matrix[0])): #makes range(0, 4)
  row = 0 #we want to increase the row index per each column check
  odds = [] #we start an empty list for all odd numbers found
  while row < total_rows: #while row is less than 3
    element = matrix[row][col] #assign the variable element this number
    if (element % 2 != 0):
      #if this number in such row & such col is not divisible by 2
      #then it is odd & we add it to our odds list we created per loop
      odds.append(element)
    row += 1
    #we incrase the row index because we want to check every column
    #at row index 0, and then at row index 1, and so on..
  print("Odd number in column", (col+1), "is", odds)
  #this prints all the elements/numbers that were odd collected in
  #the odds list  
