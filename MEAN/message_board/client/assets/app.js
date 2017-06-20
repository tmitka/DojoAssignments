var app = angular.module('message_board', ['ngRoute']);
app.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'index.html',
            controller: 'postsController'
        })
        .otherwise({
            redirectTo: '/'
        });
});

