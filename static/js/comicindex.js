$(document).ready(function () {

});
var beforeIndex = 0;
$("#hotCatgoryId .list-con-title-class a").hover(function () {
    $("#hotCatgoryId .list-con-title-class a").removeClass("active");
    $(this).addClass("active");
    var id = $("#hotCatgoryId .list-con-title-class a").index(this);
    if (beforeIndex != id)
         $($("#hotCatgoryId .index-manga-list")[beforeIndex]).hide(400);
    $($("#hotCatgoryId .index-manga-list")[id]).show(400);
    beforeIndex = id;
    $("#hotCatgoryId .list-con-title-more").attr("href", $(this).attr("href"));
}, function () {});

$(".rank-list .list").hover(function () {
    var tempObj = $(".rank-list .list.rank-item-1");
    $(tempObj).removeClass("rank-item-1");
    $(tempObj).addClass("rank-item-2");
    $(tempObj).find("img").hide();

    $(this).removeClass("rank-item-2");
    $(this).addClass("rank-item-1");
    $(this).find("img").show();
}, function () { });
