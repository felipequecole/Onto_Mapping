$(function () {
    var ol = $('#upload ol');
    //Abre o dialog
    $('body').on('click', '#openUploadXML', function (e) {
        e.preventDefault();
        $('#upload ol').empty();
        $('#uploadModal').modal('show');
    });

    $('body').on('click', '#openUploadXLS', function (e) {
        e.preventDefault();
        $('#upload ol').empty();
        $('#uploadModalXLS').modal('show');
    });

    $('#upload#submit').click(function () {
        $('#upload').getElementById("myform").submit()

    });


});