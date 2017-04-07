$(function () {
    var ol = $('#upload ol');
    //Quando clica em a ele clica em input
    $('#drop a').click( function () {
        $(this).parent().find('input').click();
    });
    //Abre o dialog
    $('body').on('click', '#openUpload', function (e) {
        e.preventDefault();
        $('#upload ol').empty();
        $('#uploadModal').modal('show');
    });

    $('#upload#submit').click(function () {
        $('#upload').getElementById("myform").submit()

    });


});