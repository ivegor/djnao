(function () {
    'use strict';
    angular
        .module('app')
        .animation('.animate_for_footer', function ($animateCss) {
            return {
                leave: function(element){
                    var ac = $('.animate-container');
                    ac.css('min-height',$('.animate').height());
                    setTimeout(function(){ac.css('min-height', '')} , 1000);
                    $('footer').animate(
                        {bottom:"-=300", position: 'absolute', opacity: 0}, 1000)
                                .animate(
                        {bottom:"+=300", opacity: 1}, 300);
                    return $animateCss(element, {
                        event: 'leave',
                        structural: true
                        });
                    }
                }
            });
})();