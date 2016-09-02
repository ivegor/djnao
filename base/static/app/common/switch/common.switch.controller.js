(function(){
    'use strict';
    angular
        .module('app')
        .controller('Switch', base);
        base.$inject = ['$stateParams', 'Request'];
        function base($stateParams, Request){
            var vm = this;
            var res = Request.getNewOrCachedData('app/' + $stateParams.category);
            try{
                res.success(function(data){
                    vm.template = data['template'];
                    vm.content = data['content']
                })
            } catch (TypeError){
                vm.template = res['template'];
                vm.content = res['content']
            }
        }
})();
