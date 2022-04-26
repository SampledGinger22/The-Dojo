var count = 2;
var count2 = 500;
const acceptbtn = document.querySelector(".accept");
const textHolder = document.querySelector(".reqcount");
const textHolder2 = document.querySelector(".con-num");
const profile = document.querySelector(".reqname")
textHolder.innerHTML = count;
textHolder2.innerHTML = count2;
acceptbtn.addEventListener("click", function (){
    textHolder.innerHTML = --count;
    textHolder2.innerHTML = ++count2;
    profile.remove();
});

const acceptbtn2 = document.querySelector(".accept2");
const profile2 = document.querySelector(".reqname2")
acceptbtn2.addEventListener("click", function (){
    textHolder.innerHTML = --count;
    textHolder2.innerHTML = ++count2;
    profile2.remove();
});


const denybtn = document.querySelector(".deny");
denybtn.addEventListener("click", function (){
    textHolder.innerHTML = --count;
    profile.remove();
});

const denybtn2 = document.querySelector(".deny2");
denybtn2.addEventListener("click", function (){
    textHolder.innerHTML = --count;
    profile2.remove();
});

const headshot = document.querySelector(".headshotimg");
const header = document.querySelector(".header");
const title = document.querySelector(".name");
const editbtn = document.querySelector(".btntxt");
const desc = document.querySelector(".userdes");
const desc1 = document.querySelector(".userdes1");
editbtn.addEventListener("click", function () {
    headshot.src = "chuck-norris.png";
    header.src = "flag.jpg";
    title.innerHTML = "Chuck Norris";
    desc.innerHTML = "Lover | Fighter | Bad MotherF*cker";
    desc1.innerHTML = "Master of the universe!";
});