(function(){
    'use strict';
    angular
        .module('app')
        .controller('Base', base);
        base.$inject = ['$scope', '$http', '$location'];
        function base($scope, $http, $location){
            $http.get('/api/base').then(function(response){
                $scope.base = response.data;
            });
            $http.get('/api/menu').then(function(response){
                $scope.menu = response.data['menu'];
            });
            $scope.isActiveUrl = function(route) {
                return $location.path().split('/')[1] == route;
            };
        }
})();