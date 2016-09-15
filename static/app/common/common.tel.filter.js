(function(){
    'use strict';
    angular
        .module('app')
        .filter('tel',tel)
        .filter('limit_from_size', limit_from_size)
        .filter('multiple_select', multiple_select);
    limit_from_size.$inject = ['$mdMedia'];

    function limit_from_size($mdMedia) {
        return function (text) {
            if ($mdMedia('xs') && text.length > 100){
                return text.slice(0,100) + '...'
            }
            return text
        }
    }

    function tel() {
        return function(tel){
            var value = String(tel).trim().replace(/^\+/, '');
            switch(value.length){
                case 11:
                    return ['+7', value.slice(1, 4), value.slice(4, 7), value.slice(7, 9), value.slice(9, 11)].join('-');
                case 10:
                    return ['+7', value.slice(0, 3), value.slice(3, 6), value.slice(6, 8), value.slice(8, 10)].join('-');
                case 5:
                    return [value.slice(0, 1), value.slice(1, 3), value.slice(3, 5)].join('-');
                default:
                    return tel
            }
        }
    }
    function multiple_select() {
        return function (cur, arr, attr) {
            if (!attr){
                attr = '$'
            }
            if(!arr || !arr[0]){
                return cur
            }
            var filtered = [];
            angular.forEach(cur, function (item) {
                if (arr.indexOf(item[attr]) != -1){
                    filtered.push(item)
                }
            });
            return filtered
        }
    }
})();
