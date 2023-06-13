function changeName(nameId) {
    console.log(nameId)
    usersNameElement = document.querySelector(nameId)
    usersName = usersNameElement.innerText
    console.log(usersName)
    if (usersName == "Jane Doe") {
        usersNameElement.innerText = "Philip J. Fry"
    } else {
        usersNameElement.innerText = "Jane Doe"
    }
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
