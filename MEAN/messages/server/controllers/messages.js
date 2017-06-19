var mongoose = require('mongoose');
var Message = mongoose.model('Message');
var Comment = mongoose.model('Comment');

function messageController(){
    var _this = this;
    this.index = function(req, res){
	Message.find({}, false, true).populate('_comments').exec(function(err, messages){
	      res.render('index.html', {messages: messages});
	});
    }
    this.new_comment = function(req, res){
	var message_id = req.params.id;
	Message.findOne({_id: message_id}, function(err, message){
		var newComment = new Comment({name: req.body.name, text: req.body.comment});
		newComment._message = message._id;
		Message.update({_id: message._id}, {$push: {"_comments": newComment}}, function(err){

		});
		newComment.save(function(err){
			if(err){
				console.log(err);
				res.render('index.html', {errors: newComment.errors});
			} else {
				console.log("comment added");
				res.redirect("/");
			}
		});

    })
    };