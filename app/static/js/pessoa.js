document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("pessoaForm");
    const mensagem = document.getElementById("mensagem");

    // 🔹 Carregar setores
    async function carregarSetores() {
        try {
            const response = await fetch("/setor");
            const setores = await response.json();

            const select = document.getElementById("setor_id");
            select.innerHTML = '<option value="">Selecione um setor</option>';

            setores.forEach(setor => {
                const option = document.createElement("option");
                option.value = setor.id;
                option.textContent = setor.nome;
                select.appendChild(option);
            });

        } catch (error) {
            mensagem.style.color = "red";
            mensagem.textContent = "Erro ao carregar setores.";
            console.error(error);
        }
    }

    carregarSetores();

    // 🔹 Submit
    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const nome = document.getElementById("nome").value.trim();
        const documento = document.getElementById("documento").value.trim();
        const tipo = document.getElementById("tipo").value;
        const setor_id = document.getElementById("setor_id").value;

        try {
            const response = await fetch("/pessoa", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    nome,
                    documento,
                    tipo,
                    setor_id
                })
            });

            const data = await response.json();

            if (response.ok) {
                mensagem.style.color = "green";
                mensagem.textContent = "Pessoa cadastrada com sucesso!";
                form.reset();
            } else {
                mensagem.style.color = "red";
                mensagem.textContent = data.erro || "Erro ao cadastrar.";
            }

        } catch (error) {
            mensagem.style.color = "red";
            mensagem.textContent = "Erro na requisição.";
            console.error(error);
        }
    });

});
