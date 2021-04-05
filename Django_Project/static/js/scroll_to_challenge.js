//This script is meant to be used by a button in order to 
//scroll down to the challenge on the lesson-challenge page. 
//Matt Williams
$(function(){
    var btnScrollDown = $('#btnScrollChallenge');

    btnScrollDown.on('click', function(){
        console.log('I was clicked');
        document.getElementById("codeArea").scrollIntoView({behavior: "smooth"}); 

    })
})