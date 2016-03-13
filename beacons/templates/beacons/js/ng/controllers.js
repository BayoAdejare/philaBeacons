'use strict';
angular.module('MuseumApp',['ngMaterial', 'ngMessages', 'ngAnimate'])

.controller('topCtrl', function ($scope, $timeout, $mdSidenav, $log, NavData) {
	$scope.currentNav = NavData;
	$scope.swipeBack = function() {
		$scope.currentNav.swipescreen = false;
		$scope.currentNav.firstscreen = true;
	};
	$scope.navBack = function() {
		$scope.currentNav.navscreen = false;
		$scope.currentNav.swipescreen = true;
	};
	$scope.infoBack = function() {
		$scope.currentNav.infoscreen = false;
		$scope.currentNav.navscreen = true;
	};
	$scope.commentBack = function() {
		$scope.currentNav.commentscreen = false;
		$scope.currentNav.infoscreen = true;
	};
	$scope.toggleRight = buildToggler('right');
	$scope.isOpenRight = function(){
	  return $mdSidenav('right').isOpen();
	};
	/*
	 * Build handler to open/close a SideNav; when animation finishes
	 * report completion in console
	 */

	function buildToggler(navID) {
	  return function() {
	    $mdSidenav(navID)
	      .toggle()
	      .then(function () {
	        $log.debug("toggle " + navID + " is done");
	      });
	  }
	}
    $scope.todos = [
      {
        face : "img/face.png",
        what: 'Brunch this weekend?',
        who: 'Min Li Chan',
        when: '3:08PM',
        notes: " I'll be in your neighborhood doing errands"
      },
      {
        face : "img/face.png",
        what: 'Brunch this weekend?',
        who: 'Min Li Chan',
        when: '3:08PM',
        notes: " I'll be in your neighborhood doing errands"
      },
      {
        face : "img/face.png",
        what: 'Brunch this weekend?',
        who: 'Min Li Chan',
        when: '3:08PM',
        notes: " I'll be in your neighborhood doing errands"
      },
      {
        face : "img/face.png",
        what: 'Brunch this weekend?',
        who: 'Min Li Chan',
        when: '3:08PM',
        notes: " I'll be in your neighborhood doing errands"
      },
      {
        face : "img/face.png",
        what: 'Brunch this weekend?',
        who: 'Min Li Chan',
        when: '3:08PM',
        notes: " I'll be in your neighborhood doing errands"
      },
    ];
})

.controller('rightCtrl', function ($scope, $timeout, $mdSidenav, $log) {
$scope.close = function () {
  $mdSidenav('right').close()
    .then(function () {
      $log.debug("close RIGHT is done");
    });

    };
  })
