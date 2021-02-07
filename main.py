import random
import art

print(art.logo)

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
pcard=[]
dcard=[]
chip=100
hit=False

def bustplayer(n):
  if n>21:
    print (f"Player is bust")

def randcard():
  r1=random.randint(0,12)
  return cards[r1]

def givecard(n):
  n.append(randcard())

def cardsum(n):
  sum=0
  for i in n:
    sum+=i
  return sum

while chip>0:
  print(f"Your chips: {chip}")
  bust=False
  if hit==False:
    pcard=[]
    dcard=[]

    bet=int(input("How much do you place a bet?: "))
    if bet>chip:
      print("Your betting is over your chips.")
      continue
    else:
      givecard(pcard)
      givecard(dcard)
      givecard(pcard)
      givecard(dcard)

  chip-=bet
  print(f"Your chips remaining is: {chip}")

  print(f"Your cards: {pcard}")
  print(f"Dealer's cards: [{dcard[0]}, *]")

  if cardsum(pcard)==21:
    print("You win")
    chip=chip+bet*2
    print(f"Your chips remaining is: {chip}")
    bust=True

  if cardsum(pcard)>21:
    print("You bust")
    bust=True
    hit=False
  
  if bust==False:
    ask=input("Type 'y' if you want to hit, or type 'n' if you want to stay: ")
    if ask=='y':
      hit=True
      givecard(pcard)
    else: #Stay
      hit=False
      if cardsum(pcard)>cardsum(dcard):
        print(f"Your cards: {pcard}")
        print(f"Dealer's cards: {dcard}")
        print("You win")
      elif cardsum(dcard)>cardsum(pcard):
        print(f"Your cards: {pcard}")
        print(f"Dealer's cards: {dcard}")
        print("You lost")
      else:
        print(f"Your cards: {pcard}")
        print(f"Dealer's cards: {dcard}")
        print("Draw")
