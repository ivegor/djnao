(function(){
   'use strict';
    angular
        .module('app')
        .controller('DetailController', DetailController);
    DetailController.$inject = ['$stateParams', 'Request'];
    function DetailController($stateParams, Request) {
        var vm = this;
        var detail = Request.getNewOrCachedData('menu/' + $stateParams.page);
        try{
            detail.success(function(data){
                vm.content = data['content'];
                vm.directive = data['directive']
            })
        } catch (TypeError){
            vm.content = detail['content'];
            vm.directive = detail['directive']
        }
    }
})();