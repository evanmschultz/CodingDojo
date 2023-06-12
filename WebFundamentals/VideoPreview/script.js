console.log("page loaded...")

function playVideo(element) {
    // console.log("play")
    element.muted = true
    element.play()
}

function stopVideo(element) {
    // console.log("stop")
    element.pause()
}
