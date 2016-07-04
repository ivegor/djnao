/**
 * Created by egor on 27.06.16.
 */
var app = angular.module('app', ['ngRoute']);

app.config(function($routeProvider, $locationProvider) {
  $routeProvider

  .when('/', {
    templateUrl : '/static/views/home.html',
    controller  : 'HomeController'
  })
  .when('/information', {
      templateUrl: '/static/views/listview.html',
      controller: 'ListController'
  })
  .when('/activity', {
      templateUrl: '/static/views/listview.html',
      controller: 'ListController'
  })
  .otherwise({redirectTo: '/'});
    $locationProvider.html5Mode(true);
});
app.controller('HomeController', function($scope) {
  $scope.message = 'Hello from HomeController';
});
app.controller('ListController', function ($scope) {
    
});
