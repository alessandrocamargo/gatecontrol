function formatDocumento(doc) {

    if (!doc) return ""

    doc = String(doc).replace(/\D/g, "")

    if (doc.length === 11) {
        return doc.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/,
            "$1.$2.$3-$4")
    }

    if (doc.length === 14) {
        return doc.replace(
            /^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/,
            "$1.$2.$3/$4-$5"
        )
    }

    return doc
}

document.addEventListener("DOMContentLoaded", () => {

    const docs = document.querySelectorAll(".doc")

    docs.forEach(el => {

        const raw = el.textContent.trim()

        el.textContent = formatDocumento(raw)

    })

})