$(function () {
    var ol = $('#upload ol');
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