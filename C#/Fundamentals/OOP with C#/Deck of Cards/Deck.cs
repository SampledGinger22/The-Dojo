class Deck{
    public List<Card> Cards = new List<Card>();
    public void NewDeck(){
        for(int i = 1; i < 14; i++){
            string name = "";
            if(i==1){
                name = "Ace";
            }
            else if(i==11){
                name = "Jack";
            }
            else if(i==12){
                name = "Queen";
            }
            else if(i==13){
                name = "King";
            }
            else {
                name = i.ToString();
            }
            Cards.Add(new Card(name, "Clubs", i));
            Cards.Add(new Card(name, "Spades", i));
            Cards.Add(new Card(name, "Hearts", i));
            Cards.Add(new Card(name, "Diamonds", i));
        }
    }
    public Card Deal(){
        Card TopCard = Cards[0];
        Cards.Remove(Cards[0]);
        Console.WriteLine($"Player has picked up a {TopCard.Name} of {TopCard.Suit}.");
        return TopCard;
    }

    public void Reset(){
        NewDeck();
    }

    public void Shuffle(List<Card> list){
        Random rand = new Random();
        int i = 1;
        int deckcount = 52;
        List<Card> tempdeck = new List<Card>();
        while(i < 53){
            if(deckcount != 0){
                int cardval = rand.Next(0, deckcount);
                tempdeck.Add(Cards[cardval]);
                Cards.Remove(Cards[cardval]);
                deckcount--;
                i++;
            }
        }
        Cards = tempdeck;
        Console.WriteLine("The Deck is Shuffled");
    }
}