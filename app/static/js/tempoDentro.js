function calcularTempo(dataEntrada) {
    const entrada  = new Date(dataEntrada)
    const agora = new Date()

    const diff = Math.floor((agora - entrada) / 1000) // segundos

    const minutos = Math.floor(diff / 60)

    if(minutos > 60) {
        return `${minutos} min`
    }

    const horas = Math.floor(minutos / 60)
    const minutosRest = minutos % 60

    return `${horas}h ${minutos}m`
}

function atualizarTempos(){
    const elementos = document.querySelectorAll(".tempo-dentro")
    elementos.forEach(el => {
        const entrada = el.dataset.entrada

        if(!entrada) return

        const tempo = calcularTempo(entrada)

        el.textContent = "⏱" + calcularTempo(entrada)

        el.classList.remove("text-sucess", "text-warning", "text-danger")
        
        if (tempo.minutos < 60 ) {
            el.classList.add("text-sucess")
        }
        else if(tempo.minutos < 120 ){
            el.classList.add("text-earning")
        }
        else {
            el.classList.add("text-danger")
        }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    atualizarTempos()
    setInterval(atualizarTempos, 60000)
})