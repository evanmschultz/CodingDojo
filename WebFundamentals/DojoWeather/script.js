function removeAlert(alertId) {
    alert = document.getElementById(alertId)
    alert.remove()
}

function updateTempScale() {
    let temps = document.querySelectorAll("[data-type='temp'")
    let selectElement = document.getElementById("temp-scale")
    let selectedScale = selectElement.value

    for (i = 0; i < temps.length; i++) {
        let temp = parseInt(temps[i].innerText)

        if (selectedScale === "farenheit") {
            temp = Math.round((9 / 5) * temp + 32)
        } else {
            temp = Math.round((5 / 9) * (temp - 32))
        }

        elementToUpdate = document.getElementById(`temp-${i + 1}`)
        elementToUpdate.innerText = `${temp}°`
    }
}
