// 点击顺序和倒序时记录用户数据
$(function () {
    $(".btn_collection").each(function () {
        $.ajax({
            url: 'userdata.ashx?d=' + new Date().getTime(),
            dataType: 'json',
            data: { tp: 7, mid: MANGABZ_COMIC_MID },
            type: 'POST',
            success: function (data) {
                if (data && data.msg == "1") {
                    if ($(".detail-info-btn-icon-2").length > 0) {
                        $(".detail-info-btn-icon-2").attr("src", MANGABZ_CSS + "images/icon_collection_2.png");
                    }
                }
            }
        });
    });
});
// 收藏事件
function setBookmarker(cid, mid, p, uid) {
    if (uid <= 0)
    {
        window.location.href = "/login/";
    }
    $.ajax({
        url: 'bookmarker.ashx?d=' + new Date().getTime(),
        dataType: 'json',
        data: { cid: cid, mid: mid, page: p, uid: uid, language: 1 },
        type: 'POST',
        success: function (msg) {
            if (msg.Value == "1") {
                if ($(".detail-info-btn-icon-2").length > 0) {
                    var collectionsrc = $(".detail-info-btn-icon-2").attr("src");
                    if (collectionsrc == MANGABZ_CSS + "images/icon_collection_2.png") {
                        ShowDialog(MANGABZ_SHOWTRADITIONAL == "True" ? "取消收藏" : "取消收藏");
                        $(".detail-info-btn-icon-2").attr("src", MANGABZ_CSS + "images/icon_collection_1.png");
                    }
                    else {
                        ShowDialog(MANGABZ_SHOWTRADITIONAL == "True" ? "收藏成功" : "收藏成功");
                        $(".detail-info-btn-icon-2").attr("src", MANGABZ_CSS + "images/icon_collection_2.png");
                    }
                }
            }
            else if (msg.Value == "2")
                ShowDialog(MANGABZ_SHOWTRADITIONAL == "True" ? "收藏失敗" : "收藏失败");
            else {
                ShowDialog(MANGABZ_SHOWTRADITIONAL == "True" ? "收藏成功" : "收藏成功");
            }
        }
    });
}

$(function () {
    $(".fold_open").click(function () {
        $(this).next().show();
        $(this).hide();
    });
    $(".fold_close").click(function () {
        $(this).parent().hide();
        $(this).parent().prev().show();
    });
});

// 倒序正序
function changeSort() {
    if (MANGABZ_COMIC_SORT == 2) {
        MANGABZ_COMIC_SORT = 1;
        $('.detail-list-form-title-icon').attr('src', MANGABZ_CSS+'images/icon_sort_up.png');
        $('.detail-list-form-title-right span').text('正序');
    }
    else {
        MANGABZ_COMIC_SORT = 2;
        $('.detail-list-form-title-icon').attr('src', MANGABZ_CSS+'images/icon_sort_down.png');
        $('.detail-list-form-title-right span').text('倒序');
    }
    $("#chapterlistload").load("/template-" + MANGABZ_COMIC_MID + "-s" + MANGABZ_COMIC_SORT + "/");
    $('.detail-list-form-more').removeClass('hide');
}
// 展开
function showMoreItem() {
    $('.detail-list-form-item').removeClass('hide');
    $('.detail-list-form-more').addClass('hide');
}

function showMoreContent() {
    $('.detail-info-content-1').hide();
    $('.detail-info-content-2').show();
    $('.detail-info-content a').hide();
}
