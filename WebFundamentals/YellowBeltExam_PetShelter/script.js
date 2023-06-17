function removeElement(id) {
    let element = document.getElementById(id)

    element.remove
}

function alertType(name) {
    let value = document.getElementsByName(name)[0].value

    alert(`You are looking for a: ${value}`)
}

function incrementLikes(id) {
    /* Decided to do it without conditionals becuase I demonstrated that on the likes 
    assignment as well as this method and this one is faster */
    let element = document.getElementById(id)
    let text = element.innerText
    let count = parseInt(text)

    count++
    element.innerText = `${count} petting(s)`
}
