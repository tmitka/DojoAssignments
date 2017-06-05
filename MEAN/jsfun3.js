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

function ninjaConstructor(name, cohort){
    var ninja = {}
    var belt = "Yellow"
    ninja.name = name;
    ninja.cohort = cohort;
    ninja.belt = belt;
    ninja.levelup = function lvlup(belt){
        if (belt = "Yellow"){
            ninja.belt = "Red"
        }
        else if (belt = "Red"){
            ninja.belt = "Black"
        }
        else console.log("Ninja cannot level up")
    }
    return ninja
}
