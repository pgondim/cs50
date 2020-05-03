document.addEventListener('DOMContentLoaded',function(){

    document.querySelectorAll('.mudar-cor').forEach(function(button){
        button.onclick = function(){
            document.querySelector('#titulo').style.color = button.dataset.color;
        }
    });
});