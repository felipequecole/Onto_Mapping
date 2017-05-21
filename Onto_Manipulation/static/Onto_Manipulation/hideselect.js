/**
 * Created by felipequecole on 19/05/17.
 */
$(function () {
   $('window').ready(function () {
      $('#generalizations').addClass('hide');
      $('#mutexExceptions').addClass('hide');
      $('#range').addClass('hide');
      $('#domain').addClass('hide');
      $('div').removeClass('hide');
   });
});

   $(window).on('load', function () {
    $('.preloader').fadeOut(1000); // set duration in brackets
});



