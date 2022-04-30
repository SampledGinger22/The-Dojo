function login(element){
    element.innerText = "Logout";
}

function like(element){
    element.innerText= parseInt(element.innerText)+1;
    alert ("\n You Liked this definition!");
}

function hide(element){
    element.remove();
}