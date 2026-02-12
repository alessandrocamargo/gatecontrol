document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("veiculoForm");
    const mensagem = document.getElementById("mensagem");

    // 🔹 Carregar setores no select
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
            mensagem.textContent = "Erro ao carregar setores.";
            console.error(error);
        }
    }

    carregarSetores();

    // 🔹 Submit do formulário
    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const placa = document.getElementById("placa").value.trim();
        const modelo = document.getElementById("modelo").value.trim();
        const tipo = document.getElementById("tipo").value;
        const setor_id = document.getElementById("setor_id").value;

        try {
            const response = await fetch("/veiculos", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    placa,
                    modelo,
                    tipo,
                    setor_id
                })
            });

            const data = await response.json();

            if (response.ok) {
                mensagem.style.color = "green";
                mensagem.textContent = "Veículo cadastrado com sucesso!";
                form.reset();
            } else {
                mensagem.style.color = "red";
                mensagem.textContent = data.message || "Erro ao cadastrar.";
            }

        } catch (error) {
            mensagem.style.color = "red";
            mensagem.textContent = "Erro na requisição.";
            console.error(error);
        }
    });

});
