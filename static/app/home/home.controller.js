(function(){
    'use strict';
    angular
        .module('app')
        .controller('HomeController', HomeController);
    HomeController.$inject = ['$http', 'Carousel'];

    function HomeController($http, Carousel) {
            var vm = this;
            $http.get('/api/slider').then(function (response) {
                    vm.slider = response.data
            });
            vm.carousel = Carousel;
        }
})();