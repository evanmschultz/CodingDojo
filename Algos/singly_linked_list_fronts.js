class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}

class SinglyLinkedList {
	constructor() {
		this.head = null;
	}

	addFront(value) {
		const newNode = new Node(value); // Step 1: Create a new node
		newNode.next = this.head; // Step 2: Point the next of new node to current head
		this.head = newNode; // Step 3: Update head to be the new node

		return this.head; // Return the new head node
	}

	removeFront() {
		if (this.head === null) {
			return null;
		}
		this.head = this.head.next;
		return this.head;
	}

	front() {
		if (this.head === null) {
			return null;
		}
		return this.head.data;
	}
}

// Examples
const SLL1 = new SinglyLinkedList();
console.log(SLL1.addFront(18)); // => Node { data: 18, next: null }
console.log(SLL1.addFront(5)); // => Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.addFront(73)); // => Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }
console.log(SLL1.removeFront()); // => Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.front()); // => 5
console.log(SLL1.removeFront()); // => Node { data: 18, next: null }
console.log(SLL1.front()); // 18
console.log(SLL1.removeFront()); // => null
console.log(SLL1.front()); // => null
