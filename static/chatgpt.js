// Função para mandar mensagem e receber resposta
function sendMessage() {
    // Pegar input do usuário
    const userInput = $('#user-input').val();
    // Limpar campo de input
    $('#user-input').val('');
    
    // Mostrar pergunta digitada
    $('#chat-log').append(`<p><strong>Você:</strong> ${userInput}</p>`);
    
    // Fazer requisição para a API do chatGPT através do backend
    $.ajax({
        url: '/chatgpt/responder',
        type: 'POST',
        headers: {
        'Content-Type': 'application/json'
    //    'Authorization': 'Bearer YOUR_API_KEY'
        },
        data: JSON.stringify({ input: userInput }),
        success: function(responseData) {
            const generatedResponse = responseData["Resposta"];
            // Mostrar resposta gerada
            $('#chat-log').append(`<p><strong>ChatGPT:</strong> ${generatedResponse}</p>`);
        }
    });
    }