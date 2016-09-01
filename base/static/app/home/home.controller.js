(function(){
    'use strict';
    angular
        .module('app')
        .controller('HomeController', HomeController);
    HomeController.$inject = ['$http', 'DataCache', 'Carousel'];

    function HomeController($http, DataCache, Carousel) {
            var vm = this;
            vm.slider = DataCache.get('slider');
            if (!vm.slider) {
                var request = $http.get('/api/slider');
                request.success(function (response) {
                    DataCache.put('slider', response);
                    vm.slider = response;
                });
            }
            vm.carousel = Carousel;
        }
})();