var mongoose = require('mongoose');
var Comments = mongoose.model("Comments");
var Message = mongoose.model("Message");

module.exports = {
    index: function(req, res){
        Message.find({}).populate('comments').exec(function (err2, messages) {
            if (err2) {
                console.log(err2);
                res.json({messages: [], errors: err2 });
            } else {
                res.json({messages: messages, errors: [] });
            }
        });

    },

    // New Message
    new_message: function(req, res){
        var newMessage = new Message({name: req.body.name, message: req.body.message});
        newMessage.save(function(err3){
            if(err3){
                console.log(err3);
                res.json({errors: err3});
            } else {
                console.log("success");
                res.json({message:"Success!"});
            }
        })
    },

    // New Comment
    new_comment: function(req, res){
        var message_id = req.params.id;
        Message.findOne({_id: message_id}, function(err, message){
            var newComment = new Comments({name: req.body.name, text: req.body.comment});
            newComment._message = message._id;
            Message.update({_id: message._id}, {$push: {"comments": newComment}}, function(err){

            });
            newComment.save(function(err4){
                if(err4){
                    console.log(err4);
                    res.json({errors: err4});
                } else {
                    console.log("comment added");
                    res.json({message:"Success!"});
                }
            });
        })
    }
}