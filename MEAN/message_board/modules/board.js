module.exports = function(request, response){
    var express = require('express');
    var app = express();
    var mongoose = require('mongoose');
    var moment = require('moment');
    var bodyParser = require('body-parser');
    app.use(bodyParser.urlencoded({ extended: true }));
    var path = require('path');
    app.use(express.static(path.join(__dirname, './static')));
    app.set('views', path.join(__dirname, './views'));
    app.set('view engine', 'ejs');

    mongoose.connect('mongodb://localhost/message_board');
    mongoose.Promise = global.Promise;
    var Schema = mongoose.Schema;

    // //Post schema
    // var PostSchema = new mongoose.Schema({
    //     username: { type: String, required: true, minlength: 2},
    //     content: {type: String, required: true, minlegth: 10},
    //     comments: [{type: Schema.Types.ObjectID, ref: 'Comment'}]
    // }, {timestamps:true});

    // //Comment schema
    // var CommentSchema = new mongoose.Schema({
    //     _post: [{type: Schema.Types.ObjectID, ref: 'Post'}],
    //     username: { type: String, required: true, minlength: 2},
    //     content: {type: String, required: true, minlegth: 10},
    // }, {timestamps:true});

    // mongoose.model('Post', PostSchema);
    // mongoose.model('Comment', CommentSchema);
    // var Post = mongoose.model('Post');
    // var Comment = mongoose.model('Comment');

    app.get('/', function(request, reponse){
        response.render('index');
    });

    app.post(function(request, response){
        var username = request.body.username;
        var content = request.body.username;
        console.log('This is post: ' + request.body);
        response.redirect('/');
    });
    
};