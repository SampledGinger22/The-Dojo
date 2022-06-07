interface IConsumable
{
    string Name {get;set;}
    int Calories {get;set;}
    bool IsSpicy {get;set;}
    bool IsSweet {get;set;}
    string GetInfo(string name, int cal, bool spice, bool sweet){
        Name = name;
        Calories = cal;
        IsSpicy = spice;
        IsSweet = sweet;
    }
}   

