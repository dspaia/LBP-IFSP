document.addEventListener("DOMContentLoaded",()=>{
    const botoes = document.querySelectorAll("seletor-personagem")
    const containerBiografia = document.getElementById("container-biografia")
    botoes.forEach(botao=>{
        const personagemId = botao.dataset.id
        containerBiografia.innerHTML = "<h2>Carregando...</h2><p></p>"

        fetch(`/biografia/${personagemId}`)
        .then(response=>{
            if (!response.ok){
                throw new Error("A resposta de rede não foi bem sucedida")
            }
            return response.json()
        })
        .then(data=>{
            containerBiografia.innerHTML = `<h2>${data.nome}<h2> <p>${data.nome}</p>`
        })
        .catch(error=>{
            console.error("Erro ao buscar a biografia:", error)

            containerBiografia.innerHTML = "<h2> Ocorreu um erro.</h2> <p>Não foi possivel carregar os dados</p>"
        })
    })
})