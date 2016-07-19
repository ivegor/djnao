(function () {
    'use strict';
    angular
        .module('app', ['ui.router', 'ngSanitize', 'ngAnimate'])
        .config(function($stateProvider, $urlRouterProvider, $locationProvider) {
            $urlRouterProvider.otherwise('/');
            $stateProvider
                .state('home', {
                    url: '/',
                    templateUrl : '/static/views/home.html',
                    controller  : 'HomeController'
                })
                .state('menu', {
                    url: '/:category',
                    templateUrl: '/static/views/listview.html',
                    controller: 'ListController',
                    abstract: true
                })
                    .state('menu.list', {
                        url: '',
                        templateUrl: '/static/views/baselist.html'
                    })
                    .state('menu.detail', {
                        url: '/:page',
                        templateUrl: '/static/views/detailview.html',
                        controller: 'DetailController'
                    });
            $locationProvider.html5Mode(true);
            $locationProvider.hashPrefix('!');
        });


})();