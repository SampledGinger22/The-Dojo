class Human {
    public string Name { get; set; }
    public int Strength { get; set; }
    public int Intelligence { get; set; }
    public int Dexterity { get; set; }
    public int Health { get; set; }

    public Human(string name){
        Name = name;
        Strength = 10;
        Intelligence = 10;
        Dexterity = 10;
        Health = 100;
    }

    public void GetInfo(string testname, int stre, int intel, int dex, int heal){
        Name = testname;
        Strength = stre;
        Intelligence = intel;
        Dexterity = dex;
        Health = heal;
    } 

    public virtual int Attack(Human enemy){
        int dmg = Strength * 3;
        enemy.Health -= dmg;
        if(enemy.Health < 0){
            enemy.Health = 0;
        }
        Console.WriteLine($"{Name} attacked {enemy.Name} for {dmg} damage!");
        return enemy.Health;
    }
}
