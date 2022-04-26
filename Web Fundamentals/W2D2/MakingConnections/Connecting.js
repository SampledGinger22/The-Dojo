var count = 0;
const button = document.querySelector(".likes");
const textHolder = document.querySelector(".likecount");
textHolder.innerHTML = count;
button.addEventListener("click", function (){
    textHolder.innerHTML = ++count;
});