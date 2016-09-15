(function(){
    'use strict';
    angular
        .module('app')
        .controller('SwitchElement', base);
        base.$inject = ['$stateParams', '$http', '$location'];
        function base($stateParams, $http, $location){
            var vm = this;
            vm.cur_section = $stateParams.category;
            $http.get('api/app/' + $stateParams.category + '/' + $stateParams.id).then(
                function(response){
                    vm.template = response.data['template'];
                    vm.content = response.data['content']
                },
                function(){
                        $location.path("/");
                })
        }
})();
