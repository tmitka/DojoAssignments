var mongoose = require('mongoose');
var messages = require('../controllers/messages.js');
module.exports = (function (app) {
    app.get('/api', messages.index); 
    app.post('/api/new_post', messages.create);
    app.post('/api/comments/new/:id', messages.new_comment);
});
