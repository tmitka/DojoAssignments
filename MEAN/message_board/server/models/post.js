// require mongoose
var mongoose = require('mongoose');

// var Schema = mongoose.Schema;
// // Create dog schema and attach it as a model to our database
// var DogSchema = new Schema({
//     name: String,
//     weight: Number,
//     color: String
// });
// // register the schema as a model
// mongoose.model('Dog', DogSchema);
// // assigning Dog to a variable to use later
// var Dog = mongoose.model('Dog');
// mongoose.Promise = global.Promise;

var Schema = mongoose.Schema;
var MessageSchema = new Schema({
	name: String,
	message: String,
	comments: [{type: Schema.Types.ObjectId, ref: 'Comments'}]
});
// MessageSchema.path('name').required(true, 'Name cannot be blank');
// MessageSchema.path('message').required(true, 'Message cannot be blank');

mongoose.model("Message", MessageSchema);
var Message = mongoose.model("Message");

mongoose.Promise = global.Promise;