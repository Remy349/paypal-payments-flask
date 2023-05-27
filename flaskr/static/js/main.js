document.addEventListener('DOMContentLoaded', () => {
  const btnPaypal = document.getElementById('btnPaypal')

  if (btnPaypal) {
    btnPaypal.addEventListener('click', async () => {
      const res = await fetch('/create-order', {
        method: 'POST',
      })

      const data = await res.json()

      window.location.href = data.links[1].href
    })
  }
})
