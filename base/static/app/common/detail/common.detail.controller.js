(function(){
   'use strict';
    angular
        .module('app')
        .controller('DetailController', DetailController);
    DetailController.$inject = ['$stateParams', 'Request'];
    function DetailController($stateParams, Request) {
        var vm = this;
    }
})();