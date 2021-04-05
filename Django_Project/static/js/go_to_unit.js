//This script is meant to be used by a button in order to 
//go back to the unit-overview page from the lesson-challenge page 
$(function(){
    var btnUnit = $("#btnUnit");

    btnUnit.on('click', function() {
        console.log('Unit button was clicked');
        
        window.location.href = '/unit/' + unit_id + "/lessons/"
    })
})