(function(){
    'use strict';
    angular
        .module('app')
        .controller('Base', base);
        base.$inject = ['$http', '$location', '$mdSidenav'];
        function base($http, $location, $mdSidenav){
            var vm = this;
            vm.openMenu = openMenu;
            vm.focusSection = focusSection;
            vm.isActive = isActive;
            vm.hide = hide;

            $http.get('/api/base').then(function(response){
                vm.base = response.data;
            });
            $http.get('/api/menu').then(function(response){
                vm.menu = response.data;
            });

            function openMenu(){
                $mdSidenav('left').toggle();
            }
            function focusSection(){
                $mdSidenav('left').toggle();
            }

            function isActive(slug, pane){
                if (slug == $location.path().split('/')[1]){
                    if (!vm.init){
                        vm.init = 1;
                        pane.expand();
                    }
                    return 1
                }
            }
            function hide(){
                return angular.element(document.querySelector( '#animated')).hasClass('ng-enter-active') ;
            }
        }
})();