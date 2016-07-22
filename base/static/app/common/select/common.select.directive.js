(function(){
    'use strict';
    angular
        .module('app')
        .directive('selectpicker', selectpicker);
    function selectpicker() {
        return {
        restrict: 'A',
        priority: 1000,
        link: function (scope, element, attrs) {
            var e = $('.selectpicker');
            scope.$watch(attrs.ngModel, function(n, o){
              e.selectpicker('refresh');
            });
        }
    };
  }
})();
