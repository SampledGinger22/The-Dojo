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

class Sensei extends Ninja {
    constructor(){
        super("Master Splinter", 200);
        this.speed = 10;
        this.strength = 10;
        this.wisdom = 10;
    }
    speakWisdom(){
        this.drinkSake();
        console.log("Even a mighty eagle must rest its wings from the chaos of the wind,")
    }
}