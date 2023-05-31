window.onload = function () {
    document.getElementById("idade").addEventListener("change", function () {
        var idadeSelecionada = this.value;

        // Remove o conteúdo anterior do container
        $("#imagem-container").html("");

        if (idadeSelecionada) {
            // Cria o elemento iframe com a imagem
            $.ajax({
                url: '/graficos/' + idadeSelecionada,
                type: 'GET',
                success: function(response){
                    console.log(response)
                    $("#imagem-container").html(response);
                }
            });
        }
    });
}