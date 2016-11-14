(function() {'use strict';
    angular.module('app',[
	'ngCookies'
 ], function($interpolateProvider){
	// Contorna prroblema de interpola��o da renderiza��o de template do django
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
 })
 .run( function run($http, $cookies ){
	// Evita problemas relacionados ao CSRF
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
 });
})();