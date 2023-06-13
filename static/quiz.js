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
                    // Limpar as perguntas e respostas anteriores
                    $('#perguntas').empty();
                    $('#respostas').empty();

                    // Preencher as perguntas e respostas
                    var letras = ['a', 'b', 'c'];
                    var perguntasTable = $('<table>').addClass('table');
                    var respostasTable = $('<table>').addClass('table');
                    $.each(response, function(key, value) {
                        var numero = key;
                        var pergunta = value['Pergunta'];
                        var opcoes = value['Opcoes']

                        // Div Pergunta
                        var row = $('<tr>');
                        var cell = $('<td>').text(pergunta);
                        var perguntasCell = $('<td>').text("Pergunta " + numero);
                        row.append(perguntasCell);
                        row.append(cell);
                        perguntasTable.append(row);
                        
                        var row = $('<tr>');
                        var respostasCell = $('<td>').text("Resposta " + numero);
                        row.append(respostasCell);
                        $.each(opcoes, function(letra, resposta) {
                            var radioId = 'resposta-' + numero + '-' + letra;
                            var radio = $('<input>').attr('type', 'radio').attr('name', key.split(' ')[1]).val(letra).attr('id', radioId).addClass('resposta-radio');
                            var label = $('<label>').text(resposta).attr('for', radioId);
                            var cell = $('<td>').append(radio).append(label);
                            row.append(cell);
                            respostasTable.append(row);
                        });
                    });

                    $('#perguntas').append(perguntasTable);
                    $('#respostas').append(respostasTable);

                }
            });
        });
        $('#verificar').click(function () {
            dificuldade = false
            if (document.querySelector(".btn-success")) {
                dificuldade = 'Fácil';
            } else if (document.querySelector(".btn-warning")) {
                dificuldade = 'Médio';
            } else if (document.querySelector(".btn-danger")) {
                dificuldade = 'Difícil';
            }
            var respostas = {};
            $('input[class=resposta-radio]:checked').each(function() {
                respostas[$(this).attr('id').split('-')[1]] = $(this).val();
            });
            send = {};
            send['Dificuldade'] = dificuldade;
            send['Resposta'] = JSON.stringify(respostas);

            $.ajax({
                url: '/quiz/responder',
                type: 'POST',
                data: send,
                success: function (response) {
                    // Exibir o resultado das respostas
                    acertos = response['resultado']['acertos'];
                    total = response['resultado']['total'];
                    var porcentagemAcertos = (acertos / total) * 100;
                    var label = "Parabens!";
                    if (porcentagemAcertos < 50){
                        label = "Estude mais!";
                    } 

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
            });
        });
    });
}