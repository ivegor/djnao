(function(){
    'use strict';
    angular
        .module('app')
        .directive('defaultView', defaultView);
    function defaultView(){
        return {
            templateUrl: '/static/views/defaulview.html',
            restrict: 'A'
        }
    }
})();