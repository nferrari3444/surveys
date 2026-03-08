const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");


console.log('ahora??')

// Add Event Listeners
btn.addEventListener("click", () => {

    console.log('hola hola')
	menu.classList.toggle("hidden");
	});
