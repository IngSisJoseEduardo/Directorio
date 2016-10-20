
$(document).ready(function(){
    var alto = $( window ).height();
    var salto = (alto-160)+"px";
    
    $("#table-list").css("max-height",salto);
    $("#table-milista").css("max-height",salto);
    $("#preview-detalle").css("max-height",salto);

    

});

//funciones
function detalle(ruta){
    $('#preview-detalle').load(ruta);
}