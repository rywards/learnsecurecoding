$(function(){

	//query the page for element with id "btnSubmitCode" (among others)
	var btnSubmit = $('#btnSubmitCode');
    var btnProceed = $('#btnProceed');
	var overlay = $(document.createElement('div'))
		.addClass('overlay')
		.append(
			$(document.createElement('p'))
			.addClass('w3-xlarge')
			.text('Submitting...')
		);

	//add an event handler for the button
	btnSubmit.on('click', function() {

        if(unit_id == tut_unit_id && lesson_id == tut_lesson1_id) {
            btnProceed.prop("disabled", false);
        }
		
        else {
            //contents of the code area
            var codeAreaContents = editor.getValue();

            var dataToSubmit = {    
                code: codeAreaContents,
                lesson_id: lesson_id
            }
			
			//add overlay to screen
			showOverlay();

            //create a POST request to /challenge/submit (https://api.jquery.com/jQuery.post/)
            $.post('/unit/'+ unit_id + '/lessons/' + lesson_id +'/' , dataToSubmit)
            .then(function(data) {
                console.log(data);
				$('#response_text').html(data['message']);

                if (data["success_state"] == 1){
                    btnProceed.prop("disabled",false);
                }

            })
			.fail(function(response) {
				$('#response_text').html('Sorry, an error occurred while submitting your code. Please try again.');
			})
			.always(function(response) {
				console.log('done');
				hideOverlay();
			});
        }
	});

	//This function is meant to be used by a button in order to
	//go back to the unit-overview page from the lesson-challenge page
	var btnUnit = $("#btnUnit");

	btnUnit.on('click', function() {
		console.log('Unit button was clicked');

		window.location.href = '/unit/' + unit_id + "/lessons"
	});

	//This funtion sets the previous code cookie
	//var codeArea = $('#codeArea');
	editor.on('change', function(){
		var codeAreaContents = editor.getValue();
		var lesson_cookie = 'savedCode_lesson' + lesson_id; 
		localStorage.setItem(lesson_cookie, codeAreaContents);
	});

	//This function is meant to be used by a button on the lesson-challenge page
	//in order to reset the challenge for that given lesson. 
	var btnReset = $('#btnReset');

	btnReset.on('click', function(){

		$.ajax({
			url:'/challenges/' + challenge_id + '.json/',   
			method: "GET",
			dataType: 'json',
			success: function(response){
				var lesson_cookie = 'savedCode_lesson' + lesson_id;
				localStorage.removeItem(lesson_cookie);
				editor.getDoc().setValue(response['challengeoverview'])
			}
		});
	})

	//This function is meant to be used by a button in order to
	//scroll down to the challenge on the lesson-challenge page.
	var btnScrollDown = $('#btnScrollChallenge');

	btnScrollDown.on('click', function(){
		console.log('I was clicked');
		document.getElementById("codeEnter").scrollIntoView({behavior: "smooth"});

	});

	//This function is meant to be used by a button in order to
	//scroll up to the lesson on the lesson-challenged page
	var btnScrollUp = $('#btnScrollLesson');

	btnScrollUp.on('click', function(){
		console.log('I was clicked');
		document.getElementById("lessonTitle").scrollIntoView({behavior: "smooth"});

	});


	//This function is meant to be used by a button in order to
	//take the user to the next lesson after completing the current lesson

	var btnProceed = $('#btnProceed');

	btnProceed.on('click', function(){
		const url_begin = "http://"
		var url_additive = '';

		if(lesson_id < num_Lessons){
			url_additive = '/unit/'+ unit_id + '/lessons/' + (lesson_id + 1) +'/'
		}

		var current_url = $(location).attr("href");
		var index_of_slash = current_url.indexOf('/', url_begin.length);
		var base_url = (index_of_slash == - 1) ? current_url : current_url.slice(0, index_of_slash);

		window.location.assign(base_url.concat(url_additive));

	});
	
	function showOverlay() {
		overlay.appendTo(document.body);
	}
	
	function hideOverlay() {
		overlay.remove();
	}
});