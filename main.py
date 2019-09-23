
##from menu import *
from dealer import Dealer
import pickle
import random
import time

deck = []
dealt = []
money = 100
turn = 0

def create(money):
    for x in range(2):
        dealer = Dealer()
        dealer.add_player("test")
    #    dealer.add_player("test2")
        dealer.deal_cards()
        for player in dealer.players:
            deck.append([dealer.inspect_players()])

    deal(money, deck, turn)

def deal(money, deck, turn):
    if turn >= 30:
        print ("Sorry.. You lost")
        quit()
        
    turn = turn + 1
    a = random.choice(deck)
    b = random.choice(deck)
    
    if a in dealt:
        a = random.choice(deck)
    else:
        dealt.append(a)
        
    if b in dealt:
        b = random.choice(deck)
    else:
        dealt.append(b)
        
    result = a + b

 #   recieve(money, result, turn)
    
    dealt.append(result)
    recieve(money, result, turn)

        
def recieve(money, result, turn):
    h1 = result[0]
    print ("Turn", turn)
    print ("You have", '$',money)
    sub_dict = {14: 'A', 13: 'K', 12: 'Q', 11: 'J'}
    g = []
    print (h1[1])
    for t in h1[1]:
        a, b = t
        if a in sub_dict:
            a = sub_dict[a]
        if b in sub_dict:
            b = sub_dict[b]
        g.append((a,b))
    
    bonus_price(money, result, turn)

def bonus_price(money, result, turn):
    h1 = result[0]
    if h1[0] == "EMPEROR STRAIGHT FLUSH":
        money = money + 200
        print ("CONGRATULATIONS! YOU GOT THE HIGHEST HAND IN AZ POKER!!! YOU WIN!!!")
        conclusion(money, turn)
    elif h1[0] == "ROYAL STRAIGHT FLUSH":
        money = money + 150
        print ("CONGRATULATIONS! YOU GOT ROYAL STRAIGHT FLUSH!!! YOU EARN EXTRA $150$ AS A BONUS!!!")
        decision(money, result, turn)
    elif h1[0] == "BACK STRAIGHT FLUSH":
        money = money + 120
        print ("CONGRATULATIONS! YOU GOT BACK STRAIGHT FLUSH!!! YOU EARN EXTRA $120$ AS A BONUS!!!")
        decision(money, result, turn)
    elif h1[0] == "FIVE OF A KIND":
        money = money + 100
        print ("CONGRATULATIONS! YOU GOT FIVE OF A KIND!!! YOU EARN EXTRA $100$ AS A BONUS!!!")
        decision(money, result, turn)
    elif h1[0] == "STRAIGHT FLUSH":
        money = money + 80
        print ("CONGRATULATIONS! YOU GOT STRAIGHT FLUSH!!! YOU EARN EXTRA $80$ AS A BONUS!!!")
        decision(money, result, turn)
    elif h1[0] == "FLUSH":
        money = money + 40
        print ("CONGRATULATIONS! YOU GOT FLUSH!!! YOU EARN EXTRA $60$ AS A BONUS!!!")
        decision(money, result, turn)
    elif h1[0] == "FULL HOUSE":
        money = money + 60
        print ("CONGRATULATIONS! YOU GOT FULL HOUSE!!! YOU EARN EXTRA $40$ AS A BONUS!!!")
        decision(money, result, turn)
    elif h1[0] == "FOUR OF A KIND":
        money = money + 20
        print ("CONGRATULATIONS! YOU GOT FOUR OF A KIND!!! YOU EARN EXTRA $20$ AS A BONUS!!!")
        decision(money, result, turn)
    else:
        decision(money, result, turn)
        
def decision(money, result, turn):
    print ('')
    while True:
        try:
            call = int(input("Would you like to continue with this hand? Yes:1, No:2 : "))
            
        except ValueError:
            print("You have entered an incorrect number, please try again")
            time.sleep(2)
            continue
    
        if call == 1:
            bet(money, result, turn)

        elif call ==2:
            money = money - 5
            print ('')
            deal(money, deck, turn)
        
        else:
            print ("You have entered an incorrect number, please try again")
            continue
        break


def bet(money, result, turn):
    print ('')

    bet = int(input("Place your bet. Min:10, Max: {} : ".format(money)))

    if bet > money:
        print ("You have betted more than you own, try again")
        print ('')
        bet(money, result, turn)

    elif bet < 10:
        print ("You have to bet at least the minimum, try again")
        print ('')
        bet(money, result, turn)
       
    else:
        dealer_strategy(money, result, bet, turn)


