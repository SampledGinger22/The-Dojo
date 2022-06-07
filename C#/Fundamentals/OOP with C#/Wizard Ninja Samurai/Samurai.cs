class Samurai : Human {

    public Samurai(string newname) : base(newname){
        Health = 200;
    }

    public override int Attack(Human enemy){
        base.Attack(enemy);
        if(enemy.Health <= 50){
            enemy.Health = 0;
        }
        return enemy.Health;
    }

    public void Meditate(){
        Health = 200;
    }
}