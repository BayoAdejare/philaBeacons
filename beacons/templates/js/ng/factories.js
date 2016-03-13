angular.module('MuseumApp')

.factory('NavData', function() {
 var currentNav = {
		firstscreen : true,
		swipescreen : false,
		navscreen : false,
		infoscreen : false,
		commentscreen : false,
		lastscreen : ''
	};
  return currentNav;
})
;