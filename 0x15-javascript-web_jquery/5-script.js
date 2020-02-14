/* adds LI element to list when DIV#add_item is clicked */
$('#add_item').click(() => {
  $('ul.my_list').append($('<li>Item</li>'));
});
