from replit import clear
#HINT: You can call clear() to clear the output in the console.
more = True
bid_dict = {}
while more == True: 
  name = input("What is your name? ")
  price = int(input("What is the price? "))
  
  bid_dict[name] = price
  print(bid_dict)
  answer = input("Are there others who want to bid? Y/N\n")
  
  if answer.upper() == "Y":
    more = True
    clear()
  elif answer.lower() == "N":
    more = False
  else:
    more = False

max = [["Test", 0]]
for names in bid_dict:
  if bid_dict[names] > max[0][1]:
    max[0] = [names, bid_dict[names]]

print(f"{max[0][0]} won the bid!")
print(f"{max[0][1]} was the bid amount.")
              
