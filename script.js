let indiceAtual = 0;

function registrarClique(indice) {

    let cliques = JSON.parse(localStorage.getItem("cliques")) || {};

    cliques[indice] = (cliques[indice] || 0) + 1;

    localStorage.setItem("cliques", JSON.stringify(cliques));

    console.log("Enviando evento:", ofertas[indice].nome);

if (typeof gtag === "function") {
    gtag("event", "clique_oferta", {
        oferta: ofertas[indice].nome,
        loja: ofertas[indice].nome
    });
}
}
   
function mostrarOferta(indice) {

    const oferta = ofertas[indice];

    document.getElementById("produto-imagem").src = oferta.imagem;

    document.getElementById("produto-nome").textContent = oferta.nome;

    document.getElementById("produto-antigo").textContent = oferta.precoAntigo;

    document.getElementById("produto-preco").textContent = oferta.preco;

    const botao = document.getElementById("produto-link");

    botao.href = "#";

    botao.onclick = function (e) {

        e.preventDefault();

        registrarClique(indice);

        if (typeof gtag === "function") {

            gtag("event", "clique_oferta", {
                oferta: ofertas[indice].nome,
                loja: ofertas[indice].nome,

                event_callback: function () {
                    window.open(oferta.link, "_blank");
                }

            });

        } else {

            window.open(oferta.link, "_blank");

        }

    };

}

mostrarOferta(indiceAtual);

setInterval(() => {

    indiceAtual++;

    if (indiceAtual >= ofertas.length) {
        indiceAtual = 0;
    }

    mostrarOferta(indiceAtual);

}, 5000);