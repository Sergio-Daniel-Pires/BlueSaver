window.onload = function () {
    $(document).ready(function() {
        $.ajax({
            url: "data",
            type: "GET",
            success: function(data) {
                var placeholder = data.place_holder;
                var facil = data.facil;
                var medio = data.medio;
                var dificil = data.dificil;

                facil.forEach(function(item) {
                    if (item.imagem === ""){
                        item.imagem = placeholder;
                    } 
                    $("#facil").append('<a href="#" class="item"><img onerror="this.src='+ "'" + placeholder + "';" + '"src="' + item.imagem + '" alt="' + item.texto + '"><p>' + item.texto + '</p></a>');
                });

                medio.forEach(function(item) {
                    $("#medio").append('<a href="#" class="item"><img onerror="this.src='+ "'" + placeholder + "';" + '"src="' + item.imagem + '" alt="' + item.texto + '"><p>' + item.texto + '</p></a>');
                });

                dificil.forEach(function(item) {
                    $("#dificil").append('<a href="#" class="item"><img onerror="this.src='+ "'" + placeholder + "';" + '"src="' + item.imagem + '" alt="' + item.texto + '"><p>' + item.texto + '</p></a>');
                });
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
}