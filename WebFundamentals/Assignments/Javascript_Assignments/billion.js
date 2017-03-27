function makemoney(number){
    var sum = 0;
    var pennies = 1;
    var collected = 0;
    var dollars = 0;
    for (var i = 1; i <= number; i ++){
        if (number == 1){
            collected ++;
            sum = sum + pennies;
            pennies += 1;
            
        } else {
            pennies = (pennies * 2);
            sum =  pennies / 2;
            dollars = sum / 100
            collected ++;
           
        }
    }
     console.log("You will have $", dollars, " after", number, "days.");
    }



makemoney(30)