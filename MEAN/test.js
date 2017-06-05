// Overview: This function creates game objects, by returning a game object when invoked
function GameConstructor(consumerPrice,dealerCost,name, inStock){
  // private variables
  // dealerCost is private so a buyer can't see our ridiculous markup!
  var consumerPrice = consumerPrice;
  var dealerCost = dealerCost;
  // if you are returning an object, set it as the last private variable
  var ourGame = {}; // end of private properties
  // public properties
  //_ signifies a field that we shouldn't modify, but is public
  ourGame._name = name;
  ourGame.type = 'board game';
  ourGame.player = [];
  // public methods can affect private variables!
  ourGame.addPlayer = function(player_name){
    ourGame.player.push(player_name);
  }
  ourGame.showPrivateVariables = function(){
    console.log(dealerCost);
    console.log(consumerPrice);
  }//end of methods


  //private methods :
  function myPrivateFunction(){
    console.log('hello, I am going to create a new object when I am returned!');
  }
  //End private methods
    // run events prior to construction if necessary
  myPrivateFunction();
  // return your final object (We will learn about other strategies to construct objects soon!)
  return ourGame;
}