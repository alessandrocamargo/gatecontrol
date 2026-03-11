document.addEventListener("DOMContentLoaded", () => {

  const documentoInput = document.getElementById("documento")
  const nomeInput = document.getElementById("nome")
  const tipoSelect = document.getElementById("tipo")
  const setorInput = document.getElementById("setor")

  if (!documentoInput) return

  documentoInput.addEventListener("blur", async () => {

    const documento = documentoInput.value.trim()
    if (!documento) return

    try {
      const resp = await fetch(`/pessoas/buscar/${documento}`)
      const data = await resp.json()

      if (data.existe) {

        // preenche
        nomeInput.value = data.nome || ""
        tipoSelect.value = data.tipo || "visitante"
        setorInput.value = data.setor_id || ""

        // trava campos que vieram do banco
        nomeInput.readOnly = true
        tipoSelect.disabled = true
        setorInput.readOnly = true

      } else {

        // limpa e libera para cadastro
        nomeInput.value = ""
        tipoSelect.value = "visitante"
        setorInput.value = ""

        nomeInput.readOnly = false
        tipoSelect.disabled = false
        setorInput.readOnly = false
      }

    } catch (err) {
      console.error("Erro ao buscar pessoa:", err)
    }

  })

})