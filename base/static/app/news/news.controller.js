(function(){
    'use strict';
    angular
        .module('app')
        .controller('NewsController', news);
    news.$inject = ['$scope', '$http', 'Likes', '$mdMedia'];
    function news($scope, $http, Likes, $mdMedia){
        var vm = this;
        var newsObj = $scope.switch.content;
        var newsLikes = Likes.news;
        var cur_likes = newsLikes[newsObj.id];

        vm.set_like = set_like;
        vm.size = $mdMedia;

        newsObj.like  = !!cur_likes;
        newsObj.additional.likes = cur_likes || newsObj.additional.likes;

        function set_like(news) {
            if (!news.like){
                news.additional.likes +=1;
                newsLikes[news.id] = news.additional.likes;
                $http.post('/api/news_like', {id: news.id})
            }
            news.like = true;
        }
    }
})();