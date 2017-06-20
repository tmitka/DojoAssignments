var mongoose = require('mongoose');

var Schema = mongoose.Schema;

//Post schema
var PostSchema = new Schema({
    username: { type: String, required: true, minlength: 2},
    content: {type: String, required: true, minlegth: 10},
    comments: [{type: Schema.Types.ObjectId, ref: 'Comment'}]
}, {timestamps:true});

//Comment schema
var CommentSchema = new Schema({
    _post: [{type: Schema.Types.ObjectId, ref: 'Post'}],
    username: { type: String, required: true, minlength: 2},
    content: {type: String, required: true, minlegth: 10},
}, {timestamps:true});

mongoose.model('Post', PostSchema);
mongoose.model('Comment', CommentSchema);

