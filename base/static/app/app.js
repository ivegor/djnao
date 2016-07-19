'use strict';
var app = angular.module('app', ['ui.router', 'ngSanitize', 'ngAnimate']);

app.config(function($stateProvider, $urlRouterProvider, $locationProvider) {
    // $urlRouterProvider.otherwise('/');
    $stateProvider
        .state('home', {
            url: '/',
            templateUrl : '/static/views/home.html',
            controller  : 'HomeController'
        })
        .state('menu', {
            url: '/:category',
            templateUrl: '/static/views/listview.html',
            controller: 'ListController',
            abstract: true
        })
            .state('menu.list', {
                url: '',
                templateUrl: '/static/views/baselist.html'
            })
            .state('menu.detail', {
                url: '/:page',
                templateUrl: '/static/views/detailview.html',
                controller: 'DetailController'
            });
    $locationProvider.html5Mode(true);
});

app.controller('Base', function($scope, $http, $location, $animateCss){
    $http.get('/api/base').then(function(response){
        $scope.base = response.data;
    });
    $http.get('/api/menu').then(function(response){
        $scope.menu = response.data;
    });
    $scope.isActiveUrl = function(route) {
        return $location.path().split('/')[1] == route;
    };
});

app.animation('.animate_for_footer', function ($animateCss) {
    return {
        leave: function(element){
            var ac = $('.animate-container');
            ac.css('min-height',$('.animate').height());
            setTimeout(function(){ac.css('min-height', '')} , 1000);
            $('footer').animate(
                {bottom:"-=300", position: 'absolute', opacity: 0}, 1000)
                        .animate(
                {bottom:"+=300", opacity: 1}, 300);
            return $animateCss(element, {
                event: 'leave',
                structural: true
            });
        }
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
app.controller('ListController', function ($scope, $stateParams, DataCache, $http, $location) {
    $scope.currentUrl = $location.path();
    // $scope.menu = getCachedData('menu/' + $stateParams.category, $http, DataCache);
    $scope.menu = DataCache.get('menu/' + $stateParams.category);
    if (!$scope.menu) {
		var requestDetail = $http.get('/api/menu/' + $stateParams.category);
		requestDetail.success(function (response) {
			DataCache.put('menu/' + $stateParams.category, response);
			$scope.menu = response;
		});
	}
    $scope.isActiveUrl = function(route) {
        return $location.path().split('/')[2] == route;
    };
});
app.controller('DetailController', function ($scope, $stateParams, DataCache, $http, $location) {

    $scope.detail = DataCache.get('detail' + $stateParams.page);
    if (!$scope.detail) {
		var requestDetail = $http.get('/api/detail/' + $stateParams.page);
		requestDetail.success(function (response) {
			DataCache.put('detail' + $stateParams.page, response);
			$scope.detail = response;
		});
	}
    // $http.get('/api/staff').success(function(response){console.log(response); $scope.detail=response})
    // $scope.set = function(){return '/static/views/staff.html'}
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
app.directive('staff', function(){
    return {
        restrict: 'C',
        template: ' hi ' * 5
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