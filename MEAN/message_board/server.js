
var express = require("express");
var mongoose = require("mongoose");
var path = require("path");
var bodyParser = require("body-parser");

var app = express();

// --------------------------------------------------
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, "./client")));
app.use(express.static(path.join(__dirname, "./bower_components")));
// app.set("views", path.join(__dirname, "./client/views"));
// app.set("view engine", "ejs");
// ---------------------------------------------------

// require the mongoose configuration file which does the rest for us
require('./server/config/mongoose.js');

// --------Routes-------------
// store the function in a variable
var router = require('./server/config/routes.js');
// invoke the function stored in routes_setter and pass it the "app" variable
router(app);


app.listen(8000, function(){
	console.log("server running on port 8000");
});



