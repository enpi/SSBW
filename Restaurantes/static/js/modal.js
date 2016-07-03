var app = angular.module( "Modulo", [ "ngAnimate", 'ui.bootstrap' ] );

app.controller("AppController", function( $scope, $modal ) {

    $scope.openModal = function(){
                            var modal = $modal.open({templateUrl:"login", controller:"controlador"})
                            }

 });

 app.controller("controlador", function($scope, $modalInstance)){
    $scope

 }

