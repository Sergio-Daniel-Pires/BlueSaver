function toggleFullscreen(){
    var btnFullScreen = document.getElementById('tela_cheia')
    
    if(document.fullscreenElement){
        document.exitFullscreen();
        btnFullScreen.textContent = 'Tela Cheia'; 
    }
    else{
        document.documentElement.requestFullscreen();
        btnFullScreen.textContent = 'Sair da Tela Cheia'; 
    }
}