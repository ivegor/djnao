(function(){
   'use strict';
    angular
        .module('app')
        .controller('DetailController', function ($scope, $stateParams, DataCache, $http, $location) {

            $scope.detail = DataCache.get('detail' + $stateParams.page);
            if (!$scope.detail) {
                var requestDetail = $http.get('/api/detail/' + $stateParams.page);
                requestDetail.success(function (response) {
                    DataCache.put('detail' + $stateParams.page, response);
                    $scope.detail = response;
                });
            }
            // $http.get('/api/staff').success(function(response){console.log(response); $scope.detail=response})
            // $scope.set = function(){return '/static/views/staff.html'}
        });
})();