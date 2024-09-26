
def q1():
  #Write Assignment code here
  bool1 = (True)
  bool2 = (False)
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here
  num = input("Enter an interger: ")
  num = int(num)
  bool = num != 0
  print(bool)

def q3():
  #Write Assignment code here
  num1 = input("Enter a number: ")
  numi = float(num1)
  bool1 = (num1 > -1 and num1 < 11)
  print(bool1)

def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink")
  bool2 = (not food == "pizza" or not drink == "pop")
  print(bool2)

def q5():
  #Write Assignment code here
  num3 = input("Enter an integer: ")
  num3 = int(num3)
  bool3 = not num3%2
  print(f"The integer {num3} is {bool3}.")

#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''