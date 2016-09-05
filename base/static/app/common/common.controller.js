(function(){
    'use strict';
    angular
        .module('app')
        .controller('Base', base);
        base.$inject = ['$http', '$location', '$mdSidenav'];
        function base($http, $location, $mdSidenav){
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

            vm.focusSection = function(){
                $mdSidenav('left').toggle();
            };

            vm.isActive = function(slug, pane){
                if (slug == $location.path().split('/')[1]){
                    if (!vm.init){
                        vm.init = 1;
                        pane.expand();
                    }
                    return 1
                }
            };
            vm.hide = function(){
                return angular.element( document.querySelector( '#animated')).hasClass('ng-enter') ;
            }
        }
})();