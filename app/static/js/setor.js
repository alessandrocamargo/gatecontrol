document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("setorForm");
    const mensagem = document.getElementById("mensagem");

    if (form) {
        form.addEventListener("submit", async function (event) {
            event.preventDefault();

            const nome = document.getElementById("nome").value;

            const response = await fetch("/setor", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ nome: nome })
            });

            const data = await response.json();

            if (response.status === 201) {
                mensagem.textContent = "Setor cadastrado com sucesso!";
                mensagem.className = "success";
                form.reset();
            } else {
                mensagem.textContent = data.erro || "Erro ao cadastrar";
                mensagem.className = "error";
            }
        });
    }

});
