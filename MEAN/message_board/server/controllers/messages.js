var mongoose = require('mongoose');
var Post = mongoose.model('Post');
var Comment = mongoose.model('Comment');


function postController(){
    var _this = this;
    this.index = function (request, response) {
        Comment.find({}, function (comment_err, comments) {
            if (comment_err) {
                console.log('Something went wrong trying to get comments');
                console.log(comment_err);
                response.json(comment_err);
            } else {
                console.log('Successfully retrieved comments');
                Post.find({}).populate('comments').exec(function (populate_err, posts) {
                    if (populate_err) {
                        console.log('Something went wrong trying to populate comments');
                        response.json(populate_err);
                    } else {
                        console.log('Comments populated successfully');
                        response.json(posts);
                    };
                });
            };
        });
    };
    this.create = function (request, response) {
        var username = request.body.username;
        var content = request.body.content;
        var post = new Post({ username: username, content: content });
        post.save(function (post_err) {
            if (post_err) {
                console.log('Something went wrong posting a new message');
                console.log(post_err);
                response.json(post_err);
            } else {
                console.log('New message posted successfully');
                response.json({success:'New message posted successfully'})
            };
        });
    };
    this.new_comment = function (request, response) {
        var post_id = request.params.id;
        var username = request.body.username;
        var content = request.body.content;

        Post.findOne({ _id: post_id }, function (find_err, post) {
            if (find_err) {
                console.log('Something went wrong trying to find this post');
                console.log(find_err);
                response.json(find_err);
            } else {
                console.log('Post found successfully')
                var comment = new Comment({ username: username, content: content });
                comment._post = post._id;
                post.comments.push(comment);
                comment.save(function (save_err) {
                    if (save_err) {
                        console.log('Something went wrong trying to save new comment');
                        console.log(save_err);
                        response.json(save_err);
                    } else {
                        console.log('New comment save successfully');
                        post.save(function (post_save_err) {
                            if (post_save_err) {
                                console.log('Something went wrong trying to save comments to post');
                                console.log(post_save_err);
                                response.json(post_save_err);
                            } else {
                                console.log('Successfully added comment to post');
                                response.json({success:'Successfully added comment to post'});
                            };
                        })
                    };
                });
            };
        });
    };
};


module.exports = new postController();

