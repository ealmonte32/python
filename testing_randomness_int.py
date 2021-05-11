#ealmonte32

import random

generate1 = 0
generate2 = 0
generate3 = 0
generate4 = 0
generate5 = 0
generate6 = 0

stop = 0
while stop < 1:
  generate1 = random.randint(1,1000)
  generate2 = random.randint(1,1000)
  generate3 = random.randint(1,1000)
  generate4 = random.randint(1,1000)
  generate5 = random.randint(1,1000)
  generate6 = random.randint(1,1000)
  
  print(generate1,generate2,generate3,generate4,generate5,generate6)
  
  if (generate1 == generate2) or (generate1 == generate3) or (generate1 == generate4) or (generate1 == generate5) or (generate1 == generate6):
    print("Match!")
    stop = 1
  elif (generate2 == generate3) or (generate2 == generate4) or (generate2 == generate5) or (generate2 == generate6):
    print("Match!")
    stop = 1
  elif (generate3 == generate4) or (generate3 == generate5) or (generate3 == generate6):
    print("Match!")
    stop = 1
  elif (generate4 == generate5) or (generate4 == generate6):
    print("Match!")
    stop = 1
  elif (generate5 == generate6):
    print("Match!")
    stop = 1
  else:
    print("no matches yet..\n")
#end