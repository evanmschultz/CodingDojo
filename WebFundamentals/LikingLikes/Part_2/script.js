function increaseLikesCount(likesDisplayId) {
    let likesDisplay = document.getElementById(likesDisplayId)
    console.log(likesDisplay)

    /* parseInt(str, radix) no radix, so it assumes it is base 10, gets the integer out and can use that 
    to store count without anther variable needed */
    let count = parseInt(likesDisplay.innerText)
    count++
    likesDisplay.innerText = count + " like(s)"
}

/* ///////////////////
my original idea until I learned about parseInt()
   /////////////////// */

/*
let displayLikes1 = 0;
let displayLikes2 = 0;
let displayLikes3 = 0;

function increaseLikesCount(elementID) {
    let likesDisplay = document.getElementById(elementID);
    let count;

    if (elementID === "display-likes-1") {
        displayLikes1++;
        count = displayLikes1;
    } else if (elementID === "display-likes-2") {
        displayLikes2++;
        count = displayLikes2;
    } else {
        displayLikes3++;
        count = displayLikes3;
    }

    likesDisplay.innerText = count + " like(s)";
}
*/
