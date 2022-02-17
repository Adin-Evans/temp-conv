def convert(su,eu,n):
  if su == "c" and eu == "k":
    print(str(n + 273) + " K" )
  elif su == "f" and eu == "c":
    print(str(5/9 * (n - 32)) + " C")
  elif su == "f" and eu == "k":
    print(str(((5/9) * (n - 32)) + 273) + " K")
  elif su == "c" and eu == "f":
    print(str((n * (9/5)) + 32) + " F")
  elif su == 'k' and eu == 'c':
    print(str(n - 273) + " C")
  elif su == 'k' and eu == 'f':
    print(str(((n-273)*(9/5))+32) + " F")
    
while True: 
  sUnit = (input("Starting Unit: F, C, or K: ")).lower()
  eUnit = (input("Ending Unit: F, C, or K: ")).lower()
  temp = (float(input("What is the degree: ")))
  if sUnit == 'k' and sUnit < 0:
    print("Can't have negative kelvin")
  convert(sUnit,eUnit,temp)