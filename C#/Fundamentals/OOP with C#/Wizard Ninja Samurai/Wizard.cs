class Wizard : Human {

    public string MagicType;

    public Wizard(string newname) : base(newname){
        MagicType = "Dark Magic";
        Intelligence = 25;
        Health = 50;
    }

    public override void Attack(int enemyhealth){
        enemyhealth = enemyhealth - (Intelligence * 5);
        Health = Health + (Intelligence * 5);
    }

    public void Heal(int friendhealth){
        friendhealth += Intelligence * 10;
    }
}
