window.onload = function () {
    $(document).ready(function() {
        loadQuizData();
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
            
            // loadQuiz();

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


let quizData;
let currentQuestion = 0;
let score = 0;
let difficulty = "Fácil";

function loadQuizData() {
    $.ajax({
        url: "/quiz",
        type: "POST",
        dataType: "json",
        success: function (data) {
            quizData = data;
        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    });
}

function loadQuiz() {
    document.getElementById('submit').innerText = "Refazer "
    console.log(currentQuestion);
    console.log(currentQuizData);

    const currentQuizData = quizData[difficulty][currentQuestion];


    $("#question").text(currentQuizData.question);
    $("#options").empty();

    currentQuizData.options.forEach((option, index) => {
        const li = $("<li>").text(option);
        li.click(() => selectAnswer(index));
        $("#options").append(li);
    });
}

function selectAnswer(selectedIndex) {
    const currentQuizData = quizData[difficulty][currentQuestion];

    if (selectedIndex === currentQuizData.correctAnswer) {
        score++;
    }

    currentQuestion++;

    if (currentQuestion < quizData[difficulty].length) {
        loadQuiz();
    } else {
        showResults();
    }
}

function showResults() {
    $("#quiz-container").html(`
        <h2>You scored ${score}/${currentQuestion} correct answers.</h2>
        <button onclick="location.reload()">Restart Quiz</button>
    `);
}

function changeDifficulty() {
    const difficultySelect = $("#difficulty");
    difficulty = difficultySelect.val();
    currentQuestion = 0;
    score = 0;
    loadQuiz();
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