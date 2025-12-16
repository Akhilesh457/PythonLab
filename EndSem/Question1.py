def create_deck():
    # Define the values for cards
    values_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    # Define the suits
    suits_list = ['h', 'c', 'd', 's']
    
    # Initialize an empty list to store the cards
    deck = []
    
    # Use nested loops to iterate through all combinations of values and suits
    for suit in suits_list:
        for value in values_list:
            # Create the two-character abbreviation and add to deck
            card = value + suit
            deck.append(card)
    
    return deck

# Example usage:
if __name__ == "__main__":
    deck = create_deck()
    print(f"Total cards in deck: {len(deck)}")
    print("Deck of cards:", deck)
