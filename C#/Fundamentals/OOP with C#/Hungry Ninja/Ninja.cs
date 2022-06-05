class Ninja
{
    private int calorieIntake;
    public List<Food> FoodHistory;
    
    public Ninja(){
        calorieIntake = 0;
        FoodHistory = new List<Food>();
    }
    bool IsFull{
        get {
            return calorieIntake > 1200;
        }
    }
    // build out the Eat method
    public void Eat(Food item){
        if(IsFull == false){
            calorieIntake += item.Calories;
            FoodHistory.Add(item);
            Console.WriteLine($"Ninja ate {item.Name}");
            if(item.IsSpicy == true){
                Console.WriteLine($"{item.Name} is FUCKING SPICY!!! BRING MILK");
            }
            if(item.IsSweet == true){
                Console.WriteLine($"{item.Name} is sweet as a button");
            }
        }
        else if(IsFull == true){
            Console.WriteLine("WARNING! Ninja is on the brink of exploding, cease eating immediately!");
        }
    }
}