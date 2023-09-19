function pushFront(arr, val) {
	for (let i = arr.length; i > 0; i--) {
		arr[i] = arr[i - 1];
	}
	arr[0] = val;
	return arr;
}

console.log(pushFront([5, 7, 2, 3], 8)); // [8, 5, 7, 2, 3]

function popFront(arr) {
	let val = arr[0];
	for (let i = 0; i < arr.length; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length = arr.length - 1;
	console.log(arr);
	return val;
}

console.log(popFront([0, 5, 10, 15])); // [ 5, 10, 15 ], 0

function insertAt(arr, idx, val) {
	for (let i = arr.length; i > idx; i--) {
		arr[i] = arr[i - 1];
	}
	arr[idx] = val;
	return arr;
}

console.log(insertAt([100, 200, 5], 2, 311)); // [100, 200, 311, 5]

function removeAt(arr, idx) {
	let val = arr[idx];
	for (let i = idx; i < arr.length; i++) {
		arr[i] = arr[i + 1];
	}
	arr.length = arr.length - 1;
	console.log(arr);
	return val;
}

console.log(removeAt([1000, 3, 204, 77], 1)); // [ 1000, 204, 77 ], 3

function swapPairs(arr) {
	for (let i = 0; i < arr.length - 1; i += 2) {
		let temp = arr[i];
		arr[i] = arr[i + 1];
		arr[i + 1] = temp;
	}
	return arr;
}

console.log(swapPairs([1, 2, 3, 4])); // [2, 1, 4, 3]

function removeDuplicates(arr) {
	for (let i = 0; i < arr.length; i++) {
		if (arr[i] === arr[i + 1]) {
			removeAt(arr, i);
			i--;
		}
	}
	return arr;
}

console.log(removeDuplicates([-2, -2, 3.14, 5, 5, 10])); // [ -2, 3.14, 5, 10 ]
