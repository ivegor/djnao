(function(){
   'use strict';
    angular
        .module('app')
        .controller('DetailController', DetailController);
    DetailController.$inject = ['$stateParams', 'Request'];
    function DetailController($stateParams, Request) {
            var vm = this;
            var detail = Request.getNewOrCachedData('detail/' + $stateParams.page);
            try{
                detail.success(function(data){
                    vm.detail = data;
                })
            } catch (TypeError){
                vm.detail = detail
            }
        }
})();