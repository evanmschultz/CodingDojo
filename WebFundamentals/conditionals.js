/* 
MVP

As a diligent student, I want to reward myself if I finish my homework, and based on the time of day:

I want a latte if it's before 10 am
I want a hot chocolate it's between 10 am and 4 pm
I want ice cream between 4 pm - 10 pm.
If it's after 10 pm, I don't want anything other than sleep!
*/

function reward(finished, time) {
  if (finished && time < 10) {
    console.log("Have a latte!");
  } else if (finished && time < 16) {
    console.log("Grab a hot chocolate!");
  } else if (finished && time < 22) {
    console.log("Get some ice cream!");
  } else if (finished && time >= 22) {
    console.log("Great work, go to sleep!");
  } else {
    console.log("Get back to work!");
  }
}

// console.log("MVP");
// reward(true, 9);
// reward(false, 10);
// reward(true, 11);
// reward(true, 21);
// reward(true, 22);

/*
Formatted the way I wanted to originally, but I felt I should show competency in combing conditionals

FEATURE 1

Building off the MVP, if I'm up for ice cream, I want strawberry - but only if it's Wednesday. Otherwise, I want vanilla.
*/

function yourReward(finished, time, day) {
  if (finished) {
    if (time < 10) {
      console.log("Have a latte!");
    } else if (time < 16) {
      console.log("Grab a hot chocolate!");
    } else if (time < 22) {
      if (day == "Wednesday") {
        console.log("Get yourself some strawberry ice cream!");
      } else {
        console.log("Get yourself some vanilla ice cream!");
      }
    } else if (time >= 22) {
      console.log("Great work, go to sleep!");
    }
  } else {
    console.log("Get back to work!");
  }
}

// console.log("FEATURE 1");
// yourReward(true, 9);
// yourReward(false, 10);
// yourReward(true, 11);
// yourReward(true, 21, "Wednesday");
// yourReward(true, 21, "Tuesday");
// yourReward(true, 22);

/*
FEATURE 2

Building off Feature 1, I want to adjust the current conditions and add a new option so that if the time is between 3 pm - 6 pm, 
I want to have it pick either ice cream or hot chocolate depending on if the time is even or odd.
*/

function yourReward(finished, time, day) {
  if (finished) {
    if (time < 10) {
      console.log("Have a latte!");
    } else if (time < 15) {
      console.log("Grab a hot chocolate!");
    } else if (15 <= time < 18) {
      if (time % 2 != 0) {
        console.log("Pick a flavor of ice cream!");
      } else {
        console.log("Get some hot chocolate!");
      }
    } else if (time < 22) {
      if (day == "Wednesday") {
        console.log("Get yourself some strawberry ice cream!");
      } else {
        console.log("Get yourself some vanilla ice cream!");
      }
    } else if (time >= 22) {
      console.log("Great work, go to sleep!");
    }
  } else {
    console.log("Get back to work!");
  }
}

// console.log("FEATURE 2");
// yourReward(true, 9);
// yourReward(false, 10);
// yourReward(true, 11);
// yourReward(true, 15);
// yourReward(true, 16);
// yourReward(true, 21, "Wednesday");
// yourReward(true, 21, "Tuesday");
// yourReward(true, 22);

/*
FEATURE 3

Building off Feature 2, I want my options for the 3 pm - 6 pm slot to be a random selection: 
if the time is even, I want my selections to be ice cream, cookies, or candy. If the time is odd, 
I want my selections to be hot chocolate, tea, or cake.
*/

function yourReward(finished, time, day) {
  oddOptions = ["ice cream", "cookies", "candy"];
  evenOptions = ["hot chocolate", "tea", "cake"];

  if (finished) {
    if (time < 10) {
      console.log("Have a latte!");
    } else if (time < 15) {
      console.log("Grab a hot chocolate!");
    } else if (15 <= time < 18) {
      // get a random number from 0-2
      randomIndex = Math.floor(Math.random() * 3);
      if (time % 2 != 0) {
        choice = oddOptions[randomIndex];
        console.log("Pick a flavor of " + choice + "!");
      } else {
        choice = evenOptions[randomIndex];
        console.log("Get some hot " + choice + "!");
      }
    } else if (time < 22) {
      if (day == "Wednesday") {
        console.log("Get yourself some strawberry ice cream!");
      } else {
        console.log("Get yourself some vanilla ice cream!");
      }
    } else if (time >= 22) {
      console.log("Great work, go to sleep!");
    }
  } else {
    console.log("Get back to work!");
  }
}

// console.log("FEATURE 3");
// yourReward(true, 9);
// yourReward(false, 10);
// yourReward(true, 11);
// yourReward(true, 15);
// yourReward(true, 16);
// yourReward(true, 21, "Wednesday");
// yourReward(true, 21, "Tuesday");
// yourReward(true, 22);
