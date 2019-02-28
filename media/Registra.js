$(document).ready(function(){ 
  
    $("#id_correu").attr("placeholder", "Email");
    $("#id_username").attr("placeholder", "Nom d'usuari");
    $("#id_password1").attr("placeholder", "Contrasenya");
    $("#id_password2").attr("placeholder", "Confirma contrasenya");

    $( "#id_correu" ).addClass( "form-control" );
    $( "#id_username" ).addClass( "form-control" );
    $( "#id_password1" ).addClass( "form-control" );
    $( "#id_password2" ).addClass( "form-control" );
    $( "#id_imatge" ).addClass( "btn btn-light iniciarsessiobutton" );
})