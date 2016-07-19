(function(){
    'use strict';
    angular
        .module('app')
        .controller('HomeController', ['$scope', '$http', 'DataCache', function($scope, $http, DataCache) {
            $scope.slider = DataCache.get('slider');
            if (!$scope.slider) {
                var request = $http.get('/api/slider');
                request.success(function (response) {
                    DataCache.put('slider', response);
                    $scope.slider = response;
                });
            }
        }]);
})();