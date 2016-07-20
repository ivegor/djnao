(function () {
    'use strict';
    angular
        .module('app')
        .factory('DataCache', DataCache);

    DataCache.$inject =['$cacheFactory'];
    function DataCache ($cacheFactory) {
            return $cacheFactory('dataCache', {});
    }
})();
