/*Añade classes y placeholdes al cargar la pagina*/
$(document).ready(function(){
    $("#id_textcuriositat").attr("placeholder", "Escriu el teu comentari...");
    $( "#id_textcuriositat" ).addClass( "form-control comentari" )
})

/*Funcion para buscar las curiosidades utilizando ajax*/
function buscador() {
    text = $("#buscador").val()
    /*Evitamos que haga una peticion si el input esta vacio*/
    if (text!=""){
        console.log(text)
        /*Hacemos la peticion ajax*/
        $.get("/buscador?busca="+text,function (data) {
            console.log(data)
            $("#buscador-curiositats").children().remove()
            /*Añadimos a la lista los resultados*/
            $.each(data, function (index, element) {
                console.log(element)
                a = $("<a href=\"/curiositat/"+element.id+"\">")
                divcurio = $("<div class=\"curiositatbiblio\">")
                img = $("<img class=\"imagebiblio\" src=\""+element.imatge+"\">")
                div = $("<div class=\"col-xs-1\" align=\"center\" id=\"titolbiblio\">"+element.titol+"</div>")
                divcurio.append(img)
                divcurio.append(div)
                a.append(divcurio)
                $("#buscador-curiositats").append(a)
                $("#buscador-curiositats").append($("<hr>"))
            })
        })
    }
}
