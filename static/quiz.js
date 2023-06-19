window.onload = function () {
    $(document).ready(function() {
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

            $.ajax({
                url: '/quiz',
                type: 'POST',
                data: { Dificuldade: dificuldade },
                success: function(response) {
                    loadQuiz();
                }
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
    });
}

const questionElement = document.getElementById("question");
const optionsElement = document.getElementById("options");
const submitButton = document.getElementById("submit");

let currentQuestion = 0;
let score = 0;
let difficulty = "easy"; // Set the default difficulty level

function loadQuiz() {
    fetch("quizData.json")
        .then(response => response.json())
        .then(data => {
            const currentQuizData = data[difficulty][currentQuestion];

            questionElement.innerText = currentQuizData.question;
            optionsElement.innerHTML = "";

            currentQuizData.options.forEach((option, index) => {
                const li = document.createElement("li");
                li.innerText = option;
                li.addEventListener("click", () => selectAnswer(index));
                optionsElement.appendChild(li);
            });
        });
}

function selectAnswer(selectedIndex) {
    fetch("quizData.json")
        .then(response => response.json())
        .then(data => {
            const currentQuizData = data[difficulty][currentQuestion];

            if (selectedIndex === currentQuizData.correctAnswer) {
                score++;
            }

            currentQuestion++;

            if (currentQuestion < data[difficulty].length) {
                loadQuiz();
            } else {
                showResults();
            }
        });
}

function showResults() {
    const quizContainer = document.getElementById("quiz-container");
    quizContainer.innerHTML = `
    <h2>You scored ${score}/${currentQuestion} correct answers.</h2>
    <button onclick="location.reload()">Restart Quiz</button>
  `;
}

submitButton.addEventListener("click", loadQuiz);

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