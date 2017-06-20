app.factory('postsFactory', function ($http) {
    var factory = {}
    var posts = []; 
    function updateFactory(callback, data){
        posts = data;
    }
    factory.getPosts = function (callback) {
        $http.get('/api').then(function(response){
            console.log(response);
            updateFactory(callback, response.data);
        });
    };
    return factory;
})