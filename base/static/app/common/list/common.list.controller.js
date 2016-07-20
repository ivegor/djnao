(function(){
    'use strict';
    angular
        .module('app')
        .controller('ListController', listView);

        listView.$inject = ['$stateParams', 'Request', '$location'];

        function listView($stateParams, Request, $location) {
            var vm = this;
            vm.currentUrl = $location.path();
            var menu = Request.getNewOrCachedData('menu/' + $stateParams.category);
            try{
                menu.success(function(data){
                    vm.menu = data['menu'];
                })
            } catch (TypeError){
                vm.menu = menu['menu']
            }
            vm.isActiveUrl = function(route) {
                return $location.path().split('/')[2] == route;
            };
        }
})();