(function () {
    'use strict';
    angular
        .module('app', ['ui.router', 'ngSanitize', 'ngAnimate'])
        .config(config);

    config.$inject = ['$stateProvider', '$urlRouterProvider', '$locationProvider'];
    function config($stateProvider, $urlRouterProvider, $locationProvider) {
        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state('home', {
                url: '/',
                templateUrl : '/static/views/home.html',
                controller  : 'HomeController',
                controllerAs : 'home'
            })
            .state('menu', {
                url: '/:category',
                templateUrl: '/static/views/listview.html',
                controller: 'ListController',
                controllerAs: 'list',
                abstract: true
            })
                .state('menu.list', {
                    url: '',
                    templateUrl: '/static/views/baselist.html'
                })
                .state('menu.detail', {
                    url: '/:page',
                    templateUrl: '/static/views/detailview.html',
                    controller: 'DetailController',
                    controllerAs: 'detail'
                });
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
    }
})();