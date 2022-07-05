class Ninja {
    constructor(name, health){
        this.name = name;
        this.health = health;
        this.speed = 3;
        this.strength = 3;
    }
    sayName() {
        console.log(this.name);
    }
    showStats() {
        console.log("This is the ninja's info:", this.name, this.strength, this.speed, this.health);
    }
    drinkSake(){
        this.health += 10;
    }
}