// const password = document.querySelector(".password");
// const button = docuement.querySelector(".generate");
function passgen(){
    var list = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    var list2 = [];
    for(var i = 0; i < 14; i++){
        var rand = Math.random(0, list.length);
        list2.push(list[rand]);
    }
    var string = list2.toString();
    console.log(string);
    return list2;
}
console.log(passgen());