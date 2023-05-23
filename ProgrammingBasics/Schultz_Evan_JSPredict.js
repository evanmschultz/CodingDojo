// question 1
function myBirthYearFunc(){
    console.log("I was born in" + 1980);
}
myBirthYearFunc(); // console log states "I was born in1980" without the quotation marks and missing a space between 'in' and 1980

// question 2
function myBirthYearFunc(birthYearInput){
    console.log("I was born in" + birthYearInput);
}
myBirthYearFunc(1980); // if 1980 was the value for birthYearInput than everything would be exactly the same as the previous function output

// question 3
function add(num1, num2){
    console.log("Summing Numbers!"); // simply prints "Summing Numbers!" without the quotation marks
    console.log("num1 is: " + num1); // prints "num1 is: 10" note the space between the colon and the integer
    console.log("num2 is: " + num2); // prints "num2 is: 20" note the space between the colon and the integer
    var sum = num1 + num2; // declares new variable 'sum' and performs addition of the given numbers
    console.log(sum); // simply outputs '30', the value of 'sum', without quotation marks 
}
add(10, 20);
