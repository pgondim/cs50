document.addEventListener('DOMContentLoaded',function(){

    document.querySelector('#azul').onclick = function(){
        document.querySelector('#titulo').style.color = 'blue';
    };

    document.querySelector('#verde').onclick = function(){
        document.querySelector('#titulo').style.color = 'green';
    };

    document.querySelector('#vermelho').onclick = function(){
        document.querySelector('#titulo').style.color = 'red';
    };
});