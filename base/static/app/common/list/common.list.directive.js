(function () {
    'use strict';
    angular
        .module('app')
        .directive('onFinishRender', function ($timeout) {
            return {
                restrict: 'A',
                link: function (scope) {
                    if (scope.$last === true) {
                        $timeout(function () {
                            scope.$emit('ngRepeatFinished');
                            var quqntity=$(".item__sub_menu__left").size();
                            var widthScroll=0;
                            for (var i=0;i<quqntity;i++){
                                widthScroll+=$(".item__sub_menu__left:eq("+i+")").width();
                            }
                            $(".sub_menu__left").css('max-width', widthScroll+1);
                        });
                    }
                }
            }
        });
})();