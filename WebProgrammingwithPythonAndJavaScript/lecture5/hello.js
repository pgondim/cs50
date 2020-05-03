document.addEventListener('DOMContentLoaded',function(){
    document.querySelector('#form').onsubmit = function(){
        const name = document.querySelector('#nome').value;
        alert(`Olá ${name}`);
    }
})