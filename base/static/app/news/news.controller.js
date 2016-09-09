(function(){
    'use strict';
    angular
        .module('app')
        .controller('NewsController', news);
    news.$inject = ['$scope', '$http', 'NewsLikesService'];
    function news($scope, $http, NewsLikesService){
        var vm = this;
        vm.set_like = set_like;
        var cur_likes = NewsLikesService.getLikes($scope.switch.content.id);
        $scope.switch.content.like  = cur_likes;
        $scope.switch.content.additional.likes = cur_likes || $scope.switch.content.additional.likes;

        function set_like(news) {
            if (!news.like){
                news.additional.likes +=1;
                NewsLikesService.setLikes(news.id, news.additional.likes);
                $http.post('/api/news_like', {id: news.id})
            }
            news.like = true;
        }
    }
})();