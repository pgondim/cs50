document.addEventListener('DOMContentLoaded',()=>{

    document.querySelector('#mudar-cor').onchange = function(){
        document.querySelector('#titulo').style.color = this.value;
    };
});