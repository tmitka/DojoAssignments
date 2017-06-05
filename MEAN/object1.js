function VehicleConstructor(name, wheels, passengers){
    var vehicle = {};

    vehicle.name = name;
    vehicle.wheels = wheels;
    vehicle.passengers = passengers;
    vehicle.makeNoise = function(noise){
        console.log(noise)
    }
    return vehicle
}

var bike = VehicleConstructor("Bike", 2, 1)

//console.log(bike.name)
//console.log(bike.wheels)
//console.log(bike.passengers)
//bike.makeNoise("Ring Ring")

var sedan = VehicleConstructor("Sedan", 4, 5)
//sedan.makeNoise("Honk Honk")

var bus = VehicleConstructor("Bus", 4, 20)
bus.passengerNumber = 0
bus.pickupPassengers = function(newPassengers){
    bus.passengerNumber += newPassengers;
}

bus.pickupPassengers(10)
bus.pickupPassengers(10)

console.log(bus.passengerNumber)