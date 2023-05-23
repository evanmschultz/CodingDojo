// variable indicating the minimum age for the rider to be used for comparison
var minAge = 10;
// variable indicating the minimum height for the rider to be used for comparison
var minHeight = 42;

// variable indicating the height of the rider
var kidHeight = 40;
// variable indicating the age of the rider
var kidAge = 11;

// conditional statement to determine if the rider meets the minimum height and age requirements
if (kidHeight >= minHeight && kidAge >= minAge) {
    // code performed if the rider meets the minimum height and age requirements
    console.log("Get on that ride, kiddo!");
}
else {
    // code performed if the rider does not meet the minimum height requirement
    console.log("Sorry kiddo. Maybe next year.");
}

// conditional statement to determine if the rider meets either the minimum height OR age requirements
if (kidHeight >= minHeight || kidAge >= minAge) {
    // code performed if the rider meets the minimum height and age requirements
    console.log("Get on that ride, kiddo!");
}
else {
    // code performed if the rider does not meet the minimum height requirement
    console.log("Sorry kiddo. Maybe next year.");
}