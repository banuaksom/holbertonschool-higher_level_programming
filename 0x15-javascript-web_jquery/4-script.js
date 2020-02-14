/**
 * toggles class of HTML tag HEADER between red & green when
 * DIV#toggle_header is clicked
 */
$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
