$(function(){
	
	//query the page for element with id "btnSubmitCode" (among others)
	var btnSubmit = $('#btnSubmitCode');
	var codeArea = $('#codeArea');
    var codeAreaClass = $('#codeEnter');
	
	//add an event handler for the button
	btnSubmit.on('click', function() {
		console.log('I was clicked!');
		
		//contents of the code area
		var codeAreaContents = codeArea.val();
		
		var dataToSubmit = {
			code: codeAreaContents,
			lesson_id: lesson_id 
		}
		
		//create a POST request to /challenge/submit (https://api.jquery.com/jQuery.post/)
		$.post('/unit/'+ unit_id + '/lessons/' + lesson_id +'/' , dataToSubmit)
		.then(function(data) {
			console.log(data);
            codeAreaClass.append(data['message'])

		})
		.fail(function(err) {
			console.log(err);
		})
	})
})

//This script is meant to be used by a button in order to 
//go back to the unit-overview page from the lesson-challenge page 
$(function(){
    var btnUnit = $("#btnUnit");

    btnUnit.on('click', function() {
        console.log('Unit button was clicked');
        
        window.location.href = '/unit/' + unit_id + "/lessons"
    })
})

//This script is meant to be used by a button on the lesson-challenge page
//in order to reset the challenge for that given lesson. 
$(function(){


    var btnReset = $('#btnReset');
    var codeArea = $('#codeArea');

    btnReset.on('click', function(){

        $.ajax({
            url:'/challenges/' + challenge_id + '.json/',
            method: "GET",
            dataType: 'json',
            success: function(response){
                codeArea.val(response['challengeoverview']);
            }
        });
    })
})

//This script is meant to be used by a button in order to 
//scroll down to the challenge on the lesson-challenge page. 
$(function(){
    var btnScrollDown = $('#btnScrollChallenge');

    btnScrollDown.on('click', function(){
        console.log('I was clicked');
        document.getElementById("codeArea").scrollIntoView({behavior: "smooth"}); 

    })
})

//This script is meant to be used by a button in order to 
//scroll up to the lesson on the lesson-challenged page
$(function(){
    var btnScrollUp = $('#btnScrollLesson');

    btnScrollUp.on('click', function(){
        console.log('I was clicked');
        document.getElementById("lessonTitle").scrollIntoView({behavior: "smooth"}); 

    })
})