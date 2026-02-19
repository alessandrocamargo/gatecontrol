document.addEventListener("DOMContentLoaded", () => {
  const modalTitle = document.getElementById("movModalTitle");
  const veiculoLabel = document.getElementById("movVeiculoLabel");
  const veiculoIdInput = document.getElementById("movVeiculoId");

  const kmLabel = document.getElementById("movKmLabel");
  const kmInput = document.getElementById("movKmInput");
  const hint = document.getElementById("movHint");

  const form = document.getElementById("movForm");
  const submitBtn = document.getElementById("movSubmitBtn");

  // Vamos alternar o NAME do input, porque seu backend espera:
  // - Saída: request.form.get("km_saida")
  // - Retorno: request.form.get("km_retorno")
  function setKmFieldName(name) {
    kmInput.name = name;
  }

  document.querySelectorAll(".js-mov-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const tipo = btn.dataset.tipo; // "saida" ou "retorno"
      const placa = btn.dataset.placa || "-";
      const veiculoId = btn.dataset.veiculoId || "";

      veiculoLabel.textContent = placa;
      veiculoIdInput.value = veiculoId;

      kmInput.value = "";

      if (tipo === "saida") {
        modalTitle.textContent = "Registrar saída";
        kmLabel.textContent = "KM de saída";
        hint.textContent = "Informe a KM no momento da saída.";
        submitBtn.textContent = "Registrar saída";
        submitBtn.classList.remove("btn-warning");
        submitBtn.classList.add("btn-primary");

        // action é fixo (endpoint de saída)
        form.action = btn.dataset.actionUrl;

        // backend espera km_saida e veiculo_id
        setKmFieldName("km_saida");
        veiculoIdInput.disabled = false;
      }

      if (tipo === "retorno") {
        modalTitle.textContent = "Registrar retorno";
        kmLabel.textContent = "KM de retorno";
        hint.textContent = "Informe a KM no momento do retorno.";
        submitBtn.textContent = "Registrar retorno";
        submitBtn.classList.remove("btn-primary");
        submitBtn.classList.add("btn-warning");

        const movId = btn.dataset.movId;
        const template = btn.dataset.actionTemplate; // .../retorno/0
        form.action = template.replace(/0$/, movId);

        // backend espera km_retorno
        setKmFieldName("km_retorno");

        // retorno não precisa enviar veiculo_id (vai pela URL), mas não atrapalha.
        // Se quiser, pode desabilitar:
        veiculoIdInput.disabled = true;
      }
    });
  });
});
