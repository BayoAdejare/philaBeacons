angular.module('MuseumApp', ['ngMaterial'])
.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('orange')
    .accentPalette('orange');
});