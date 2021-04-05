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