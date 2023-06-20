window.onload = function(){
    var btnFullScreen = document.getElementById('tela_cheia')
    
    // Verificar se o navegador suporta a API Fullscreen
    if (document.documentElement.requestFullscreen) {
        btnFullScreen.style.display = 'block'; // Mostrar o botão
        
        // Adicionar um evento de clique ao botão
        btnFullScreen.addEventListener('click', function() {
            if(document.fullscreenElement){
                if(document.exitFullscreen){
                    document.exitFullscreen();
                    btnFullScreen.textContent = 'Tela Cheia';
                }
            }
            else{
                if (document.documentElement.requestFullscreen) {
                    document.documentElement.requestFullscreen();
                    btnFullScreen.textContent = 'Sair da Tela Cheia';
                }
            }
        
        });
    }
}