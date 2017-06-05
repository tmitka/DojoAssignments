function sumall(x, y){
    var sum = 0
    if (x > y){
        for (i = y; i <= x; i +=1){
            sum = sum + i
        }
    }
    else if (y > x){
        for (i = x; i <= y; i += 1){
            sum = sum + i
        }
    }
    else return console.log("please select two different numbers")

console.log(sum)
}

//sum all

function min(array){
    var min = array[0]
    for (i = 2; i < array.length; i += 1){
        if (array[i] < min){
            min = array[i]
        }
    }
console.log(min)
}

//minimum

function avg(arr){
    var sum = arr[0]
    for (i = 1; i < arr.length; i += 1){
        sum = sum + arr[i]
        var avg = sum/arr.length
    }
    console.log(avg)
}

//average

var object_functions = {
    sumall:function sumall(x, y){
    var sum = 0
    if (x > y){
        for (i = y; i <= x; i +=1){
            sum = sum + i
        }
    }
    else if (y > x){
        for (i = x; i <= y; i += 1){
            sum = sum + i
        }
    }
    else return console.log("please select two different numbers")

console.log(sum)
},
    min: function min(array){
    var min = array[0]
    for (i = 2; i < array.length; i += 1){
        if (array[i] < min){
            min = array[i]
        }
    }
console.log(min)
},
    avg: function avg(arr){
    var sum = arr[0]
    for (i = 1; i < arr.length; i += 1){
        sum = sum + arr[i]
        var avg = sum/arr.length
    }
    console.log(avg)
}
}
var person = {
    name: "Ted",
    distance_traveled: 0,
    say_name: function(){
        console.log(person.name);
    },
    say_something: function(string){
        console.log(person.name + " is running");
    },
    walk: function(){
        console.log(person.name + " is walking");
        distance += 3
    },
    run: function(){
        console.log(person.name + " is running");
        disance += 10
    },
    crawl: function(){
        console.log(person.name + " is crawling");
        distance += 1
    },
}

