class Food
{
    public string Name;
    public int Calories;
    public bool IsSpicy; 
    public bool IsSweet; 

    public Food(string foodname, int cal, bool spice, bool sweet){
        Name = foodname;
        Calories = cal;
        IsSpicy = spice;
        IsSweet = sweet;
    }
}