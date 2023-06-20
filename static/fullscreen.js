window.onload= function(){
    var fullscreenButton = document.getElementById('tela_cheia');
    var cookie= document.cookie("tela_cheia=false");

    // Verificar se o navegador suporta a API Fullscreen
    if (document.documentElement.requestFullscreen) {
        fullscreenButton.style.display = 'block'; // Mostrar o botão

        // Verificar se há um cookie salvo para a tela cheia
        //var fullscreenCookie = getCookie('tela_cheia');
        //var isFullscreen = fullscreenCookie === 'true';
        //setFullscreen(isFullscreen); // Configurar o estado inicial
        
       
        // Adicionar um evento de clique ao botão
        fullscreenButton.addEventListener('click', function() {
            if(document.fullscreenElement){
                if(document.exitFullscreen){
                    document.exitFullscreen();
                    cookie= document.cookie("tela_cheia=true");
                     
                }
            }
            else{
                if (document.documentElement.requestFullscreen) {
                    document.documentElement.requestFullscreen();
                    setFullscreen(true);
                    cookie= document.cookie("tela_cheia=true");
                }
            }
        
        });
    }
    
    function setFullscreen(isFullscreen) {
        if (isFullscreen) {
        fullscreenButton.textContent = 'Sair da Tela Cheia';
        } else {
        fullscreenButton.textContent = 'Tela Cheia';
        }
    }

    function getCookie(name) {
        var cookieName = name + '=';
        var cookieArray = document.cookie.split(';');
        for (var i = 0; i < cookieArray.length; i++) {
          var cookie = cookieArray[i];
          while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
          }
          if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length, cookie.length);
          }
        }
        return '';
    }
    /*
    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.startsWith(name + '=')) {
            return cookie.substring(name.length + 1);
          }
        }
        return null;
    }
    */

}