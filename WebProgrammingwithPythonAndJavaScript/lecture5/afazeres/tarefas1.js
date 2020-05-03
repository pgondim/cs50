document.addEventListener('DOMContentLoaded', ()=>{

    document.querySelector('#submit').disable = true;

    document.querySelector('#tarefa').onkeyup = ()=>{
        document.querySelector('#submit').disabled = false;
    };

    document.querySelector('#nova-tarefa').onsubmit = ()=>{

        const li = document.createElement('li');

        li.innerHTML = document.querySelector('#tarefa').value;

        document.querySelector('#tarefas').append(li);

        document.querySelector('#tarefa').value = '';

        document.querySelector('#submit').disabled = true;
        
        // o comportamento padrão de submissão de formulário é tentar enviar esse formulário pra outro site, como queremos ficar apenas nessa pagina, temos que dar um retorno de false a fim de parar a submissão do formulário 
        return false
    };
});