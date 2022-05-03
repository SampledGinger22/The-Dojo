const two_str1 = "creature";

function reverse(val){
    var placeholder = "";
    for(var i = val.length-1; i>= 0; i--){
        placeholder += val[i];
    }
    return(placeholder)
}
answer = reverse(two_str1)
console.log(answer)