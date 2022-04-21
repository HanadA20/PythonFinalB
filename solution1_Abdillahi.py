
class Card:
  
#suppose to be 2 "_" in __init__
  
  def __init__(self, the_rank, the_suit): #variable the_rank passed into init function should match what self.rank is equaled to
    
    self.rank = the_rank

    self.suit = the_suit

  def color(self): #self in ()

    if self.suit == "Club" or self.suit == "Spade":

      return "black"

    else:

     return "red"

# Represent card as a string.

# The symbols list entries "0" and "1" are dummy entries.

  def __str__(self): #bad indents
     symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] #Symbols should be symbols
     return symbols[self.rank] + self.suit

c1 = Card(14, "Diamond") #card should be Card

print(c1)

print(c1.rank, c1.suit, c1.color())
