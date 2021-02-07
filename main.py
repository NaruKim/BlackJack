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

def givecard(n):
  n.append(random.choice(cards))

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

  if 11 in pcard and sum(pcard)>21:
    pcard.remove(11)
    pcard.append(1)
    print("Your Ace(11) has changed to Ace(1)")

  if 11 in dcard and sum(dcard)>21:
    dcard.remove(11)
    dcard.append(1)
    print("Your Ace(11) has changed to Ace(1)")

  print(f"Your cards: {pcard}")
  print(f"Dealer's cards: [{dcard[0]}, *]")

  if sum(pcard)==21:
    print("You win")
    chip=chip+bet*2
    print(f"Your chips remaining is: {chip}")
    bust=True

  if sum(pcard)>21:
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
      if sum(pcard)>sum(dcard):
        print(f"Your cards: {pcard}")
        print(f"Dealer's cards: {dcard}")
        print("You win")
      elif sum(dcard)>sum(pcard):
        print(f"Your cards: {pcard}")
        print(f"Dealer's cards: {dcard}")
        print("You lost")
      else:
        print(f"Your cards: {pcard}")
        print(f"Dealer's cards: {dcard}")
        print("Draw")
