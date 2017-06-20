app.controller('postsController', function($scope, postsFactory){
    console.log('helo world');
    $scope.posts = []
    
    function getPosts(data){
        $scope.posts = data;
    };

    $scope.index = function(){
        postsFactory.getPosts(getPosts)
    };

    $scope.index();


});