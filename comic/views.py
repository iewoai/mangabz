from django.shortcuts import render
from mangabz.utils import *
import json
from django.http import HttpResponse


def home(request):
    # 首页左1(5:3)大右3(10:3, 5:3*2)小图，可调整位置，丢全站热度最高
    data_banner = [
        {
            "rowkey":"73",
            "title":"鬼灭之刃",
            "detail_url":"/73bz/",
            "img_url":"http://static.mangabz.com/mangabz/12/2019/10/26/b105f94957af4df8.jpg",# 图片比例：5:3 * 120px
        },
        {
            "rowkey":"266",
            "title":"咒术回战",
            "detail_url":"/266bz/",
            "img_url":"http://static.mangabz.com/mangabz/86/2021/2/2/12d889a402e44b11.jpg",# 图片比例：10:3 * 60px
        },
        {
            "rowkey":"2255",
            "title":"干杂活我乃最强",
            "detail_url":"/2255bz/",
            "img_url":"http://static.mangabz.com/mangabz/86/2021/2/2/cdf6fe4e81084b7a.jpg",# 图片比例：5:3 * 60px
        },
        {
            "rowkey":"1294",
            "title":"最后再拜托您一件事可以吗",
            "detail_url":"/1294bz/",
            "img_url":"http://static.mangabz.com/mangabz/86/2021/2/2/20078eee91644ef9.jpg",# 图片比例：5:3 * 60px
        }
    ]
    data_popular = [
        {      
            "rowkey":"242",
            "title":"篮球少年王",
            "class":["运动"],
            "detail_url":"/242bz/",
            "cover_img_url":"http://cover.mangabz.com/1/242/20191203160605_180x240_20.jpg",
        },
        {      
            "rowkey":"236",
            "title":"工作细胞black",
            "class":[],
            "detail_url":"/236bz/",
            "cover_img_url":"http://cover.mangabz.com/1/236/20191203155214_180x240_20.jpg",
        },
        {      
            "rowkey":"234",
            "title":"极主夫道",
            "class":["生活"],
            "detail_url":"/234bz/",
            "cover_img_url":"http://cover.mangabz.com/1/234/20191220110607_180x240_25.jpg",
        },
        {      
            "rowkey":"139",
            "title":"海贼王",
            "class":["热血"],
            "detail_url":"/139bz/",
            "cover_img_url":"http://cover.mangabz.com/1/139/20191203153434_180x240_26.jpg",
        }
    ]
    data_rank = [
        {      
            "rowkey":"134",
            "title":"不过是蜘蛛什么的",
            "class":["冒险"],
            "detail_url":"/134bz/",
            "cover_img_url":"http://cover.mangabz.com/1/134/20191203152816_320x246_33.jpg",
        },
        {      
            "rowkey":"73",
            "title":"鬼灭之刃",
            "class":["热血","冒险"],
            "detail_url":"/73bz/",
            "cover_img_url":"http://cover.mangabz.com/1/73/20191203103229_320x246_47.jpg",
        },
        {      
            "rowkey":"123",
            "title":"平凡职业成就世界最强 零",
            "class":["冒险","魔法"],
            "detail_url":"/123bz/",
            "cover_img_url":"http://cover.mangabz.com/1/123/20191220112220_320x246_39.jpg",
        },
        {      
            "rowkey":"91",
            "title":"五等分的花嫁",
            "class":["恋爱","校园"],
            "detail_url":"/91bz/",
            "cover_img_url":"http://cover.mangabz.com/1/91/20191203131109_320x246_34.jpg",
        },
        {      
            "rowkey":"72",
            "title":"平凡职业成就世界最强",
            "class":["冒险"],
            "detail_url":"/72bz/",
            "cover_img_url":"http://cover.mangabz.com/1/72/20191220112108_320x246_39.jpg",
        },
        {      
            "rowkey":"64",
            "title":"炎炎之消防队",
            "class":["热血"],
            "detail_url":"/64bz/",
            "cover_img_url":"http://cover.mangabz.com/1/64/20191203100442_320x246_42.jpg",
        },
        {      
            "rowkey":"38",
            "title":"一拳超人",
            "class":["热血","冒险"],
            "detail_url":"/38bz/",
            "cover_img_url":"http://cover.mangabz.com/1/38/20191206093248_320x246_31.jpg",
        }
    ]
    data_recommend = [
        {      
            "rowkey":"249",
            "title":"名侦探柯南",
            "class":["悬疑"],
            "detail_url":"/249bz/",
            "cover_img_url":"http://cover.mangabz.com/1/249/20191203162547_180x240_21.jpg",
        },
        {      
            "rowkey":"238",
            "title":"樱兰高校男公关部",
            "class":["恋爱","校园"],
            "detail_url":"/238bz/",
            "cover_img_url":"http://cover.mangabz.com/1/238/20191203155800_180x240_21.jpg",
        },
        {      
            "rowkey":"136",
            "title":"入间同学入魔了",
            "class":["魔法"],
            "detail_url":"/136bz/",
            "cover_img_url":"http://cover.mangabz.com/1/136/20191203153041_180x240_27.jpg",
        },
        {      
            "rowkey":"72",
            "title":"平凡职业成就世界最强",
            "class":["冒险"],
            "detail_url":"/72bz/",
            "cover_img_url":"http://cover.mangabz.com/1/119/20191218155827_180x240_31.jpg",
        },
        {      
            "rowkey":"119",
            "title":"化物语",
            "class":[],
            "detail_url":"/119bz/",
            "cover_img_url":"http://cover.mangabz.com/1/64/20191203100442_320x246_42.jpg",
        },
        {      
            "rowkey":"83",
            "title":"约定的梦幻岛",
            "class":["冒险","科幻","悬疑"],
            "detail_url":"/83bz/",
            "cover_img_url":"http://cover.mangabz.com/1/83/20191203105842_180x240_27.jpg",
        },
        {      
            "rowkey":"261",
            "title":"天是红河岸",
            "class":["悬疑"],
            "detail_url":"/261bz/",
            "cover_img_url":"http://cover.mangabz.com/1/261/20191018193301_180x240_19.jpg",
        },
        {      
            "rowkey":"260",
            "title":"和恋爱相恋的由加里",
            "class":["恋爱"],
            "detail_url":"/260bz/",
            "cover_img_url":"http://cover.mangabz.com/1/260/20191212155610_180x240_19.jpg",
        },
        {      
            "rowkey":"259",
            "title":"汤神君没有朋友",
            "class":["运动"],
            "detail_url":"/259bz/",
            "cover_img_url":"http://cover.mangabz.com/1/259/20191203164916_180x240_24.jpg",
        },
        {      
            "rowkey":"285",
            "title":"魔笛MAGI",
            "class":["冒险"],
            "detail_url":"/258bz/",
            "cover_img_url":"http://cover.mangabz.com/1/258/20191203164656_180x240_26.jpg",
        },
        {      
            "rowkey":"255",
            "title":"粗点心战争",
            "class":[],
            "detail_url":"/255bz/",
            "cover_img_url":"http://cover.mangabz.com/1/255/20191203163854_180x240_11.jpg",
        },
        {      
            "rowkey":"253",
            "title":"零的日常",
            "class":["悬疑"],
            "detail_url":"/253bz/",
            "cover_img_url":"http://cover.mangabz.com/1/253/20191203163442_180x240_23.jpg",
        }
    ]
    data_ascend = [
        {
            "title":"关于我转生后成为史莱姆的那件事",
            "author":["川上泰树","伏濑"],
            "rowkey":"207",
            "detail_url":"/207bz/",
            "cover_img_url":"http://cover.mangabz.com/1/207/20191203094359_180x240_16.jpg",
            "description":"普通上班族三上悟（37，童贞）遇刺身亡。迎接他的，是转生后的异世界史莱姆生活……",
            "class":["热血","冒险"],
        },
        {
            "title":"拳愿阿修罗",
            "author":["三肉必起","牙霸子","达露没恩"],
            "rowkey":"54",
            "detail_url":"/54bz/",
            "cover_img_url":"http://cover.mangabz.com/1/54/20191203093051_180x240_19.jpg",
            "description":"赌上性命和荣耀的绝命赛！",
            "class":["热血","运动"],
        },
        {
            "title":"夹在我女友和青梅竹马间的各种修罗场",
            "author":["裕时悠示","七介"],
            "rowkey":"178",
            "detail_url":"/178bz/",
            "cover_img_url":"http://cover.mangabz.com/1/178/20191202155351_180x240_19.jpg",
            "description":"裕时悠示原作的轻小说《夹在我女友和青梅竹马间的修罗场》...",
            "class":["热血"],
        },
        {
            "title":"欢迎来到实力至上主义的教室",
            "author":["衣笠彰梧","一乃ゆゆ"],
            "rowkey":"75",
            "detail_url":"/75bz/",
            "cover_img_url":"http://cover.mangabz.com/1/75/20191203103551_180x240_17.jpg",
            "description":"对希望的升学、就业目标有著近乎100%的达成率，全国屈指可...",
            "class":["校园"],
        },
        {
            "title":"亚尔斯兰战记",
            "author":["荒川弘","田中芳树"],
            "rowkey":"42",
            "detail_url":"/42bz/",
            "cover_img_url":"http://cover.mangabz.com/1/42/20191202164804_180x240_15.jpg",
            "description":"少年终会成长为男人，男人将会登上王位，真正的英雄是谁？...",
            "class":[],
        },
        {
            "title":"白银之匙",
            "author":["荒川弘"],
            "rowkey":"28",
            "detail_url":"/28bz/",
            "cover_img_url":"http://cover.mangabz.com/1/28/20191202154519_180x240_17.jpg",
            "description":"因为某些理由不愿归家的少年特意从札幌的重点初中升入北部...",
            "class":["生活"],
        }
    ]
    data_hot_class = [
        {
            "class":"热血",
            "comic_list":[
                {      
                    "rowkey":"265",
                    "title":"石纪元（Dr.Stone）",
                    "class":["热血","冒险"],
                    "detail_url":"/265bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/265/20191203170212_180x240_27.jpg",
                },
                {      
                    "rowkey":"14654",
                    "title":"游戏王SEVENS 卢克！爆裂霸道传！！",
                    "class":["热血"],
                    "detail_url":"/14654bz/",
                    "cover_img_url":"http://cover.mangabz.com/15/14654/20201010164703_180x240_24.jpg",
                },
                {      
                    "rowkey":"511",
                    "title":"进击的巨人",
                    "class":["热血","冒险"],
                    "detail_url":"/511bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/511/20191206153908_180x240_22.jpg",
                },
                {      
                    "rowkey":"15260",
                    "title":"疫神的病历簿",
                    "class":["热血","冒险","魔法"],
                    "detail_url":"/15260bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/253/20191203163442_180x240_23.jpg",
                },
                {      
                    "rowkey":"1573",
                    "title":"棒球大联盟2nd",
                    "class":["热血","运动"],
                    "detail_url":"/1573bz/",
                    "cover_img_url":"http://cover.mangabz.com/2/1573/20191216151856_180x240_22.jpg",
                },
                {      
                    "rowkey":"266",
                    "title":"咒术回战",
                    "class":["热血","冒险"],
                    "detail_url":"/266bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/266/20191203170525_180x240_26.jpg",
                }
            ]
        },
        {
            "class":"恋爱",
            "comic_list":[
                {      
                    "rowkey":"60",
                    "title":"辉夜大小姐想让我告白 ~天才们的恋爱头脑战~",
                    "class":["恋爱"],
                    "detail_url":"/60bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/60/20191203095013_180x240_19.jpg",
                },
                {      
                    "rowkey":"15210",
                    "title":"此情即恋",
                    "class":["恋爱"],
                    "detail_url":"/15210bz/",
                    "cover_img_url":"http://cover.mangabz.com/16/15210/20201113192251_180x240_26.jpg",
                },
                {      
                    "rowkey":"7456",
                    "title":"超绝可爱男生等我回家",
                    "class":["恋爱"],
                    "detail_url":"/7456bz/",
                    "cover_img_url":"http://cover.mangabz.com/8/7456/20200516223404_180x240_20.jpg",
                },
                {      
                    "rowkey":"2258",
                    "title":"女友成双",
                    "class":["恋爱","校园"],
                    "detail_url":"/2258bz/",
                    "cover_img_url":"http://cover.mangabz.com/3/2258/20200304162942_180x240_22.jpg",
                },
                {      
                    "rowkey":"11104",
                    "title":"我们相恋的理由",
                    "class":["恋爱"],
                    "detail_url":"/11104bz/",
                    "cover_img_url":"http://cover.mangabz.com/12/11104/20200720164239_180x240_18.jpg",
                },
                {      
                    "rowkey":"9083",
                    "title":"若你想夺走",
                    "class":["恋爱"],
                    "detail_url":"/9083bz/",
                    "cover_img_url":"http://cover.mangabz.com/10/9083/20200608093216_180x240_17.jpg",
                }
            ]
        },
        {
            "class":"校园",
            "comic_list":[
                {      
                    "rowkey":"18939",
                    "title":"露出导演",
                    "class":["校园"],
                    "detail_url":"/18939bz/",
                    "cover_img_url":"http://cover.mangabz.com/19/18939/20210301223717_180x240_20.jpg",
                },
                {      
                    "rowkey":"2258",
                    "title":"女友成双",
                    "class":["校园","恋爱"],
                    "detail_url":"/2258bz/",
                    "cover_img_url":"http://cover.mangabz.com/3/2258/20200304162942_180x240_22.jpg",
                },
                {      
                    "rowkey":"13124",
                    "title":"请不要过分期待这样的我",
                    "class":["校园"],
                    "detail_url":"/13124bz/",
                    "cover_img_url":"http://cover.mangabz.com/14/13124/20200908110617_180x240_21.jpg",
                },
                {      
                    "rowkey":"11398",
                    "title":"时薪300日元的死神",
                    "class":["校园"],
                    "detail_url":"/11398bz/",
                    "cover_img_url":"http://cover.mangabz.com/12/11398/20200802000640_180x240_18.jpg",
                },
                {      
                    "rowkey":"7286",
                    "title":"复仇的教科书",
                    "class":["校园","悬疑"],
                    "detail_url":"/7286bz/",
                    "cover_img_url":"http://cover.mangabz.com/8/7286/20200509232302_180x240_14.jpg",
                },
                {      
                    "rowkey":"18683",
                    "title":"濑乃同学对恋爱一窍不通",
                    "class":["校园","恋爱"],
                    "detail_url":"/18683bz/",
                    "cover_img_url":"http://cover.mangabz.com/19/18683/20210214115530_180x240_24.jpg",
                }
            ]
        },
        {
            "class":"奇幻",
            "comic_list":[
                {      
                    "rowkey":"11270",
                    "title":"转生剑圣想要悠闲地生活",
                    "class":["冒险"],
                    "detail_url":"/11270bz/",
                    "cover_img_url":"http://cover.mangabz.com/12/11270/20200728154241_180x240_24.jpg",
                },
                {      
                    "rowkey":"10944",
                    "title":"僵尸少女小骸",
                    "class":["冒险"],
                    "detail_url":"/10944bz/",
                    "cover_img_url":"http://cover.mangabz.com/11/10944/20200714095753_180x240_16.jpg",
                },
                {      
                    "rowkey":"106",
                    "title":"图书馆的大魔法师",
                    "class":["冒险"],
                    "detail_url":"/106bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/106/20191220142953_180x240_18.jpg",
                },
                {      
                    "rowkey":"1007",
                    "title":"物语中的人",
                    "class":["魔法"],
                    "detail_url":"/1007bz/",
                    "cover_img_url":"http://cover.mangabz.com/2/1007/20191213093036_180x240_22.jpg",
                },
                {      
                    "rowkey":"5879",
                    "title":"驯服暴君后逃跑",
                    "class":["魔法"],
                    "detail_url":"/5879bz/",
                    "cover_img_url":"http://cover.mangabz.com/6/5879/20200422160138_180x240_24.jpg",
                },
                {      
                    "rowkey":"1654",
                    "title":"一不小心在异世界当上了最强魔王的十个孩子的妈妈",
                    "class":["魔法"],
                    "detail_url":"/1654bz/",
                    "cover_img_url":"http://cover.mangabz.com/2/1654/20191213104126_180x240_22.jpg",
                }
            ]
        },
        {
            "class":"科幻",
            "comic_list":[
                {      
                    "rowkey":"207",
                    "title":"关于我转生后成为史莱姆的那件事",
                    "class":["科幻"],
                    "detail_url":"/207z/",
                    "cover_img_url":"http://cover.mangabz.com/1/207/20191203094359_180x240_16.jpg",
                },
                {      
                    "rowkey":"18738",
                    "title":"坦克女孩",
                    "class":["科幻","魔法"],
                    "detail_url":"/18738bz/",
                    "cover_img_url":"http://cover.mangabz.com/19/18738/20210217204822_180x240_20.jpg",
                },
                {      
                    "rowkey":"917bz",
                    "title":"黑礁",
                    "class":["科幻"],
                    "detail_url":"/917bz/",
                    "cover_img_url":"http://cover.mangabz.com/1/917/20191209154104_180x240_23.jpg",
                },
                {      
                    "rowkey":"18421",
                    "title":"未来态：超级英雄军团<",
                    "class":["科幻","魔法"],
                    "detail_url":"/18421bz/",
                    "cover_img_url":"http://cover.mangabz.com/19/18421/20210129085112_180x240_24.jpg",
                },
                {      
                    "rowkey":"15153",
                    "title":"隐退人偶师的MMO机巧叙事诗",
                    "class":["冒险","科幻"],
                    "detail_url":"/15153bz/",
                    "cover_img_url":"http://cover.mangabz.com/16/15153/20201109100613_180x240_20.jpg",
                },
                {      
                    "rowkey":"14472",
                    "title":"真相部",
                    "class":["魔法"],
                    "detail_url":"/14472bz/",
                    "cover_img_url":"http://cover.mangabz.com/15/14472/20201001093954_180x240_22.jpg",
                }
            ]
        }
    ]
    data = {
        "banner": data_banner,
        "popular":data_popular,
        "rank":data_rank,
        "recommend":data_recommend,
        "ascend":data_ascend,
        "hot_class":data_hot_class,
    }
    return render(request, "home.html", {"data":data})

