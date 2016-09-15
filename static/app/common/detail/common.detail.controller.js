(function(){
   'use strict';
    angular
        .module('app')
        .controller('DetailController', DetailController);
    DetailController.$inject = ['$stateParams'];
    function DetailController($stateParams) {
        var vm = this;
    }
})();