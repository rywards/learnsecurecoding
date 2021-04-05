//This script is meant to be used by a button in order to 
//scroll up to the lesson on the lesson-challenged page
$(function(){
    var btnScrollUp = $('#btnScrollLesson');

    btnScrollUp.on('click', function(){
        console.log('I was clicked');
        document.getElementById("lessonTitle").scrollIntoView({behavior: "smooth"}); 

    })
})