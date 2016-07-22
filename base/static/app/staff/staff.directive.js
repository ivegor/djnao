(function(){
    'use strict';
    angular
        .module('app')
        .directive('staff', staff);
    staff.$inject = [];
    function staff(){
        return {
            templateUrl: '/static/views/staff.html',
            restrict: 'A'
        }
    }
})();
