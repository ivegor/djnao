(function(){
    'use strict';
    angular
        .module('app')
        .controller('Base', base);
        base.$inject = ['$scope', '$http', '$location', '$mdSidenav'];
        function base($scope, $http, $location, $mdSidenav){
            var vm = this;
            $http.get('/api/base').then(function(response){
                vm.base = response.data;
            });
            $http.get('/api/menu').then(function(response){
                vm.menu = response.data;
            });
            vm.openMenu = function(){
                $mdSidenav('left').toggle();
            };
            vm.isSelected = function(slug){
                return slug == $location.path().split('/')[1]
            };
            vm.focusSection = function(){
                $mdSidenav('left').toggle();
            };
            vm.isOpen = function(){
                return 1
            };
            vm.isSectionSelected = function(){
                return 1
            }
        }
})();