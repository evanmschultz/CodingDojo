function changeLogin(element) {
    console.log("changeLogin called")
    if (element.innerText == "Logout") {
        element.innerText = "Login"
    } else {
        element.innerText = "Logout"
    }
}

function removeButton(element) {
    console.log("removeButton called")
    element.remove()
}
