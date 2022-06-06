class Player{
    public string Name;
    public List<Card> hand = new List<Card>();

    public Player(string name){
        Name = name;
    }
    public Card Draw(Card newCard){
        hand.Add(newCard);
        return newCard;
    }
    public void ShowHand(){
        Console.WriteLine("The Player currently holds:");
        for(int i = 0; i < hand.Count(); i++){
        Console.WriteLine($"{hand[i].Name} of {hand[i].Suit}");
        }
    }

    public void Discard(int num){
        Console.WriteLine($"Player has discarded a {hand[num].Name} of {hand[num].Suit}.");
        hand.Remove(hand[num]);
    }

    public void StartNew(){
        hand.Clear();
        Console.WriteLine($"Player has folded. They now hold {hand.Count()} cards.");
    }
}