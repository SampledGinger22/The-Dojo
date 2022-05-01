let disp = "";

function press(num) {
    var displayDiv = document.querySelector("#display");
    disp = disp + num.toString(); //Changing it to a string changes it from text to a numberical value we can use to do the math
    displayDiv.innerText = disp;
}

let arr = [];
let op = "";
let sum = 0;

function setOP(key) {
    if(arr.length === 1) {
        var valTwo = parseFloat(disp);
        arr.push(valTwo);
        calc(op);
        arr = [];
        arr.push(sum);
        disp = "";
        op = key;
    }
    if(arr.length === 0) {
        op = key;
        var valOne = parseFloat(disp);
        arr.push(valOne);
        disp = "";
    }
}

function calc(cal) {
    if(cal === "+") {
        sum = arr[0] + arr[1];
    }
    if(cal === "-"){
        sum = arr[0] - arr[1];
    }
    if(cal === "*"){
        sum = arr[0] * arr[1];
    }
    if(cal === "/"){
        sum = arr[0] / arr[1];
    }
    var total = document.querySelector("#display");
    total.innerText = sum;
}

function clr() {
    disp = "";
    op = "";
    sum = 0;
    arr = [];
    var clearDisp = document.querySelector("#display")
    clearDisp.innerText = "0";
}

function calculate() {
    var valTwo = parseFloat(disp);
        arr.push(valTwo);
        calc(op);
}