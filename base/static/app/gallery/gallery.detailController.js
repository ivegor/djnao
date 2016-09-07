(function(){
    'use strict';
    angular
        .module('app')
        .controller('GalleryDetailController', GalleryDetail);
    GalleryDetail.$inject = ['Carousel', '$mdDialog', '$mdMedia'];

    function GalleryDetail(Carousel, $mdDialog, $mdMedia) {
        var vm = this;
        vm.carousel = Carousel;
        vm.size = $mdMedia;
        vm.show = function(ev, gals, index, car) {
            var useFullScreen = $mdMedia('xs');
            $mdDialog.show({
                controller: DialogController,
                templateUrl: '/static/views/gallery_slider.html',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose:true,
                fullscreen: useFullScreen,
                locals: {
                    gals: gals,
                    init: index,
                    car: car
                }
            });
            function DialogController($scope, $mdDialog, gals, init, car) {
                $scope.hide = function() {
                    $mdDialog.hide();
                };
                $scope.cancel = function() {
                    $mdDialog.cancel();
                };
                $scope.gallery = gals;
                $scope.init = init;
                $scope.car = car;
                $scope.hi = function(){console.log('hi')};
            }
        };

    }
})();