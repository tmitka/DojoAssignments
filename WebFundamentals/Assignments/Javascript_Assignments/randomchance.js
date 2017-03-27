function randomchance(number){
    var quarters = number;
    var usernumber = Math.round(Math.random() * 100) + 1;
    var win = Math.round(Math.random() * 100) + 1;
    for (var i = number; i > 0; i --){
        if (usernumber == win){
            quarters = quarters + Math.trunc(Math.random() * 50)+51;
            break;

        }
        else (quarters -= 1)
            usernumber = Math.round(Math.random() * 100) + 1;
            win = Math.round(Math.random() * 100) + 1;

    }
    console.log(quarters);
}

randomchance(100)