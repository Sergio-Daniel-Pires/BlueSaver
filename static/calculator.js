
function calculator(){
    // Obter os valores do formulário
    var qtd_pessoas = parseFloat(document.getElementById('qtd_pessoas').value);
    var gasto_mensal = parseFloat(document.getElementById('gasto_mensal').value);
    var estado = document.getElementById('estado').value;

    if (isNaN(qtd_pessoas)|| isNaN(gasto_mensal)) {
        alert('Por favor, preencha todos os campos obrigatórios.');
    }
    else if( !Number.isInteger(parseFloat(qtd_pessoas)) || !Number.isInteger(parseFloat(gasto_mensal))){
        alert('Por favor, preencha os campos números com valores inteiros.');
    }
    else if (estado === ""){
        alert('Por favor, selecione seu estado.');
    }
    else{
        // Realizar o cálculo
        var resultado = parseInt((gasto_mensal*1000)/(qtd_pessoas*30));
        // Exibir o resultado
        document.getElementById('resultado').textContent = 'O consumo médio na sua residência é ' + resultado +' Litros/pessoa/dia';
    }
    
}
    
