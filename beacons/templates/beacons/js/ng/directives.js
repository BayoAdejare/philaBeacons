angular.module('MuseumApp')

.directive('topmenu', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    templateUrl: 'templates/topmenu.html',
    controller: 'topCtrl',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
.directive('firstscreen', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    templateUrl: 'templates/firstscreen.html',
    controller: 'topCtrl',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
.directive('swipescreen', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    templateUrl: 'templates/swipescreen.html',
    controller: 'topCtrl',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
.directive('navscreen', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    controller: 'topCtrl',
    templateUrl: 'templates/navscreen.html',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
.directive('infoscreen', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    controller: 'topCtrl',
    templateUrl: 'templates/infoscreen.html',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
.directive('commentscreen', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    controller: 'topCtrl',
    templateUrl: 'templates/commentscreen.html',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
.directive('sidenavright', function(NavData){
  return {
    restrict: 'E',
    scope: {},
    controller: 'rightCtrl',
    templateUrl: 'templates/sidenavright.html',
    link: {
    pre: function(scope, elem, attrs) {
          scope.navData = NavData;
        }
    }
  };  
})
;
