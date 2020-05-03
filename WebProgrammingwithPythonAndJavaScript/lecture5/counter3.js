document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = contador
})

let counter = 0
function contador(){
    counter++
    document.querySelector('#counter').innerHTML = counter

    if (counter % 10 === 0){
        alert(`Contador está em ${counter}`)
    }
}