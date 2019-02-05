function proposar(){
    $(".js").show();
}
$(document).ready(function(){ 
  
    $("#textcuriositat").attr("placeholder", "Escriu la teva curiositat");
    
    $( "#textcuriositat" ).addClass( "form-control text" );
    $( "#selectorimage" ).addClass( "btn btn-light iniciarsessiobutton" );
    $( "#selecciona" ).addClass( "form-control col-lg-10");
    $( "#novacategoria" ).addClass( "form-control col-lg-10" );
})