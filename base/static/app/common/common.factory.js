(function () {
    'use strict';
    angular
        .module('app')
        .factory('DataCache', DataCache)
        .factory('getNewOrCachedData', getNewOrCachedData);

    DataCache.$inject =[$cacheFactory];
    function DataCache ($cacheFactory) {
            return $cacheFactory('dataCache', {});
    }

    function getNewOrCachedData(path){
        getData.$inject = [$http, DataCache];
        function getData(path, $http, DataCache){
            function request(){
                return $http.get('/api/' + path).success(function(response){
                    DataCache.put(path, response);
                    return response
                })
            }
            return DataCache.get(path) || request()
        }
        return getData
    }
})();
