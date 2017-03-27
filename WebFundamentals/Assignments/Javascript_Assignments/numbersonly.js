function numbersonly(arr){
    var newarray = [];
    for (var i = 0; i < arr.length; i ++){
        if (typeof arr[i] === "number"){
            newarray.push(arr[i]);
        }
    }
 console.log(newarray);
}



numbersonly([2, 4, 5, "what", 6]);