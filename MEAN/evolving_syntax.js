"use strict"
var runningLogger = () => { console.log("I am running");}

//function runningLogger(){
//    console.log("I am running!")
//}

var multby10 = (number) => { console.log(number * 10) };

//function multby10(number){
//    return number * 10
//}
//console.log(multby10(5))

var stringReturnOne = (string) => {console.log(string)};

//var string1 = "Once upon a time"
//var string2 = "In a land not so different than our own."

//function stringReturnOne(string1){
//    return string1
//}

var stringReturnTwo = (string) => {console.log(string)};

//function stringReturnTwo(string2){
//    return string2
//}

var caller = (param) => {if(typeof param === 'function'){
    param("World2")
}}

//function caller(parameter){
//    if (typeof parameter === 'function'){
//        parameter()
//    }
//}

runningLogger()
multby10(5)
stringReturnOne("What in the")
stringReturnTwo("World")
caller(stringReturnTwo)