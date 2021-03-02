$(function () {
    $('.lang-option.active').click(function () {
        $('.lang-option.noactive').toggle();
    });
});
function ShowDialog(title, timeout) {
    if (!timeout)
    {
        timeout = 2000;
    }
    $(".toast-win").text(title);
    $(".toast-win").show();
    setTimeout(function () {
        $(".toast-win").hide();
    }, timeout);
}