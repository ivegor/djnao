(function(){
    'use strict';
    angular
        .module('app')
        .service('NewsLikesService', newsLikes);
    newsLikes.$inject = [];
    function newsLikes(){
        var vm = this;
        vm.getLikes = getLikes;
        vm.setLikes = setLikes;
        vm.id_likes = {};

        function getLikes(id){
            return vm.id_likes[id]
        }
        function setLikes(id, likes){
            vm.id_likes[id] = likes;
        }
    }
})();