const cancel = document.querySelector(".cancel")
const deletebutton = document.querySelector(".deletebutton")
const warning = document.querySelector(".warningheader")
function popwarning(){
    if (warning.style.display = "none") {
        warning.style.display = "flex";
    }
}

function exit(){
    if (warning.style.display = "flex"){
        warning.style.display = "none";
    }
}

