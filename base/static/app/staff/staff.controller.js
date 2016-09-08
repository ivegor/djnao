(function(){
    'use strict';
    angular
        .module('app')
        .controller('staff', staff);
    staff.$inject = ['$mdDialog', '$mdMedia', '$http'];
    function staff($mdDialog, $mdMedia, $http){
        var vm = this;
        vm.category = ['администрация', 'педагоги', 'обслуживающий персонал'];
        vm.cur_cat = vm.category[0];
        vm.set_like = set_like;
        vm.show = show;

        function set_like(staff) {
            if (!staff.like){
                staff.additionalinformation.likes +=1;
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