.controller('timeCtrl', function($scope) {
	$scope.totalTime= 4;
	$scope.artTime= 30;
})
.controller('customKeyInputCtrl', keyInputCtrl);
 
  function keyInputCtrl ($scope, $timeout, $q) {
    $scope.music = {
		selected: [],
		songs: [{
			id: 1,
			title: "Easy Like a Sunday Morning",
			artist: "Lionel Richie"
		},{
			id: 2,
			title: "Sorry",
			artist: "Justin Bieber"
		},{
			id: 3,
			title: "Let it Be",
			artist: "The Beatles"
		},{
			id: 4,
			title: "Symphony 5",
			artist: "Beetoven"
		},{
			id: 5,
			title: "Beat It",
			artist: "Micheal Jackson"
		},{
			id: 6,
			title: "Elton John",
			artist: "Mona Lisa Smile"
		}]
	};
	$scope.emos = {
		selected: [],
		options: [{
			id: 1,
			filters: ["innocent", "cute", "sweet", "religious", "christian"],
			icon: "angel.svg",
			name: "Angel"
		},{
			id: 2,
			filters: ["mad", "outrage", "sour", "dark"],
			icon: "angry.svg",
			name: "Angry"
		},{
			id: 3,
			filters: ["bald", "hair", "cover"],
			icon: "cap.svg",
			name: "Cap"
		},{
			id: 4,
			filters: ["funny", "scary", "balloon", "red", "silly"],
			icon: "clown.svg",
			name: "Clown"
		},{
			id: 5,
			filters: ["scattered", "disconnect", "broken", "dazed", "mixed"],
			icon: "confused.svg",
			name: "Confused"
		},{
			id: 6,
			filters: ["popular", "chill", "blue", "dazed", "stylish"],
			icon: "cool.svg",
			name: "Cool"
		},{
			id: 7,
			filters: ["sad", "unhappy", "blue", "tears"],
			icon: "crying.svg",
			name: "Crying"
		},{
			id: 8,
			filters: ["tech", "connected", "web", "digital", "computer"],
			icon: "cyber.svg",
			name: "Cyber"
		},{
			id: 9,
			filters: ["blue", "artist", "twenties", "dark", "funk"],
			icon: "depression.svg",
			name: "Depression"
		},{
			id: 10,
			filters: ["negative", "ugly", "creepy", "hate", "scorn"],
			icon: "dislike.svg",
			name: "Dislike"
		},{
			id: 11,
			filters: ["vision", "lens", "geek", "nerd", "smart"],
			icon: "eyeglass.svg",
			name: "Eyeglass"
		},{
			id: 12,
			filters: ["happy", "festive", "cheerful", "brave", "colorful"],
			icon: "gay.svg",
			name: "Gay"
		},{
			id: 13,
			filters: ["Unusual", "tech", "glasses"],
			icon: "geek.svg",
			name: "Geek"
		},{
			id: 14,
			filters: ["bright", "yellow", "colorful", "light", "rejoice"],
			icon: "happy.svg",
			name: "Happy"
		},{
			id: 15,
			filters: ["laugh", "funny", "dirty", "whimsy", "joke"],
			icon: "humor.svg",
			name: "Humor"
		},{
			id: 16,
			filters: ["kiss", "romance", "embrace", "love", "greeting"],
			icon: "kiss.svg",
			name: "Kiss"
		},{
			id: 17,
			filters: ["funny", "joke", "comic", "humor"],
			icon: "laughing.svg",
			name: "Laughing"
		},{
			id: 18,
			filters: ["happy", "cute", "sweet", "interest", "bright"],
			icon: "like.svg",
			name: "Like"
		},{
			id: 19,
			filters: ["kiss", "romance", "desire", "heat", "connection"],
			icon: "love.svg",
			name: "Love"
		},{
			id: 20,
			filters: ["green", "greed", "paper", "happy", "coins"],
			icon: "money.svg",
			name: "Money"
		},{
			id: 21,
			filters: ["whimsical", "old fashioned", "hipster", "lighthearted", "carefree"],
			icon: "mustache.svg",
			name: "mustache"
		},{
			id: 22,
			filters: ["rebelious", "punk", "rock", "dissent", "alternative", "edgy"],
			icon: "punk.svg",
			name: "punk"
		},{
			id: 23,
			filters: ["stiff", "mechanical", "cold", "futuristic", "robotic"],
			icon: "robot.svg",
			name: "robot"
		},{
			id: 24,
			filters: ["safe", "defensive", "stable", "confident", "assured"],
			icon: "security.svg",
			name: "security"
		},{
			id: 25,
			filters: ["tired", "drowsy", "silent", "dark", "dreamy", "restful"],
			icon: "sleepi.svg",
			name: "sleepy"
		},{
			id: 26,
			filters: ["intelligent", "nerdy", "quick", "bright", "difficult"],
			icon: "smart.svg",
			name: "smart"
		},{
			id: 27,
			filters: ["happy", "upbeat", "approachable", "radiant", "content"],
			icon: "smile.svg",
			name: "smile"
		},{
			id: 28,
			filters: ["best", "top", "ultimate", "winner", "standout", "masterpiece"],
			icon: "star.svg",
			name: "star"
		},{
			id: 29,
			filters: ["cool", "chill", "relaxed", "sunny", "carefree", "casual"],
			icon: "sunglass.svg",
			name: "sunglass"
		},{
			id: 30,
			filters: ["cool", "chill", "relaxed", "sunny", "carefree", "casual"],
			icon: "sunglass_2.svg",
			name: "sunglass_2"
		},{
			id: 31,
			filters: ["cool", "chill", "relaxed", "sunny", "carefree", "casual"],
			icon: "sunglass_3.svg",
			name: "sunglass_3"
		},{
			id: 32,
			filters: ["shocking", "unexpected", "wonder", "disbelief", "astound", "stun"],
			icon: "surprise.svg",
			name: "surprise"
		},{
			id: 33,
			filters: ["playful", "silly", "mocking", "frivolous", "insignificant", "unimportant"],
			icon: "tongue.svg",
			name: "tongue"
		},{
			id: 34,
			filters: ["kidding", "flirty", "provocative", "coy", "teasing", "enticing"],
			icon: "wink.svg",
			name: "wink"
		}]
	};
    var self = this;

    self.readonly = false;
    self.selectedItem = null;
    self.searchText = null;
    self.querySearch = querySearch;
    self.keywords = loadKeywords();
    self.selectedKeywords = [];
    self.numberChips = [];
    self.numberChips2 = [];
    self.numberBuffer = '';
    self.autocompleteRequireMatch = false;
    self.transformChip = transformChip;
    self.transformChipMusic = transformChipMusic;
    self.transformChipEmo = transformChipEmo;
    self.music = $scope.music;
    self.emos = $scope.emos;

    /**
     * Return the proper object when the append is called.
     */
    function transformChip(chip) {
      // If it is an object, it's already a known chip
      if (angular.isObject(chip)) {
        return chip;
      }

      // Otherwise, create a new one
      return { name: chip, type: 'new' }
    }
    function transformChipMusic(chip1, chip2) {

      // Otherwise, create a new one
      return { name: 'chip1+'-'+chip2, '+chip2, type: 'music' }
    }function transformChipEmo(chip) {

      // Otherwise, create a new one
      return { name: 'Emo: '+chip, type: 'emo' }
    }

    /**
     * Search for vegetables.
     */
    function querySearch (query) {
      var results = query ? self.keywords.filter(createFilterFor(query)) : [];
      return results;
    }

    /**
     * Create filter function for a query string
     */
    function createFilterFor(query) {
      var lowercaseQuery = angular.lowercase(query);

      return function filterFn(keyword) {
        return (keyword._lowername.indexOf(lowercaseQuery) === 0) ||
            (keyword._lowertype.indexOf(lowercaseQuery) === 0);
      };

    }

    function loadKeywords() {
      var keyWd = [
        {
          'name': 'Happy',
          'type': 'text'
        },
        {
          'name': 'Sad',
          'type': 'text'
        },
        {
          'name': 'Rebelious',
          'type': 'text'
        },
        {
          'name': 'Inspired',
          'type': 'text'
        },
        {
          'name': 'Mischevious',
          'type': 'text'
        }
      ];

      return keyWd.map(function (keyw) {
        keyw._lowername = keyw.name.toLowerCase();
        return keyw;
      });
    }
}
;