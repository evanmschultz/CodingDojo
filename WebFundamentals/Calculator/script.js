let display = document.getElementById("display")
let operator = ""
let tempResult = 0
let resetDisplay = false
let calcCarry = false

function press(number) {
    if (resetDisplay) {
        display.innerText = 0
        resetDisplay = false
    }

    if (display.innerText === "0") {
        // check for strict equality, js treats '-' as 0 on nums > |1|

        display.innerText = number
    } else if (calcCarry) {
        // if there is a calculation being carried over, set display to number so it won't concatenate

        display.innerText = number
    } else {
        // concatenate display and number

        display.innerText += number
    }
}

function setOP(operatorInput) {
    // updates tempResult, clears display

    if (resetDisplay) {
        // if equals was pressed last: update tempResult with result, update operator,
        // reset display, update resetDisplay bool, exit function

        tempResult = display.innerText
        operator = operatorInput
        display.innerText = tempResult
        resetDisplay = false
        return
    }

    if (operator) {
        // if there is an operator (a calculation has carried over), calculate and store result

        tempResult = calculator()
        calcCarry = true // set calcCarry to show result on next operator input
        display.innerText = tempResult
        operator = operatorInput
        return
    } else if (display.innerText == 0 && operatorInput == "-") {
        // if '-' is first input, make number negative

        display.innerText = "-"
        return
    } else {
        // if this is the first operatorInput, set tempResult to be current display

        tempResult = display.innerText
    }

    // update operator and reset display
    operator = operatorInput
    display.innerText = 0
}

function clr() {
    // reset all global calculation variables

    console.log("clear pressed")
    display.innerText = 0
    operator = ""
    tempResult = 0
}

function equals() {
    // updates display, clears tempResult
    // if equals is pushed, variable (resetDisplay) will clear display once any button is pushed

    if (resetDisplay) {
        display.innerText = 0
        resetDisplay = false
    }
    if (!operator) {
        return
    } else {
        display.innerText = calculator()
        resetDisplay = true
    }
}

function calculator() {
    let result = 0

    if (operator == "+") {
        result = parseFloat(tempResult) + parseFloat(display.innerText)
    } else if (operator == "-") {
        result = parseFloat(tempResult) - parseFloat(display.innerText)
    } else if (operator == "*") {
        result = parseFloat(tempResult) * parseFloat(display.innerText)
    } else {
        result = parseFloat(tempResult) / parseFloat(display.innerText)
    }

    operator = ""
    return result
}
