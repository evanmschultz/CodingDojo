let likes = 0
let likesDisplay = document.querySelector("#likes-display")
// console.log(likesDisplay)

function increaseLikes() {
    likes++
    // console.log(likes)
    likesDisplay.innerText = likes + " like(s)"
}