def detail(request, rowkey):
    data = {
        "title":"关于我转生后成为史莱姆的那件事",
        "cover_img_url":"http://cover.mangabz.com/1/207/20191203094359_360x480_53.jpg", #图片比例：3:4 * 120px
        "star":"2.0",
        "author":["川上泰树","伏濑"],
        "status":"连载中",
        "class":["科幻"],
        "rowkey":"207",
        "description":"普通上班族三上悟（37，童贞）遇刺身亡。迎接他的，是转生后的异世界史莱姆生活……",
        "first_chapter":{
            "chapter_url":"/m26072/",
            "title":"第一卷",
            "full_title":"",
        },
        "latest_chapter":{
            "chapter_url":"/m164936/",
            "title":"第81话",
            "full_title":"试看版",
        },
        "chapter_num":"81",
        "update_time":"2021-03-06 18:00",
    }
    return render(request, "detail.html", {"data":data})

def chapter(request, rowkey, sort):
    chapter_data = [{"chapter_url": "/m164936/", "full_title": "试看版", "title": "第81话", "page": "68"}, {"chapter_url": "/m160758/", "full_title": "试看版", "title": "第80话", "page": "32"}, {"chapter_url": "/m162658/", "full_title": "试看版", "title": "第79话", "page": "20"}, {"chapter_url": "/m155712/", "full_title": "试看版", "title": "第78话", "page": "40"}, {"chapter_url": "/m150977/", "full_title": "试看版", "title": "第77话", "page": "44"}, {"chapter_url": "/m146975/", "full_title": "试看版", "title": "第76话", "page": "32"}, {"chapter_url": "/m143158/", "full_title": "试看版", "title": "第75话", "page": "41"}, {"chapter_url": "/m138261/", "full_title": "试看", "title": "第74话", "page": "60"}, {"chapter_url": "/m132309/", "full_title": "试看版", "title": "第73话", "page": "40"}, {"chapter_url": "/m127243/", "full_title": "试看版", "title": "第72话", "page": "34"}, {"chapter_url": "/m122073/", "full_title": "试看版", "title": "第71话", "page": "38"}, {"chapter_url": "/m116555/", "full_title": "试看版", "title": "第70话", "page": "42"}, {"chapter_url": "/m113113/", "full_title": "特恩佩斯特复活祭", "title": "第69话", "page": "40"}, {"chapter_url": "/m108971/", "full_title": "", "title": "第68话", "page": "46"}, {"chapter_url": "/m108970/", "full_title": "", "title": "第67话", "page": "44"}, {"chapter_url": "/m108969/", "full_title": "", "title": "第66话", "page": "30"}, {"chapter_url": "/m108968/", "full_title": "", "title": "第65话", "page": "40"}, {"chapter_url": "/m108967/", "full_title": "", "title": "第64话", "page": "48"}, {"chapter_url": "/m82699/", "full_title": "逆袭时刻", "title": "第63话", "page": "27"}, {"chapter_url": "/m82698/", "full_title": "是魔物也是人类", "title": "第62话", "page": "19"}, {"chapter_url": "/m82697/", "full_title": "魔女的处罚", "title": "第61话", "page": "33"}, {"chapter_url": "/m82696/", "full_title": "希望的条件", "title": "第60话", "page": "26"}, {"chapter_url": "/m82695/", "full_title": "绝望与希望", "title": "第59话", "page": "55"}, {"chapter_url": "/m82694/", "full_title": "灾祸", "title": "第58话", "page": "32"}, {"chapter_url": "/m82693/", "full_title": "带来灾祸的来访者", "title": "第57话", "page": "26"}, {"chapter_url": "/m82692/", "full_title": "各自的盘算", "title": "第56话", "page": "26"}, {"chapter_url": "/m82691/", "full_title": "魔物的天敌", "title": "第55话", "page": "32"}, {"chapter_url": "/m26105/", "full_title": "", "title": "第54话", "page": "20"}, {"chapter_url": "/m26104/", "full_title": "", "title": "第53话", "page": "22"}, {"chapter_url": "/m15777/", "full_title": "", "title": "第52话", "page": "44"}, {"chapter_url": "/m15776/", "full_title": "", "title": "第51话", "page": "24"}, {"chapter_url": "/m15775/", "full_title": "", "title": "第50话", "page": "29"}, {"chapter_url": "/m15774/", "full_title": "", "title": "第49话", "page": "21"}, {"chapter_url": "/m15772/", "full_title": "", "title": "第48话", "page": "27"}, {"chapter_url": "/m26102/", "full_title": "", "title": "第47话", "page": "38"}, {"chapter_url": "/m26101/", "full_title": "", "title": "第46话", "page": "51"}, {"chapter_url": "/m26100/", "full_title": "", "title": "第45话", "page": "21"}, {"chapter_url": "/m26099/", "full_title": "", "title": "第44话", "page": "35"}, {"chapter_url": "/m26098/", "full_title": "", "title": "第43话", "page": "31"}, {"chapter_url": "/m26097/", "full_title": "", "title": "第42话", "page": "23"}, {"chapter_url": "/m26096/", "full_title": "", "title": "第41话", "page": "33"}, {"chapter_url": "/m26095/", "full_title": "", "title": "第40话", "page": "55"}, {"chapter_url": "/m26093/", "full_title": "", "title": "第39话", "page": "36"}, {"chapter_url": "/m26092/", "full_title": "", "title": "第38话", "page": "53"}, {"chapter_url": "/m26091/", "full_title": "", "title": "第37话", "page": "26"}, {"chapter_url": "/m26090/", "full_title": "", "title": "第36话", "page": "27"}, {"chapter_url": "/m26089/", "full_title": "", "title": "第35话", "page": "35"}, {"chapter_url": "/m26088/", "full_title": "", "title": "第34话", "page": "47"}, {"chapter_url": "/m26087/", "full_title": "", "title": "第33话", "page": "23"}, {"chapter_url": "/m26086/", "full_title": "", "title": "第32话", "page": "31"}, {"chapter_url": "/m26085/", "full_title": "", "title": "第31话", "page": "31"}, {"chapter_url": "/m26084/", "full_title": "", "title": "第30话", "page": "25"}, {"chapter_url": "/m26082/", "full_title": "", "title": "第29话", "page": "35"}, {"chapter_url": "/m26081/", "full_title": "", "title": "第28话", "page": "56"}, {"chapter_url": "/m26080/", "full_title": "", "title": "第27话", "page": "31"}, {"chapter_url": "/m26079/", "full_title": "", "title": "第26话", "page": "27"}, {"chapter_url": "/m26078/", "full_title": "", "title": "第25话", "page": "33"}, {"chapter_url": "/m26077/", "full_title": "", "title": "第24话", "page": "28"}, {"chapter_url": "/m26076/", "full_title": "", "title": "第23话", "page": "29"}, {"chapter_url": "/m26075/", "full_title": "", "title": "第22话", "page": "32"}, {"chapter_url": "/m26074/", "full_title": "", "title": "第21话", "page": "31"}, {"chapter_url": "/m26073/", "full_title": "", "title": "第20话", "page": "32"}, {"chapter_url": "/m26071/", "full_title": "", "title": "第19话", "page": "28"}, {"chapter_url": "/m26070/", "full_title": "", "title": "第18话", "page": "29"}, {"chapter_url": "/m26069/", "full_title": "", "title": "第17话", "page": "34"}, {"chapter_url": "/m26068/", "full_title": "", "title": "第16话", "page": "29"}, {"chapter_url": "/m26067/", "full_title": "", "title": "第15话", "page": "29"}, {"chapter_url": "/m26066/", "full_title": "", "title": "第14话", "page": "28"}, {"chapter_url": "/m26065/", "full_title": "", "title": "第13话", "page": "33"}, {"chapter_url": "/m26064/", "full_title": "", "title": "第12话", "page": "32"}, {"chapter_url": "/m26063/", "full_title": "", "title": "第11话", "page": "30"}, {"chapter_url": "/m26062/", "full_title": "", "title": "第10话", "page": "34"}, {"chapter_url": "/m26061/", "full_title": "", "title": "第9话", "page": "31"}, {"chapter_url": "/m26060/", "full_title": "", "title": "第8话", "page": "31"}, {"chapter_url": "/m26059/", "full_title": "", "title": "第7话", "page": "30"}, {"chapter_url": "/m26058/", "full_title": "", "title": "第6话", "page": "26"}, {"chapter_url": "/m26057/", "full_title": "", "title": "第5话", "page": "29"}, {"chapter_url": "/m26056/", "full_title": "", "title": "第4话", "page": "28"}, {"chapter_url": "/m26055/", "full_title": "", "title": "第3话", "page": "33"}, {"chapter_url": "/m26054/", "full_title": "", "title": "第2话", "page": "37"}, {"chapter_url": "/m26053/", "full_title": "", "title": "第1话", "page": "48"}, {"chapter_url": "/m26124/", "full_title": "", "title": "成为史莱姆的那件事 现场录音", "page": "5"}, {"chapter_url": "/m26123/", "full_title": "", "title": "成为史莱姆的那件事 漫步08", "page": "21"}, {"chapter_url": "/m26122/", "full_title": "", "title": "成为史莱姆的那件事 漫步07", "page": "10"}, {"chapter_url": "/m26121/", "full_title": "", "title": "成为史莱姆的那件事 漫步06", "page": "21"}, {"chapter_url": "/m26120/", "full_title": "", "title": "成为史莱姆的那件事 漫步05", "page": "19"}, {"chapter_url": "/m26119/", "full_title": "", "title": "成为史莱姆的那件事 漫步03", "page": "23"}, {"chapter_url": "/m26118/", "full_title": "", "title": "成为史莱姆的那件事 漫步02", "page": "23"}, {"chapter_url": "/m26117/", "full_title": "", "title": "成为史莱姆的那件事 漫步01", "page": "33"}, {"chapter_url": "/m26125/", "full_title": "", "title": "第6卷", "page": "8"}, {"chapter_url": "/m26116/", "full_title": "", "title": "第6卷", "page": "188"}, {"chapter_url": "/m26111/", "full_title": "", "title": "第5卷", "page": "188"}, {"chapter_url": "/m26103/", "full_title": "", "title": "第4卷", "page": "187"}, {"chapter_url": "/m26094/", "full_title": "", "title": "第3卷", "page": "219"}, {"chapter_url": "/m26083/", "full_title": "", "title": "第2卷", "page": "197"}, {"chapter_url": "/m26072/", "full_title": "", "title": "第1卷", "page": "244"}]
    if(sort == "2"):
        return render(request, "detail_sort.html", {"chapter_data": chapter_data})
    elif(sort == "1"):
        chapter_data.reverse()
        return render(request, "detail_sort.html", {"chapter_data": chapter_data})

