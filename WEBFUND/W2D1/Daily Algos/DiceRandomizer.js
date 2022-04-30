function d6() {
    var roll=Math.random (1,6);
    min = Math.ceil(1);
    max = Math.floor(7);
    roll = Math.floor(Math.random()*(7 - 1)) +1;
    return roll;
}
    
var playerRoll = d6();
console.log("The player rolled: " + playerRoll);
