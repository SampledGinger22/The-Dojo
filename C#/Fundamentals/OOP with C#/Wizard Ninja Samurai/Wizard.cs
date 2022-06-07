class Wizard : Human {

    public Wizard(string newname) : base(newname){
        Intelligence = 25;
        Health = 50;
    }

    public override int Attack(Human enemy){
        int dmg = Intelligence * 5;
        enemy.Health -= dmg;
        if(enemy.Health < 0){
            enemy.Health = 0;
        }
        Health += dmg;
        Console.WriteLine($"{Name} attacked {enemy.Name} for {dmg} damage! {enemy.Name} now has {enemy.Health} health points and {Name} has {Health} health points.");
        return enemy.Health;
    }

    public int Heal(Human friend){
        friend.Health += Intelligence * 10;
        return friend.Health;
    }
}
