(function(){
    'use strict';
    angular
        .module('app')
        .controller('staff', staff);
    staff.$inject = ['$scope', '$mdDialog', '$mdMedia', '$http', 'Likes'];
    function staff($scope, $mdDialog, $mdMedia, $http, Likes){
        var vm = this;
        var staffList = $scope.switch.content;
        var staffLikes = Likes.staff;
        var st;
        
        vm.category = ['администрация', 'педагоги', 'обслуживающий персонал'];
        vm.cur_cat = vm.category[0];
        vm.set_like = set_like;
        vm.show = show;

        for (var i = 0; i < staffList.length; i++){
            st = staffList[i];
            if (st.additionalinformation){
                st.like = !!staffLikes[st.id];
                st.additionalinformation.likes = staffLikes[st.id] || st.additionalinformation.likes
            }
        }

        function set_like(staff) {
            if (!staff.like){
                staff.additionalinformation.likes += 1;
                staffLikes[staff.id] = staff.additionalinformation.likes;
                $http.post('/api/like', {id: staff.id})
            }
            staff.like = true;
        }

        function show(ev, st) {
            var useFullScreen = $mdMedia('xs');
            $mdDialog.show({
                controller: DialogController,
                templateUrl: '/static/views/staff/desc.html',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose:true,
                fullscreen: useFullScreen,
                locals: {
                    staff: st
                }
            });
            function DialogController($scope, $mdDialog, staff) {
                $scope.hide = function() {
                    $mdDialog.hide();
                };
                $scope.cancel = function() {
                    $mdDialog.cancel();
                };
                $scope.staff = staff
            }
        }
    }
})();
