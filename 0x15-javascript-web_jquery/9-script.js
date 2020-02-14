/* fetches from URL, displays value of hello from fetch in DIV#hello */
$.ajax({
  type: 'GET',
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  success: (res) => {
    $('#hello').text(res.hello);
  }
});
