function buttonClicked(element) {
	element.classList.add('clicked');

	setTimeout(function () {
		element.classList.remove('clicked');
	}, 100);
}
