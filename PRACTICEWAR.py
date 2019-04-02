class Deck:
    """Definition of the Deck class. Each Deck is just a list of
    cards. It is initialized to contain the full deck of 52 cards."""
    
    def __init__(self):
        """Return a new deck of cards."""
        
        self._cards = []
        
        # For each suit and each rank, generate
        # a card and add it to the deck.
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self._cards.append(c)
        
    def shuffle(self):
        """Shuffle the cards in place."""
        # Note that random.shuffle is a method on Lists,
        # not on Decks. If we want to shuffle a Deck, we
        # have to define it ourselves.
        random.shuffle(self._cards)

    def deal(self):
        """Remove and return the top card, or None
        if the deck is empty."""
        # The following only works because we’ve
        # defined __len__ below.
        if len(self) == 0:
            return None
        else:
            # Removes the top card from the deck and
            # returns it.
            return self._cards.pop(0)
    
    def __len__(self):
        """Returns the number of cards left in the deck."""
        return len(self._cards)

    def __str__(self):
        result = ""
        for c in self._cards:
            result = result + str(c) 
        return result


class Card:
    """A card object with a suit and rank."""
    
    # These are class attributes, not instance attributes
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('S', 'D', 'H', 'C')
    
    # This is called as Card(rank, suit).
    def __init__(self, rank, suit):
        """Create a Card object with the given rank and suit."""
        
        if (not rank in Card.RANKS or not suit in Card.SUITS ):
            print ("Not a legal card specification.")
            return
        self._rank = rank
        self._suit = suit
        
    def getRank(self):
        """Return my rank."""
        return self._rank
    
    def getSuit(self):
        """Return my suit."""
        return self._suit

    def __str__(self):
        """Return a string that is the print representation
        of this Card's value."""
        
        # Create a dictionary for the special cases.
        translate = { 1:'A', 11:'J', 12:'Q', 13:'K' }
        r = self._rank
        # See if r is a special case (printwise).
        if r in [1, 11, 12, 13]:
            myrank = translate[r]
        else:
            myrank = str( r )
        return myrank + " "+ self._suit
      
        

    def __lt__(self, other):


        return ( self._rank < other.getRank() )


def main():
    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    
    playGame(cardDeck,player1,player2)

main()
