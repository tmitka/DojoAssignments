function runningLogger(){
    console.log("I am running!")
}

function multby10(number){
    return number * 10
}
console.log(multby10(5))

string1 = "Once upon a time"
string2 = "In a land not so different than our own."

function stringReturnOne(string1){
    return string1
}

function stringReturnTwo(string2){
    return string2
}

function caller(parameter){
    if (typeof parameter === 'function'){
        parameter()
    }
}

function myDoubleConsoleLog(params1, params2){
    if (typeof params1 === 'function' && typeof params2 === 'function'){
        var both_params = params1 + params2
        return both_params 
    }
}

//console.log(myDoubleConsoleLog(stringReturnOne, stringReturnTwo))

function caller2(param){
    console.log('starting')
    setTimeout(function(){
        if (typeof param === 'function'){
        console.log('ending')
        return "interesting"
    }
    }, 2000)

}

caller2(myDoubleConsoleLog)