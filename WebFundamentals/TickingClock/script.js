const secondsHand = document.getElementById("seconds-hand")
const minuteHand = document.getElementById("minute-hand")
const hourHand = document.getElementById("hour-hand")

function updateHandAngles() {
    const now = new Date()

    const seconds = now.getSeconds()
    const secondsHandAngle = (seconds % 60) * 6 + 90 // 360 / 60 = 6, 1 second = 6° // add 90° to compensate for initial transform
    secondsHand.style.transform = `rotate(${secondsHandAngle}deg)`

    const minute = now.getMinutes()
    const minuteHandAngle = (minute % 60) * 6 + 90
    minuteHand.style.transform = `rotate(${minuteHandAngle}deg)`

    const hours = now.getHours()
    const hourHandAngle = (hours % 12) * 30 + 90 // 360 / 12 = 30, 1 hour = 30°
    hourHand.style.transform = `rotate(${hourHandAngle}deg)`
}

setInterval(() => {
    updateHandAngles()
}, 1000)
