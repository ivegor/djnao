'use strict';
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

app.controller('Base', function($scope, $http){
    $http.get('/api/base').then(function(response){
        $scope.base = response.data;
    })

});

app.controller('HomeController', ['$scope', '$http', 'DataCache', function($scope, $http, DataCache) {
    $scope.slider = DataCache.get('slider');
    if (!$scope.slider) {
		var request = $http.get('/api/slider');
		request.success(function (response) {
			DataCache.put('slider', response);
			$scope.slider = response;
		});
	}
}]);
app.controller('ListController', function ($scope) {
    
});
app.filter('tel', function () {
    return function(tel){
        var value = String(tel).trim().replace(/^\+/, '');
        switch(value.length){
            case 11:
                return ['+7', value.slice(1, 4), value.slice(4, 7), value.slice(7, 9), value.slice(9, 11)].join('-');
            case 10:
                return ['+7', value.slice(0, 3), value.slice(3, 6), value.slice(6, 8), value.slice(8, 10)].join('-');
            case 5:
                return [value.slice(0, 1), value.slice(1, 3), value.slice(3, 5)].join('-');
            default:
                return tel
        }
    }
});
app.factory('DataCache', function ($cacheFactory) {
	return $cacheFactory('dataCache', {});
});
