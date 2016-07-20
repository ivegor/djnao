(function () {
    'use strict';
    angular
        .module('app')
        .factory('Request', Request);

    Request.$inject = ['$http', 'DataCache'];

    function Request($http, DataCache){
        return {
            getNewOrCachedData: getNewOrCachedData
        };

        function getNewOrCachedData(path){
            function request(){
                return $http.get('/api/' + path).success(function(response){
                    DataCache.put(path, response);
                    return response
                })
            }
            return DataCache.get(path) || request()
        }
    }
})();