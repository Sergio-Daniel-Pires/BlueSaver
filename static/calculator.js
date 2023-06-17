function calculator(){
    // Obter os valores do formulário
    var qtd_pessoas = parseFloat(document.getElementById('qtd_pessoas').value);
    var gasto_mensal = parseFloat(document.getElementById('gasto_mensal').value);
    var estado = document.getElementById('estado').value;
    var taxas_estado = {"norte":1.92, "nordeste":2.13, "sudeste":3.17, "sul":3.80, "centro-oeste":4.17};

    if (isNaN(qtd_pessoas)|| isNaN(gasto_mensal)) {
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
        var resultado_gasto_pessoa = parseInt((gasto_mensal*1000)/(qtd_pessoas*30));
        var texto_gasto_agua = 'O consumo médio na sua residência é ' + resultado_gasto_pessoa +' Litros/pessoa/dia';
        //realiza o cálculo de valor médio da conta de água mensal
        var gasto_conta_agua = parseFloat(gasto_mensal * taxas_estado[estado]);
        var texto_conta_agua = 'O preço médio de sua conta de luz será de: R$' + gasto_conta_agua.toFixed(2);

        // Exibir o resultado
        document.getElementById('resultado').innerHTML = texto_gasto_agua + '<br>' + texto_conta_agua;
        
    }

}
    
    
