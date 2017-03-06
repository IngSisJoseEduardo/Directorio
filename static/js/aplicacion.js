
$(document).ready(function(){
    var alto = $( window ).height();
    var salto = (alto-185)+"px";

    $("#table-list").css("max-height",salto);
    $("#table-milista").css("max-height",salto);
    $("#preview-detalle").css("max-height",salto);

    $('select').material_select();

    $('.searchable').multiSelect({
        selectableHeader: "<input type='text' class='search-input form-control' autocomplete='off' placeholder='ejemplo. Lic. josé'>",
        selectionHeader: "<input type='text' class='search-input form-control' autocomplete='off' placeholder='ejemplo. Lic. josé'>",
        afterInit: function(ms){
        var that = this,
            $selectableSearch = that.$selectableUl.prev(),
            $selectionSearch = that.$selectionUl.prev(),
            selectableSearchString = '#'+that.$container.attr('id')+' .ms-elem-selectable:not(.ms-selected)',
            selectionSearchString = '#'+that.$container.attr('id')+' .ms-elem-selection.ms-selected';

        that.qs1 = $selectableSearch.quicksearch(selectableSearchString)
        .on('keydown', function(e){
          if (e.which === 40){
            that.$selectableUl.focus();
            return false;
          }
        });

        that.qs2 = $selectionSearch.quicksearch(selectionSearchString)
        .on('keydown', function(e){
          if (e.which == 40){
            that.$selectionUl.focus();
            return false;
          }
        });
        },
        afterSelect: function(){
        this.qs1.cache();
        this.qs2.cache();
        },
        afterDeselect: function(){
        this.qs1.cache();
        this.qs2.cache();
        }
        });
});


//funciones
function detalle(ruta){
    // $('#preview-detalle').load(ruta);
    $.ajax({
        type: "GET",
        url: ruta,
        success: function(a) {
                $('#preview-detalle').html(a);
        }
       });
    console.log("ajax");
}

function agregar(ruta){
    $.ajax({
        type: "GET",
        url: ruta,
        success: function(a){
            $('#mensaje-añadir').html(a);
            $('#btn-agregar').hide();
            // $("#accion").html('<a href="javascript:void();" class="btn">Quitar<a>')            
        }
    });
    console.log("añadir");
}
function quitar(ruta){
    $.ajax({
        type :"GET",
        url : ruta,
        success : function(a){
            $('#mensaje-añadir').html(a);
            $("#btn-quitar").hide();
            // $('#accion').html('<a href="javascript:void();" class = "btn">Añadir</a>');
        }
    });
}

function acuses_mi_lista(ruta,tipo){
    $('#tipo').val("acus");
    $('#form_multiple').submit();
}

function etiquetas_mi_lista(){
    $('#tipo').val("eti");
    $('#form_multiple').submit();   
}

function lista_mi_lista(){
    $('#tipo').val("lista");
    $('#form_multiple').submit();   
}

function agregar_entregados(ruta){
    libro = $("#libro").val();
    cantidad = $("#cantidad").val();
    datos = $("#form_agregar").serialize();
    if (libro != 0 && cantidad != 0) {
        $.ajax({
            type: "POST",
            url: ruta,
            data: datos,
            success: function(a) {
                    obs = $('#libro option:selected').text()
                    $('#tabla_obsequio').html(a);
                    $('#cantidad').val(0)
                    $("#infomensaje").html("<h5 style = 'color:green;'>!Información de "+obs+" actualizada¡</h5>")
                    
            }
           });
    }
    else{
        $("#infomensaje").html("<h5 style = 'color:red;'>!Selecciona un Obsequio y pon una cantidad¡</h5>")
    }   
}

//envia el formulario de la pagina de reportes a la vista en Django
function lista_entregados_word(){
    $('#tipo').val("entregado");
    $('#form-reportes').submit();
}
function lista_pendientes_word(){
    $('#tipo').val("pendiente");
    $('#form-reportes').submit();
}
function lista_no_autorizados(){
    $('#tipo').val("noautorizado");
    $('#form-reportes').submit();
}