window.onload = function () {
    $(document).ready(function() {
        $.ajax({
            url: "data",
            type: "GET",
            success: function(data) {
                var placeHolder = data.place_holder;
                // Dispensable, tinha trechos praticamente identicos para cada dificuldade, 
                // Refatorado utilizando a função ao inves de copiar e colar com if
                // Eu acho que isso se tornaria um Bloater que eu poderia refatorar com for
                // Mas por conta da A4.2, não irei.
                addHint(data.facil, "#facil", placeHolder);
                addHint(data.medio, "#medio", placeHolder);
                addHint(data.dificil, "#dificil", placeHolder);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
}

function addHint(categoria, objId, placeHolder){
    categoria.forEach(function(item) {
        if (item.imagem === ""){
            item.imagem = placeHolder;
        } 
        $(objId).append('<a href="#" class="item"><img onerror="this.src='+ "'" + placeHolder + "';" + '"src="' + item.imagem + '" alt="' + item.texto + '"><p>' + item.texto + '</p></a>');
    });
}