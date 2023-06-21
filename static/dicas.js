window.onload = function () {
    $(document).ready(function() {
        $.ajax({
            url: "data",
            type: "GET",
            success: function(data) {
                var placeholder = data.place_holder;
                var categorias = [data.facil, data.medio, data.dificil];
                var ids = ["#facil", "#medio", "#dificil"];
                
                // Bloaters, Se tivessem +10 dificuldades, não deveriam ter +10 forEach, reduzido para forEach dinamico.
                categorias.forEach(function(categoria, index) {
                    categoria.forEach(function(item) {
                        if (item.imagem === ""){
                            item.imagem = placeholder;
                        } 
                        $(ids[index]).append('<a href="#" class="item"><img onerror="this.src='+ "'" + placeholder + "';" + '"src="' + item.imagem + '" alt="' + item.texto + '"><p>' + item.texto + '</p></a>');
                    });
                });
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
}