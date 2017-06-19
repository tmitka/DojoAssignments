app.factory("messageFactory", function ($http) {
    
    var factory = {};
    factory.messages = [];
    
    // index: Retrieve all 
    factory.index = function(callback){
        $http.get("/api").then(function(response){
            factory.messages = response.messages;
            callback(factory.messages);
        });    
    };
    // create: add 
    factory.createMessage = function(message, callback){
        $http.post("/api/message",message).then(function(response){
            factory.index(callback);
        });
    };

    factory.createComment = function(comment, messageId, callback){
        $http.post("/api/comment/" + messageId,comment).then(function(response){
            factory.index(callback);
        });
    }
        
    return factory;
});