def dealer_strategy(money, result, bet, turn):
    h1 = result[0]
    h2 = result[0]
    percentage = (random.sample(range(1,10), (1)))[0]
    if percentage >= 6:
        if h2[2] > h1[2]:
            compare_hands(money, result, bet, turn)
        else:               
            if h2[0] == "FLUSH" or h2[0] == "FULL HOUSE" or h2[0] == "FIVE OF A KIND" or h2[0] == "STRAIGHT FLUSH" or h2[0] == "BACK STRAIGHT FLUSH" or h2[0] == "ROYAL STRAIGHT FLUSH" or h2[0] == "EMPEROR STRAIGHT FLUSH":
                compare_hands(money, result, bet, turn)
            
            elif h2[0] == "FOUR OF A KIND":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 1:
                    compare_hands(money, result, bet, turn)
                else:
                    pass
            elif h2[0] == "HOUSE":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 2:
                    compare_hands(money, result, bet, turn)
                else:
                    pass
            elif h2[0] == "STRAIGHT" or h2[0] == "BACK STRAIGHT" or h2[0] == "ROYAL STRAIGHT":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 2:
                    compare_hands(money, result, bet, turn)
                else:
                    pass
            elif h2[0] == "THREE OF A KIND":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 2:
                    compare_hands(money, result, bet, turn)
                else:
                    pass
            elif h2[0] == "TWO PAIR":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 2:
                    compare_hands(money, result, bet, turn)
                else:
                    pass
            elif h2[0] == "ONE PAIR":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 5:
                    compare_hands(money, result, bet, turn)
                else:
                    pass
            elif h2[0] == "HIGH CARD":
                percentage = (random.sample(range(1,10), (1)))[0]
                if percentage >= 8:
                    compare_hands(money, result, bet, turn)
                else:
                    pass           
            else:
                money = money + 5
                print ("Dealer folds")
                print ("")
                deal(money, deck, turn) 
    else:
        if h2[0] == "FLUSH" or h2[0] == "FULL HOUSE" or h2[0] == "FIVE OF A KIND" or h2[0] == "STRAIGHT FLUSH" or h2[0] == "BACK STRAIGHT FLUSH" or h2[0] == "ROYAL STRAIGHT FLUSH" or h2[0] == "EMPEROR STRAIGHT FLUSH":
            compare_hands(money, result, bet, turn)
        elif h2[0] == "FOUR OF A KIND":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 1:
                compare_hands(money, result, bet, turn)
            else:
                pass
        elif h2[0] == "HOUSE":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 2:
                compare_hands(money, result, bet, turn)
            else:
                pass
        elif h2[0] == "STRAIGHT" or h2[0] == "BACK STRAIGHT" or h2[0] == "ROYAL STRAIGHT":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 2:
                compare_hands(money, result, bet, turn)
            else:
                pass
        elif h2[0] == "THREE OF A KIND":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 2:
                compare_hands(money, result, bet, turn)
            else:
                pass
        elif h2[0] == "TWO PAIR":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 2:
                compare_hands(money, result, bet, turn)
            else:
                pass
        elif h2[0] == "ONE PAIR":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 5:
                compare_hands(money, result, bet, turn)
            else:
                pass
        elif h2[0] == "HIGH CARD":
            percentage = (random.sample(range(1,10), (1)))[0]
            if percentage >= 8:
                compare_hands(money, result, bet, turn)
            else:
                pass           
        else:
            money = money + 5
            print ("Dealer folds")
            print ("")
            deal(money, deck, turn)       
        
def compare_hands(money, result, bet, turn):
    h1 = result[0]
    h2 = result[1]
    i = []
    sub_dict = {14: 'A', 13: 'K', 12: 'Q', 11: 'J'}
    for t in h2[1]:
        a, b = t
        if a in sub_dict:
            a = sub_dict[a]
        if b in sub_dict:
            b = sub_dict[b]
        i.append((a,b))

    if h1[2] > h2[2]:
        print ('')
        print ("Player Wins!")
        print ("Dealer had", h2[0], i)
        print ("Earns", "+", bet)
        print ('')
        money = money + bet + 5
        conclusion(money, turn)

    elif h1[2] < h2[2]:
        print ('')
        print ("Dealer Wins!")
        print ("Dealer has", h2[0], i)
        print ("Loses", "-", bet)
        print ('')
        money = money - bet - 5
        conclusion(money, turn)
        
    else:
        print ("TIE!", "Both Player has", h1[0],"!")
        print ('')
        conclusion(money, turn)

def conclusion(money, turn):
    print ('')
    
    if money <= 5:
        print ("Sorry.. You lost")
        quit()       

    elif money >= 300:
        print ("Congratulations! You Won!!!")
        quit()
        
    else:
        deal(money, deck, turn)
        
print ("Game: AZ Poker, made by: Johnny Kang")
print ('')
print ("AZ Poker Hand Ranks             (Probability)")
print ("Rank 16: Emperor Straight Flush = 0.0023%")
print ("Rank 15: Royal Straight Flush   = 0.0069%")
print ("Rank 14: Back Straight Flush    = 0.0083%")
print ("Rank 13: Five Of A Kind         = 0.022%")
print ("Rank 12: Straight Flush         = 0.046%")
print ("Rank 11: Flush                  = 0.42%")
print ("Rank 10: Full House             = 0.71%")
print ("Rank 9: Four Of A Kind          = 0.81%")
print ("Rank 8: House                   = 3.43%")
print ("Rank 7: Royal Straight          = 5.91(7.51)%")
print ("Rank 6: Back Straight           = 5.91(7.51)%")
print ("Rank 5: Straight                = 7.39(7.51)%")
print ("Rank 4: Three Of A Kind         = 9.24%")
print ("Rank 3: Two Pair                = 22.51%")
print ("Rank 2: One Pair                = 41.22%")
print ("Rank 1: High Card               = 14.06%")
print ('')
print ("To win this game, earn up to $300 or More under 30 turns!")
print ("You earn or lose money depend on amount you bet.")
print ("If your money reaches $5 or lower, you lose!")
time.sleep(2)
print ("Antes are $5. So you will lose extra $5 every time you fold and you will earn extra $5 every time dealer folds")
time.sleep(2)
print ("Have Fun!")
print ('')
create(money)



    
#windowSurface = pygame.display.set_mode((500, 400), 0, 32)

#menu = MainMenu(windowSurface)
#menu.run()
