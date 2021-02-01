console.log("Working!")

let theme = localStorage.getItem('themes')

if (theme == null){
	themeChange('light')
} else {
	themeChange(theme)
}

let themeDots = document.getElementsByClassName('theme-dots')

for (var i = 0; themeDots.length > i; i++) {
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log("Option is selected!", mode)
		themeChange(mode)
	})
}

function themeChange(mode){
	if (mode == 'light'){
		document.getElementById('theme-style').href = "static/css/default.css"
	}

	if (mode == 'blue'){
		document.getElementById('theme-style').href = "static/css/blue.css"
	}

	if (mode == 'green'){
		document.getElementById('theme-style').href = "static/css/green.css"
	}

	if (mode == 'purple'){
		document.getElementById('theme-style').href = "static/css/purple.css"
	}

	localStorage.setItem('themes', mode)
}