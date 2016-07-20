(function(){
    'use strict';
    angular
        .module('app')
        .filter('tel', function () {
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
        });

})();