var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var CommentSchema = new Schema({
	name: String,
	text: String,
	_message: {type: Schema.Types.ObjectId, ref: 'Message'}
});
// CommentSchema.path('name').required(true, 'Name cannot be blank');
// CommentSchema.path('text').required(true, 'Comment cannot be blank');

mongoose.model("Comments", CommentSchema);
var Comments = mongoose.model("Comments");

mongoose.Promise = global.Promise;

