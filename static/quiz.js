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
            perguntaAtual = 0;
            pontuacao = 0;
            carregarQuiz();
        });
    });
};

let dadosQuiz;
let perguntaAtual = 0;
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
    const perguntaAtualQuiz = dadosQuiz[dificuldade][perguntaAtual];

    $("#pergunta").text(perguntaAtualQuiz.Pergunta);
    $("#opcoes").empty();

    perguntaAtualQuiz.Opcoes.forEach((opcao, indice) => {
        const li = $("<li>").text(opcao);
        li.click(() => selecionarResposta(indice));
        $("#opcoes").append(li);
    });
}

function selecionarResposta(indiceSelecionado) {
    const perguntaAtualQuiz = dadosQuiz[dificuldade][perguntaAtual];

    if (indiceSelecionado === perguntaAtualQuiz.Correta) {
        pontuacao++;
    }

    mostrarResultadoParcial(); // Mostra o resultado parcial a cada pergunta respondida

    perguntaAtual++;

    if (perguntaAtual < dadosQuiz[dificuldade].length) {
        carregarQuiz();
    } else {
        mostrarResultadoFinal();
    }
}

function mostrarResultadoParcial() {
    const porcentagemAcertos = (pontuacao / perguntaAtual) * 100;
    let label = "Parabéns!";
    if (porcentagemAcertos <= 50) {
        label = "Estude mais!";
    }

    $("#resultado").html(`
        <h4>Resultado Parcial:</h4>
        <div id="gaugeParcial"></div>
    `);

    const gauge = new JustGage({
        id: "gaugeParcial",
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

function mostrarResultadoFinal() {
    $("#quiz-container").html(`
        <h2> Você acertou ${pontuacao} de ${perguntaAtual} perguntas.</h2>
        <button class='button' onclick="location.reload()">Reiniciar Quiz</button>
    `);

    let porcentagemAcertos = (pontuacao / perguntaAtual) * 100;
    let label = "Parabens!"
    if (porcentagemAcertos <= 50) {
        label = "Estude mais!";
        }
    sound_piano();
    document.getElementById("gauge").innerHTML = '';
    var gauge = new JustGage({
        id: "gauge",
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

var muted = false;

function mute_all(){
    document.querySelectorAll("audio").forEach( element => mute_element(element));
    muted = !muted;
}

function setVolume(value) {
    var audio = document.getElementById("bgsong");
    audio.volume = value / 100;
  }