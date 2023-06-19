window.onload = function (){
    $(document).ready(function() {
        $('#btn-calcular').click(function() {
            var qtd_pessoas = parseFloat(document.getElementById('qtd_pessoas').value);
            var gasto_mensal = parseFloat(document.getElementById('gasto_mensal').value);
            var estado = document.getElementById('estado').value;

            if (isNaN(qtd_pessoas) || isNaN(gasto_mensal)) {
                alert('Por favor, preencha todos os campos obrigatórios.');
            }
            else if( !Number.isInteger(parseFloat(qtd_pessoas)) || !Number.isInteger(parseFloat(gasto_mensal))){
                alert('Por favor, preencha os campos de N° de pessoa e consumo mensal com valores inteiros.');
            }
            else if (estado === ""){
                alert('Por favor, selecione seu estado.');
            }
            else{
                // Realizar o cálculo do gasto de litros por pessoa por dia

                send = {};
                send['qtd_pessoas'] = qtd_pessoas;
                send['gasto_mensal'] = gasto_mensal;
                send['estado'] = estado;

                $.ajax({
                    url: "/calculadora/calcular",
                    type: 'POST',
                    data: send,
                    success: function(response){
                        var texto_gasto_agua = 'O consumo médio na sua residência é ' + response['gasto_pessoa'] + ' Litros/pessoa/dia';
                        //realiza o cálculo de valor médio da conta de água mensal
                        var texto_conta_agua = 'O preço médio de sua conta de luz será de: R$' + response['gasto_agua'].toFixed(2);
                
                        // Exibir o resultado
                        document.getElementById('resultado').innerHTML = texto_gasto_agua + '<br>' + texto_conta_agua;

                    }
                })
                
            }
        });
    });
}