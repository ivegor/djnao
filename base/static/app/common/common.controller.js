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
                return 0
            };
            vm.isSectionSelected = function(mainMenu){
                for (var ob in mainMenu.sub_menus){
                    var active = mainMenu.sub_menus[ob]['slug'] == $location.path().split('/')[1]
                    if (active){
                        return 1
                    }
                }
                return 0
            };
            vm.toggleMenu = function(){

            };
            $scope.initOpen =  function(){

                for (var ob in sub_menus){
                    var active = sub_menus[ob]['slug'] == $location.path().split('/')[1];
                    if (active){
                        return 1
                    }
                }
                return 0
            };
            vm.isActive = function(slug, pane){
                if (slug == $location.path().split('/')[1]){
                    if (!vm.init){
                        vm.init = 1;
                        pane.expand();
                    }
                    return 1
                }
            }
        }
})();