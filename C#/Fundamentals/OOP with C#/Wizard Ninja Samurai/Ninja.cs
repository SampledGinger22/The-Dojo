class Ninja : Human{

    public Ninja(string newname) : base(newname){
        Dexterity = 175;
    }
    public override int Attack(Human enemy){
        int dmg = Dexterity * 5;
        enemy.Health -= dmg;
        Random rand = new Random();
        int hitchance = rand.Next(1,6);
        if(hitchance == 5){
            enemy.Health -= 10;
            Console.WriteLine($"{Name} attacked {enemy.Name} for {dmg+10} damage!");
        }
        else{
            Console.WriteLine($"{Name} attacked {enemy.Name} for {dmg} damage!");
        }
        return enemy.Health;
    }

    public int Steal(Human enemy){
        enemy.Health -= 5;
        Health += 5;
        Console.WriteLine($"Enemy health is now {enemy.Health} and your health is now {Health}");
        return enemy.Health;
    }
}