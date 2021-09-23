$(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();

    $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      const lang = $('INPUT#language_code').val();

      $.get('https://www.fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
