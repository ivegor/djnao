(function(){
    'use strict';
    angular
        .module('app')
        .directive('staff', staff);
    staff.$inject = [];
    function staff(){
        return {
            require: 'ngInclude',
            templateUrl: '/static/views/staff.html'
        }
    }

})();
