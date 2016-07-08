'use strict';
var app = angular.module('app', ['ngRoute', 'ngSanitize', 'ngAnimate']);

app.config(function($routeProvider, $locationProvider) {
  $routeProvider

  .when('/', {
    templateUrl : '/static/views/home.html',
    controller  : 'HomeController'
  })
  .when('/:category', {
      templateUrl: '/static/views/listview.html',
      controller: 'ListController'
  })
  .when('/:category/:page', {
      templateUrl: '/static/views/detailview.html',
      controller: 'DetailController'
  })
  .otherwise({redirectTo: '/'});
    $locationProvider.html5Mode(true);
});

app.controller('Base', function($scope, $http, $location){
    $http.get('/api/base').then(function(response){
        $scope.base = response.data;
    });
    $http.get('/api/menu').then(function(response){
        $scope.menu = response.data;
    });
    $scope.isActiveUrl = function(route) {
        return $location.path().split('/')[1] == route;
    }

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
app.controller('ListController', function ($scope, $routeParams, DataCache, $http, $location) {
    $scope.currentUrl = $location.path();
    $scope.menu = getCachedData('menu/' + $routeParams.category, $http, DataCache);
});
app.controller('DetailController', function ($scope, $routeParams, DataCache, $http, $location) {
    $scope.currentUrl = $location.path().replace(/\/[\w-]+$/, '');
    $scope.menu = DataCache.get('menu' + $routeParams.category);
    if (!$scope.menu) {
		var requestMenu = $http.get('/api/menu/' + $routeParams.category);
		requestMenu.success(function (response) {
			DataCache.put('menu' + $routeParams.category, response);
			$scope.menu = response;
		});
	}
    $scope.detail = DataCache.get('detail' + $routeParams.page);
    if (!$scope.detail) {
		var requestDetail = $http.get('/api/detail/' + $routeParams.page);
		requestDetail.success(function (response) {
			DataCache.put('detail' + $routeParams.page, response);
			$scope.detail = response;
		});
	}
    $scope.isActiveUrl = function(route) {
        return $location.path().split('/')[2] == route;
    };
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
app.directive('onFinishRender', function ($timeout) {
    return {
        restrict: 'A',
        link: function (scope, element, attr) {
            if (scope.$last === true) {
                $timeout(function () {
                    scope.$emit('ngRepeatFinished');
                    var quqntity=$(".item__sub_menu__left").size();
                    var widthScroll=0;
                    for (var i=0;i<quqntity;i++){
                        widthScroll+=$(".item__sub_menu__left:eq("+i+")").width();
                    }
                    $(".sub_menu__left").css('max-width', widthScroll+1);
                });
            }
        }
    }
});
app.directive('leftMenu', function($scope, $location, DataCache, $http, $routeParams){
    $scope.currentUrl = $location.path().replace(/\/[\w-]+$/, '');
    $scope.menu = DataCache.get('menu' + $routeParams.category);
    if (!$scope.menu) {
		var requestMenu = $http.get('/api/menu/' + $routeParams.category);
		requestMenu.success(function (response) {
			DataCache.put('menu' + $routeParams.category, response);
			$scope.menu = response;
		});
	}
});

function getCachedData(path, $http, DataCache){
    function request(){
        return $http.get('/api/' + path).success(function(response){
            DataCache.put(path, response);
            return response
        })
    }
    return DataCache.get(path) || request()
}