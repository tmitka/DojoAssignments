function VehicleConstructor(name, wheels, passengers, speed){
    var distanceTraveled = 0;
    var self = this;
    this.Traveled = function(){
        distanceTraveled += self.speed;
        console.log(distanceTraveled);
    }
    this.name = name;
    this.wheels = wheels;
    this.passengers = passengers;
    this.speed = speed;
    this.makeNoise = function(noise){
        console.log(noise)
    }
    this.move = function(){
        this.makeNoise()
        Traveled()
    }
    this.miles = function(){
        console.log(distanceTraveled);
    }
}

var bike =  new VehicleConstructor("Bike", 2, 1, 15)

bike.name
bike.move
bike.Traveled()
bike.Traveled()
console.log(bike.miles)
//console.log(bike.wheels)
//console.log(bike.passengers)
//bike.makeNoise("Ring Ring")

var sedan =  new VehicleConstructor("Sedan", 4, 5)
//sedan.makeNoise("Honk Honk")

var bus = new VehicleConstructor("Bus", 4, 20)
bus.passengerNumber = 0
bus.pickupPassengers = function(newPassengers){
    bus.passengerNumber += newPassengers;
}

console.log(bus.passengerNumber)