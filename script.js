function mostrarOferta(indice) {

    const oferta = ofertas[indice];

    document.getElementById("produto-imagem").src = oferta.imagem;

    document.getElementById("produto-nome").textContent = oferta.nome;

    document.getElementById("produto-antigo").textContent = oferta.precoAntigo;

    document.getElementById("produto-preco").textContent = oferta.preco;

    document.getElementById("produto-link").href = oferta.link;

}

// Mostra a primeira oferta
mostrarOferta(0);
let indiceAtual = 0;

setInterval(() => {

    indiceAtual++;

    if (indiceAtual >= ofertas.length) {
        indiceAtual = 0;
    }

    mostrarOferta(indiceAtual);

}, 5000);