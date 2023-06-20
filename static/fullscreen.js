window.onload= function(){
    var fullscreenButton = document.getElementById('tela_cheia');

    // Verificar se o navegador suporta a API Fullscreen
    if (document.documentElement.requestFullscreen) {
        fullscreenButton.style.display = 'block'; // Mostrar o botão
    
        // Adicionar um evento de clique ao botão
        fullscreenButton.addEventListener('click', function() {
            if(document.fullscreenElement){
                if(document.exitFullscreen){
                    document.exitFullscreen();
                }
            }
            else{
                if (document.documentElement.requestFullscreen) {
                    document.documentElement.requestFullscreen();
                }
            }
        
        });
    }
}