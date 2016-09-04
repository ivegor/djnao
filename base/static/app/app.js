(function () {
    'use strict';
    angular
        .module('app', ['ngMaterial', 'ui.router', 'ngSanitize', 'ngAnimate', 'vAccordion', 'angular-carousel'])
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider', '$locationProvider', '$httpProvider'];
    function config($stateProvider, $urlRouterProvider, $locationProvider, $httpProvider) {
        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state('home', {
                url: '/',
                templateUrl : '/static/views/home.html',
                controller  : 'HomeController',
                controllerAs : 'home'
            })
            .state('category', {
                url: '/:category',
                templateUrl : '/static/views/switch.html',
                controller  : 'Switch',
                controllerAs : 'switch'
            });
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');

        $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
})();