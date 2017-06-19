var mongoose = require('mongoose');
var messages = require('../controllers/messages.js');
module.exports = function(app){
    app.get("/", messages.index)

    app.post("/message", messages.create)

    app.post("/comment/:id", messages.new_comment)
};
