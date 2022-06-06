class Samurai : Human {

    public Samurai(string newname) : base(newname){
        Health = 200;
    }

    public override void Attack(int enemyhealth){
        base.Attack(enemyhealth);
        if(enemyhealth <= 50){
            enemyhealth = 0;
        }
    }

    public void Meditate(){
        Health = 200;
    }
}