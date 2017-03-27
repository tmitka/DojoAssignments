var daysuntilmybirthday = 60;

function countdown(daysuntilmybirthday){
    while (daysuntilmybirthday > -1){
    if (daysuntilmybirthday > 30){
    console.log(daysuntilmybirthday, " days until my birthday. Such a long time...:(");
    daysuntilmybirthday -= 1;
    }
    else if (daysuntilmybirthday < 31 && daysuntilmybirthday > 5){
    console.log(daysuntilmybirthday, " days until my birthday. It's almost here!");
    daysuntilmybirthday -= 1;
    }
    else if (daysuntilmybirthday <= 5 && daysuntilmybirthday > 0){
    console.log(daysuntilmybirthday, " DAYS UNTIL MY BIRTHDAY!!.");
    daysuntilmybirthday -= 1;
    }
    else if (daysuntilmybirthday == 0){
    console.log("HAPPY BIRTHDAY!!!!!!!");
    break;
    }
}
}

countdown(daysuntilmybirthday)