(function(){
    'use strict';
    angular
        .module('app')
        .controller('ListController', listView);
        listView.$inject = [$scope, $stateParams, DataCache, $http, $location];

        function listView($scope, $stateParams, DataCache, $http, $location, getNewOrCachedData) {
            $scope.currentUrl = $location.path();
            //console.log(getNewOrCachedData('menu/' + $stateParams.category));
            $scope.menu = DataCache.get('menu/' + $stateParams.category);
            if (!$scope.menu) {
                var requestDetail = $http.get('/api/menu/' + $stateParams.category);
                requestDetail.success(function (response) {
                    DataCache.put('menu/' + $stateParams.category, response);
                    $scope.menu = response;
                });
            }
            $scope.isActiveUrl = function(route) {
                return $location.path().split('/')[2] == route;
            };
        }
})();