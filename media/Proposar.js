/*Añade classes y placeholdes al cargar la pagina*/
$(document).ready(function () {
            $("#id_titol").attr("placeholder", "Titol");
            $("#id_contingut").attr("placeholder", "Contingut");
            $("input").addClass("form-control");
            $(".submit").css("width","70px")
            $(".submit").css("margin","auto")

        })