def pages(request, rowkey, current_page=1):
    data = {
        "rowkey":"207",
        "date":"2021-03-11 21:52:06",
        "title":"关于我转生后成为史莱姆的那件事",
        "description":"普通上班族三上悟（37，童贞）遇刺身亡。迎接他的，是转生后的异世界史莱姆生活……",
        "keyword":"关于我转生后成为史莱姆的那件事,关于我转生后成为史莱姆的那件事漫画,关于我转生后成为史莱姆的那件事漫画免费阅读",
        "chapter":{
            "chapter_url":"/m164936/",
            "page_end_url":"/m164936-end/",
            "cid":"164936",
            "page":"68",
            "title":"第81话",
            "full_title":"试看版",
            "current_page":str(current_page),
        }
    }
    return render(request, "page.html", {"data":data})

def get_img_url_list(request, cid, start_page):
    img_list = [
        'http://image.mangabz.com/1/207/164936/1_5322.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/2_3035.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/3_5048.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/4_6678.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/5_8187.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/6_6670.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/7_3804.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/8_8311.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/9_1749.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/10_5490.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/11_4747.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/12_5247.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/13_9082.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/14_6432.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/15_1764.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/16_6114.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/17_9796.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/18_9744.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/19_2174.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/20_5460.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/21_7013.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/22_1675.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/23_2170.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/24_9326.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/25_6537.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/26_7955.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/27_7558.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/28_6384.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/29_8919.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/30_4799.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/31_1927.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/32_1724.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/33_5252.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/34_8616.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/35_9822.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/36_1085.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/37_3159.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/38_5338.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/39_7327.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/40_5885.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/41_6482.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/42_3267.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/43_2680.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/44_2212.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/45_5757.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/46_2839.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/47_7592.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/48_4844.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/49_5090.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/50_2048.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/51_5681.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/52_7102.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/53_3336.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/54_8654.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/55_9337.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/56_7799.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/57_2668.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/58_3155.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/59_9610.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/60_2561.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/61_3939.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/62_5810.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/63_6400.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/64_6548.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/65_2904.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/66_9453.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/67_3762.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk=', 'http://image.mangabz.com/1/207/164936/68_5432.jpg?cid=164936&key=04dfe8076b3cb2abc92c69f22cc3cf8c&uk='
        ]
    result = {}#先指定一个字典
    mid = request.GET.get('mid')
    cid = request.GET.get('cid')
    _mid = request.GET.get('_mid')
    _cid = request.GET.get('_cid')
    page = int(request.GET.get('page'))
    print(page)
    date = request.GET.get('date')
    sign = request.GET.get('sign')
    key = request.GET.get('key')
    #指定返回数据类型为json且编码为utf-8
    limit = 2
    if(page != len(img_list)):
        result['img_url_list'] = img_list[page-1:page+limit-1]
    else:
        result['img_url_list'] = img_list[page-1:]
    return HttpResponse(json.dumps(result), content_type='application/json;charset=utf-8')

def page_not_found(request, exception):
    return render(request, '404.html', status=404)