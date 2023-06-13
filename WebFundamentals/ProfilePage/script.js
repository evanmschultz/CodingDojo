function changeName(nameId) {
    console.log(nameId)
    usersName = document.querySelector(nameId)
    console.log(usersName)
    usersName.innerText = "Philip J. Fry"
}

function removeConnectionRequest(requestId) {
    // console.log(requestId)
    element = document.querySelector(requestId)
    // console.log(element + " " + requestId)
    element.remove()
}

function decreaseNotificationCount(counterId) {
    counterElement = document.querySelector(counterId)
    // console.log(counterElement)
    count = counterElement.innerText
    // console.log(count)
    count--
    counterElement.innerText = count
}

function increaseConnectionsCount(counterId) {
    // console.log(`increase called on ${counterId}`)
    counterElement = document.querySelector(counterId)
    count = counterElement.innerText
    count++
    counterElement.innerText = count
}
