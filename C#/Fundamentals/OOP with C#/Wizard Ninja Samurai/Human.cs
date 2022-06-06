class Human {
    public string Name;
    public int Strength;
    public int Intelligence;
    public int Dexterity;
    public int Health;

    public Human(string newname){
        Name = newname;
        Strength = 3;
        Intelligence = 3;
        Dexterity = 3;
        Health = 100;
    }

    public void GetInfo(string testname, int stre, int intel, int dex, int heal){
        Name = testname;
        Strength = stre;
        Intelligence = intel;
        Dexterity = dex;
        Health = heal;
    }

    public virtual void Attack(int enemyhealth){
        enemyhealth = enemyhealth - (Strength * 5);
    }
}
