(function () {
    'use strict';
    angular
        .module('app')
        .directive('onFinishRender', function ($timeout, $parse) {
            return {
                restrict: 'A',
                link: function (scope, el, attr) {
                    if (scope.$last === true) {
                        $timeout(function () {
                            if(!!attr.onFinishRender){
                                $parse(attr.onFinishRender)(scope);
                            }
                        });
                    }
                }
            }
        });
})();