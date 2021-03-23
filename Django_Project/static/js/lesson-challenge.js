$(function(){
	
	//query the page for element with id "btnSubmitCode" (among others)
	var btnSubmit = $('#btnSubmitCode');
	var codeArea = $('#codeArea');
	
	//add an event handler for the button
	btnSubmit.on('click', function() {
		console.log('I was clicked!');
		
		//contents of the code area
		var codeAreaContents = codeArea.val();
		
		var dataToSubmit = {
			code: codeAreaContents
		}
		
		//create a POST request to /challenge/submit (https://api.jquery.com/jQuery.post/)
		$.post('/challenge/submit', dataToSubmit)
		.then(function(data) {
			console.log(data);
		})
		.fail(function(err) {
			console.log(err);
		})
	})
})