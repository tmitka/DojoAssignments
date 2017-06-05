//undefined
console.log(first_variable);

//declarations hoisted
var first_variable = "Yipee I was first!";
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);

//"Yipee I was first!"

var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

//"half-chicken"
//"gone"
//"Chicken"

var new_word = "NEW!";
function lastFunc() {
  new_word = "old";
}
console.log(new_word);
//"NEW!"