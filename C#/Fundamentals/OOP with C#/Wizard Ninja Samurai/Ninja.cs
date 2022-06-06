class Ninja : Human{

    public Ninja(string newname) : base(newname){
        Dexterity = 175;
    }
    public override void Attack(int enemyhealth){
        enemyhealth = enemyhealth - (Dexterity * 5);
        Random rand = new Random();
        int hitchance = rand.Next(1,6);
        if(hitchance == 5){
            enemyhealth -= 10;
        }
    }

    public void Steal(int enemyhealth){
        enemyhealth -= 5;
        Health += 5;
    }
}