Player player = new Player("Mason");
Deck deck = new Deck();

deck.NewDeck();
deck.Shuffle(deck.Cards);
player.Draw(deck.Deal());
player.Draw(deck.Deal());
player.Draw(deck.Deal());
player.ShowHand();
player.Discard(1);
player.StartNew();
deck.Reset();
deck.Shuffle(deck.Cards);




