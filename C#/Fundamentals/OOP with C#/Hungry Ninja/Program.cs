class Food
{
    public string Name;
    public int Calories;
    public bool IsSpicy; 
    public bool IsSweet; 
}

class Buffet
{
    public List<Food> Menu;
     
    //constructor
    public Buffet()
    {
        Menu = new List<Food>()
        {
            new Food("Example", 1000, false, false)
        };
    }
     
    public Food Serve()
    {
    }
}

class Ninja
{
    private int calorieIntake;
    public List<Food> FoodHistory;
     
    // add a constructor
     
    // add a public "getter" property called "IsFull"
     
    // build out the Eat method
    public void Eat(Food item)
    {
    }
}


