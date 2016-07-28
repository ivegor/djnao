(function(){
    'use strict';
    angular
        .module('app')
        .controller('Base', base);
        base.$inject = ['$scope', '$http', '$location'];
        function base($scope, $http, $location){
            var vm = this;
            $http.get('/api/base').then(function(response){
                vm.base = response.data;
            });
            $http.get('/api/menu').then(function(response){
                vm.menu = response.data;
            });
            vm.isActiveUrl = function(route) {
                return $location.path().split('/')[1] == route;
            };
        }
})();