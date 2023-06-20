window.onload = function () {
    $(document).ready(function() {
        carregarDadosQuiz();
        // $("submit").click(loadQuiz());

        
        // Evento de clique nos botões de dificuldade
        $('.btn-dificuldade').click(function() {
            var dificuldade = $(this).data('dificuldade');

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
            
            
            carregarQuiz();

            });
        });
        // $('#verificar').click(function () {
        //     send = {};
        //     send['Dificuldade'] = dificuldade;
        //     send['Resposta'] = JSON.stringify(respostas);

        //     $.ajax({
        //         url: '/quiz/responder',
        //         type: 'POST',
        //         data: send,
        //         success: function (response) {
        //             // Exibir o resultado das respostas
        //             acertos = response['resultado']['acertos'];
        //             total = response['resultado']['total'];
        //             var porcentagemAcertos = (acertos / total) * 100;
        //             var label = "Parabens!";
        //             if (porcentagemAcertos < 50){
        //                 label = "Estude mais!";
        //             } 

        //             var gauge = new JustGage({
        //                 id: "gauge",
        //                 value: porcentagemAcertos,
        //                 min: 0,
        //                 max: 100,
        //                 title: "Porcentagem de Acertos",
        //                 label: label,
        //                 gaugeWidthScale: 0.6,
        //                 counter: true,
        //                 relativeGaugeSize: true,
        //                 levelColors: ["#ff0000", "#ffa500", "#6ab04c"], // Cores para diferentes níveis (opcional)
        //                 levelColorsGradient: false, // Gradiente entre as cores (opcional)
        //                 startAnimationType: "bounce",
        //                 startAnimationTime: 2000,
        //                 refreshAnimationType: "bounce",
        //                 refreshAnimationTime: 1000
        //             });
        //         }
        //     });
        // });
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

    if (indiceSelecionado === perguntaAtualQuiz.respostaCorreta) {
        pontuacao++;
    }

    perguntaAtual++;

    if (perguntaAtual < dadosQuiz[dificuldade].length) {
        carregarQuiz();
    } else {
        mostrarResultado();
    }
}

function mostrarResultado() {
    $("#quiz-container").html(`
        <h2>Você acertou ${pontuacao} de ${perguntaAtual} perguntas.</h2>
        <button onclick="location.reload()">Reiniciar Quiz</button>
    `);
}

function alterarDificuldade() {
    const seletorDificuldade = $("#dificuldade");
    dificuldade = seletorDificuldade.val();
    perguntaAtual = 0;
    pontuacao = 0;
    carregarQuiz();
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
  };