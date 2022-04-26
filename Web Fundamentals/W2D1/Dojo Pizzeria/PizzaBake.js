//     var pizza = {
//         crustType: "deepdish",
//         sauceType: "traditional",
//         cheeses: ["mozzarella", "feta", "gouda"],
//         toppings: ["mushrooms", "anchovies", "spicy italian sausage", "pepperoni", "red onion"],
//     };
// console.log(pizza);

function pizzaOven(crustType= ["deep dish", "hand tossed"], sauceType= ["traditional", "marinara"], cheeses= ["mozzarella", "feta", "gouda"], toppings= ["pepperoni", "sauasge"]){
    var pizza = {};
    pizza.crust = crustType;
    pizza.sauce = sauceType;
    pizza.cheese = cheeses;
    pizza.toppings = toppings;
    return pizza;
}

// default response
console.log(pizzaOven());

// assignment request
console.log(pizzaOven("deep dish,", "traditional,", ["mozzerella"], ["pepperoni", "sausage"]));

// assignment request 2
console.log(pizzaOven("hand tossed,", "marinara,", ["mozzerella", "feta"], ["mushrooms", "olives", "onions"]));
