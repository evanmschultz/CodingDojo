// Remove Blanks
function removeBlanks(str) {
	let newStr = '';
	for (let i = 0; i < str.length; i++) {
		if (str[i] != ' ') {
			newStr += str[i];
		}
	}
	return newStr;
}

console.log(removeBlanks(' Pl ayTha tF u nkyM usi c ')); // "PlayThatFunkyMusic"

// Get Digits
function getDigits(str) {
	let newStr = '';
	for (let i = 0; i < str.length; i++) {
		if (!isNaN(str[i])) {
			newStr += str[i];
		}
	}
	return Number(newStr);
}

console.log(getDigits('abc8c0d1ngd0j0!8')); // 801008

// Acronyms
function acronym(str) {
	let newStr = '';
	let arr = str.split(' ');
	for (let i = 0; i < arr.length; i++) {
		if (arr[i]) {
			newStr += arr[i][0].toUpperCase();
		}
	}
	return newStr;
}

console.log(acronym(" there's no free lunch - gotta pay yer way. ")); // TNFL-GPYW

// Count Non-Spaces
function countNonSpaces(str) {
	let count = 0;
	for (let i = 0; i < str.length; i++) {
		if (str[i] != ' ') {
			count++;
		}
	}
	return count;
}

console.log(countNonSpaces('Honey pie, you are driving me crazy')); // 29

// Remove Shorter Strings
function removeShorterStrings(arr, val) {
	let newArr = [];
	for (let i = 0; i < arr.length; i++) {
		if (arr[i].length >= val) {
			newArr.push(arr[i]);
		}
	}
	return newArr;
}

console.log(
	removeShorterStrings(
		['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'],
		4
	)
); // ['Good morning', 'sunshine', 'Earth', 'says', 'hello']
