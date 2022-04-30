var count = 0;
const button = document.querySelector(".likes");
const textHolder = document.querySelector(".likecount");
textHolder.innerHTML = count;
button.addEventListener("click", function (){
    textHolder.innerHTML = ++count;
});

var count1 = 0;
const button1 = document.querySelector(".likes1");
const textHolder1 = document.querySelector(".likecount1");
textHolder1.innerHTML = count1;
button1.addEventListener("click", function (){
    textHolder1.innerHTML = ++count1;
});

var count2 = 0;
const button2 = document.querySelector(".likes2");
const textHolder2 = document.querySelector(".likecount2");
textHolder2.innerHTML = count2;
button2.addEventListener("click", function (){
    textHolder2.innerHTML = ++count2;
});