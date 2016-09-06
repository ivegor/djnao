(function(){
    'use strict';
    angular
        .module('app')
        .controller('Switch', base);
        base.$inject = ['$stateParams', 'Request', '$location'];
        function base($stateParams, Request, $location){
            var vm = this;
            var res = Request.getNewOrCachedData('app/' + $stateParams.category);
            try{
                res.then(function(response){
                    vm.template = response.data['template'];
                    vm.content = response.data['content']
                },
                    function(response){
                        $location.path("/");
                    })
            } catch (TypeError){
                vm.template = res['template'];
                vm.content = res['content']
            }
        }
})();
