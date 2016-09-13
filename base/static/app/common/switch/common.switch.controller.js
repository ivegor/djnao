(function(){
    'use strict';
    angular
        .module('app')
        .controller('Switch', base);
        base.$inject = ['$stateParams', '$http', '$location'];
        function base($stateParams, $http, $location){
            var vm = this;
            vm.cur_section = $stateParams.category + '/';
            $http.get('api/app/' + $stateParams.category).then(
                function(response){
                    vm.template = response.data['template'];
                    vm.content = response.data['content'];
                    vm.additional = response.data['additional']
                },
                function(){
                        $location.path("/");
                })
        }
})();
