window.onload = function () {
    $(document).ready(function () {
        carregarDadosQuiz();

        // Evento de clique nos botões de dificuldade
        $('.btn-dificuldade').click(function () {
            dificuldade = $(this).data('dificuldade');

            // Remove todas as classes de cor dos botões de dificuldade
            $('.btn-dificuldade').removeClass('btn-success btn-warning btn-danger');

            // Adiciona a classe de cor correta com base na dificuldade selecionada
            if (dificuldade === 'Fácil') {
                $(this).addClass('btn-success');
            } else if (dificuldade === 'Médio') {
                $(this).addClass('btn-warning');
            } else if (dificuldade === 'Difícil') {
                $(this).addClass('btn-danger');
            }

            // Reseta os dados caso seja reiniciado o quiz de outra forma além do botão 'reiniciar'
            indicePerguntaAtual = 0;
            pontuacao = 0;
            carregarQuiz();
        });
    });
};

let dadosQuiz;
let indicePerguntaAtual = 0;
let pontuacao = 0;
let dificuldade = "Fácil";

function carregarDadosQuiz() {
    $.ajax({
        url: "/quiz",
        type: "POST",
        dataType: "json",
        success: function (data) {
            dadosQuiz = data;
        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    });
}

function carregarQuiz() {
    const perguntaAtualQuiz = dadosQuiz[dificuldade][indicePerguntaAtual];

    $("#pergunta").text(perguntaAtualQuiz.Pergunta);
    $("#opcoes").empty();

    perguntaAtualQuiz.Opcoes.forEach((opcao, indice) => {
        const li = $("<li>").text(opcao).addClass("opcao");
        li.click(() => selecionarResposta(indice));
        $("#opcoes").append(li);
    });

    // Atualizar o indicador de pergunta respondida
    $("#resultado-parcial h3").html(`${pontuacao}/${indicePerguntaAtual}`);
}

function selecionarResposta(indiceSelecionado) {
    // Bloater: Decomposição de if's e Extract Method
    const perguntaAtualQuiz = dadosQuiz[dificuldade][indicePerguntaAtual];
    indicePerguntaAtual++;

    // Desabilitar as opções de resposta, exceto a selecionada
    handleOptions(indiceSelecionado);

    // Dispensable: if decomposto
    var correctIdx = indiceSelecionado === perguntaAtualQuiz.Correta;
    pontuacao += correctIdx;
    mostrarResultadoParcial(correctIdx);

    if (indicePerguntaAtual < dadosQuiz[dificuldade].length) {
        setTimeout(() => {
            carregarQuiz();
        }, 1000);
    } else {
        mostrarResultadoFinal();
    }
}

function handleOptions(indiceSelecionado){
    $(".opcao").each(function (indice) {
        if (indice !== indiceSelecionado) {
            var newClass = "opcao-desativada"
        }
        else {
            var newClass = "opcao-selecionada"
        }
        $(this).addClass(newClass);
    });
}

function mostrarResultadoParcial(usuarioAcertou) {
    const resultadoParcial = $("#resultado-parcial");

    if (resultadoParcial.length) {
        // O elemento já existe, atualize seu conteúdo
        $("#water-container").append(`
                ${getWaterDropsHTML(usuarioAcertou)}
            </div>
        `);
    } else {
        // O elemento ainda não existe, adicione-o
        $("#quiz-container").append(`
            <div id="resultado-parcial">
                <h2>Seus acertos até agora :)</h2>
                <h3 style="font-size: 1.5rem;">Pergunta ${indicePerguntaAtual}/${dadosQuiz[dificuldade].length}</h3>
                <div class="water-container" id="water-container">
                    ${getWaterDropsHTML(usuarioAcertou)}
                </div>
            </div>
        `);
    }
}

function getWaterDropsHTML(usuarioAcertou) {
    // Bloater, usando extract method
    const totalDrops = dadosQuiz[dificuldade].length; // Número total de gotas d'água
    let dropsHTML = "";
    
    if (indicePerguntaAtual === 1) // Caso seja a primeira pergunta, gera todas as gotas para checagem do progresso do quiz
        dropsHTML = createWaterDrops(totalDrops, usuarioAcertou)
    else { 
        if (usuarioAcertou){ // Apenas alterar a gota correspondente à questão respondida
            let dropColor = "blue";
            $("#" + "drop" + (indicePerguntaAtual - 1)).css("color", dropColor);
        }
    }
    return dropsHTML;
}

function createWaterDrops(totalDrops, usuarioAcertou){
    let dropsHTML = "";
    for (let i = 0; i < totalDrops; i++) {
        let dropColor = i < indicePerguntaAtual && usuarioAcertou ? "blue" : "black";
        const dropId = "drop" + i;
        dropsHTML += `<i class="fas fa-tint" id=${dropId} style="color: ${dropColor};"></i>`;
    }
    return dropsHTML;
}

function mostrarResultadoFinal() {
    sound_piano();

    $("#quiz-container").html(`
        <h2> Você acertou ${pontuacao} de ${indicePerguntaAtual} perguntas.</h2>
        <button class='button' onclick="location.reload()">Reiniciar Quiz</button>
    `);

    let porcentagemAcertos = (pontuacao / indicePerguntaAtual) * 100;
    let label = "Parabens!"
    if (porcentagemAcertos <= 50) {
        label = "Estude mais!";
        }

    $("#resultado").html(`
        <h4>Resultado:</h4>
        <div id="gaugeFinal"></div>
    `);

    var gauge = new JustGage({
        id: "gaugeFinal",
        value: porcentagemAcertos,
        min: 0,
        max: 100,
        title: "Porcentagem de Acertos",
        label: label,
        gaugeWidthScale: 0.6,
        counter: true,
        relativeGaugeSize: true,
        levelColors: ["#ff0000", "#ffa500", "#6ab04c"], // Cores para diferentes níveis (opcional)
        levelColorsGradient: false, // Gradiente entre as cores (opcional)
        startAnimationType: "bounce",
        startAnimationTime: 2000,
        refreshAnimationType: "bounce",
        refreshAnimationTime: 1000
    });

}

let muted = true;

let audioBackground; // Variável global para armazenar a instância da música de fundo

function sound_backbround() {
    if (!muted) {
        if (!audioBackground) {
            audioBackground = new Audio("/static/sons/forest-river-with-whirls.mp3");
            audioBackground.loop = true;
        }
        audioBackground.play();
    }
}

function stop_sound_background() {
    if (audioBackground) {
        audioBackground.pause();
    }
}

function sound_bubble(){
    if(!muted){
        const aud = new Audio('/static/sons/mixkit-liquid-bubble-3000.wav')
        aud.play()
    }
}

function sound_piano(){
    if(!muted){
        const aud = new Audio('/static/sons/mixkit-quick-win-video-game-notification-269.wav')
        aud.play()
    }
}

function mute_element(element){
    element.muted = !element.muted;
}

function mute_all(){
    document.querySelectorAll("audio").forEach( element => mute_element(element));
    muted = !muted;
    if (muted) {
        stop_sound_background();
    } else {
        sound_backbround();
    }
}

function setVolume(value) {
    var audio = document.getElementById("bgsong");
    audioBackground.volume = value / 100;
    audio.volume = value / 100;
  }