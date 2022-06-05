class Buffet
{
    public List<Food> Menu;
    //constructor
    public Buffet()
    {
        Menu = new List<Food>()
        {
            new Food("Prime Rib", 1000, false, false),
            new Food("Mashed Potatoes", 500, false, false),
            new Food("Chicken Wings", 700, true, false),
            new Food("Ice Cream", 3, false, true),
            new Food("Gravy", 300, false, false),
            new Food("Smoked Burger", 600, true, false),
            new Food("Salad Bar", 0, false, false),
            new Food("Mystery Caserole", 3000, false, false)
        };
    }
    Random rand = new Random();
    public Food Serve(){
        int count = Menu.Count();
        int newserving = rand.Next(0, count);
        return Menu[newserving];
    }
}


