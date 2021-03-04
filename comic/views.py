from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    # api_request = requests.get("https://api.github.com/users?since=135")
    # api = json.loads(api_request.content)
    # return render(request, "home.html", {"api": api})
    return render(request, "home.html")

def detail(request, rowkey):
    return render(request, "detail.html")

def chapter(request, rowkey, sort):
    chapter_data = [{'html_url': '/m164936/', 'full_title': '试看版', 'title': '第81话', 'page': '68'}, {'html_url': '/m160758/', 'full_title': '试看版', 'title': '第80话', 'page': '32'}, {'html_url': '/m162658/', 'full_title': '试看版', 'title': '第79话', 'page': '20'}, {'html_url': '/m155712/', 'full_title': '试看版', 'title': '第78话', 'page': '40'}, {'html_url': '/m150977/', 'full_title': '试看版', 'title': '第77话', 'page': '44'}, {'html_url': '/m146975/', 'full_title': '试看版', 'title': '第76话', 'page': '32'}, {'html_url': '/m143158/', 'full_title': '试看版', 'title': '第75话', 'page': '41'}, {'html_url': '/m138261/', 'full_title': '试看', 'title': '第74话', 'page': '60'}, {'html_url': '/m132309/', 'full_title': '试看版', 'title': '第73话', 'page': '40'}, {'html_url': '/m127243/', 'full_title': '试看版', 'title': '第72话', 'page': '34'}, {'html_url': '/m122073/', 'full_title': '试看版', 'title': '第71话', 'page': '38'}, {'html_url': '/m116555/', 'full_title': '试看版', 'title': '第70话', 'page': '42'}, {'html_url': '/m113113/', 'full_title': '特恩佩斯特复活祭', 'title': '第69话', 'page': '40'}, {'html_url': '/m108971/', 'full_title': '', 'title': '第68话', 'page': '46'}, {'html_url': '/m108970/', 'full_title': '', 'title': '第67话', 'page': '44'}, {'html_url': '/m108969/', 'full_title': '', 'title': '第66话', 'page': '30'}, {'html_url': '/m108968/', 'full_title': '', 'title': '第65话', 'page': '40'}, {'html_url': '/m108967/', 'full_title': '', 'title': '第64话', 'page': '48'}, {'html_url': '/m82699/', 'full_title': '逆袭时刻', 'title': '第63话', 'page': '27'}, {'html_url': '/m82698/', 'full_title': '是魔物也是人类', 'title': '第62话', 'page': '19'}, {'html_url': '/m82697/', 'full_title': '魔女的处罚', 'title': '第61话', 'page': '33'}, {'html_url': '/m82696/', 'full_title': '希望的条件', 'title': '第60话', 'page': '26'}, {'html_url': '/m82695/', 'full_title': '绝望与希望', 'title': '第59话', 'page': '55'}, {'html_url': '/m82694/', 'full_title': '灾祸', 'title': '第58话', 'page': '32'}, {'html_url': '/m82693/', 'full_title': '带来灾祸的来访者', 'title': '第57话', 'page': '26'}, {'html_url': '/m82692/', 'full_title': '各自的盘算', 'title': '第56话', 'page': '26'}, {'html_url': '/m82691/', 'full_title': '魔物的天敌', 'title': '第55话', 'page': '32'}, {'html_url': '/m26105/', 'full_title': '', 'title': '第54话', 'page': '20'}, {'html_url': '/m26104/', 'full_title': '', 'title': '第53话', 'page': '22'}, {'html_url': '/m15777/', 'full_title': '', 'title': '第52话', 'page': '44'}, {'html_url': '/m15776/', 'full_title': '', 'title': '第51话', 'page': '24'}, {'html_url': '/m15775/', 'full_title': '', 'title': '第50话', 'page': '29'}, {'html_url': '/m15774/', 'full_title': '', 'title': '第49话', 'page': '21'}, {'html_url': '/m15772/', 'full_title': '', 'title': '第48话', 'page': '27'}, {'html_url': '/m26102/', 'full_title': '', 'title': '第47话', 'page': '38'}, {'html_url': '/m26101/', 'full_title': '', 'title': '第46话', 'page': '51'}, {'html_url': '/m26100/', 'full_title': '', 'title': '第45话', 'page': '21'}, {'html_url': '/m26099/', 'full_title': '', 'title': '第44话', 'page': '35'}, {'html_url': '/m26098/', 'full_title': '', 'title': '第43话', 'page': '31'}, {'html_url': '/m26097/', 'full_title': '', 'title': '第42话', 'page': '23'}, {'html_url': '/m26096/', 'full_title': '', 'title': '第41话', 'page': '33'}, {'html_url': '/m26095/', 'full_title': '', 'title': '第40话', 'page': '55'}, {'html_url': '/m26093/', 'full_title': '', 'title': '第39话', 'page': '36'}, {'html_url': '/m26092/', 'full_title': '', 'title': '第38话', 'page': '53'}, {'html_url': '/m26091/', 'full_title': '', 'title': '第37话', 'page': '26'}, {'html_url': '/m26090/', 'full_title': '', 'title': '第36话', 'page': '27'}, {'html_url': '/m26089/', 'full_title': '', 'title': '第35话', 'page': '35'}, {'html_url': '/m26088/', 'full_title': '', 'title': '第34话', 'page': '47'}, {'html_url': '/m26087/', 'full_title': '', 'title': '第33话', 'page': '23'}, {'html_url': '/m26086/', 'full_title': '', 'title': '第32话', 'page': '31'}, {'html_url': '/m26085/', 'full_title': '', 'title': '第31话', 'page': '31'}, {'html_url': '/m26084/', 'full_title': '', 'title': '第30话', 'page': '25'}, {'html_url': '/m26082/', 'full_title': '', 'title': '第29话', 'page': '35'}, {'html_url': '/m26081/', 'full_title': '', 'title': '第28话', 'page': '56'}, {'html_url': '/m26080/', 'full_title': '', 'title': '第27话', 'page': '31'}, {'html_url': '/m26079/', 'full_title': '', 'title': '第26话', 'page': '27'}, {'html_url': '/m26078/', 'full_title': '', 'title': '第25话', 'page': '33'}, {'html_url': '/m26077/', 'full_title': '', 'title': '第24话', 'page': '28'}, {'html_url': '/m26076/', 'full_title': '', 'title': '第23话', 'page': '29'}, {'html_url': '/m26075/', 'full_title': '', 'title': '第22话', 'page': '32'}, {'html_url': '/m26074/', 'full_title': '', 'title': '第21话', 'page': '31'}, {'html_url': '/m26073/', 'full_title': '', 'title': '第20话', 'page': '32'}, {'html_url': '/m26071/', 'full_title': '', 'title': '第19话', 'page': '28'}, {'html_url': '/m26070/', 'full_title': '', 'title': '第18话', 'page': '29'}, {'html_url': '/m26069/', 'full_title': '', 'title': '第17话', 'page': '34'}, {'html_url': '/m26068/', 'full_title': '', 'title': '第16话', 'page': '29'}, {'html_url': '/m26067/', 'full_title': '', 'title': '第15话', 'page': '29'}, {'html_url': '/m26066/', 'full_title': '', 'title': '第14话', 'page': '28'}, {'html_url': '/m26065/', 'full_title': '', 'title': '第13话', 'page': '33'}, {'html_url': '/m26064/', 'full_title': '', 'title': '第12话', 'page': '32'}, {'html_url': '/m26063/', 'full_title': '', 'title': '第11话', 'page': '30'}, {'html_url': '/m26062/', 'full_title': '', 'title': '第10话', 'page': '34'}, {'html_url': '/m26061/', 'full_title': '', 'title': '第9话', 'page': '31'}, {'html_url': '/m26060/', 'full_title': '', 'title': '第8话', 'page': '31'}, {'html_url': '/m26059/', 'full_title': '', 'title': '第7话', 'page': '30'}, {'html_url': '/m26058/', 'full_title': '', 'title': '第6话', 'page': '26'}, {'html_url': '/m26057/', 'full_title': '', 'title': '第5话', 'page': '29'}, {'html_url': '/m26056/', 'full_title': '', 'title': '第4话', 'page': '28'}, {'html_url': '/m26055/', 'full_title': '', 'title': '第3话', 'page': '33'}, {'html_url': '/m26054/', 'full_title': '', 'title': '第2话', 'page': '37'}, {'html_url': '/m26053/', 'full_title': '', 'title': '第1话', 'page': '48'}, {'html_url': '/m26124/', 'full_title': '', 'title': '成为史莱姆的那件事 现场录音', 'page': '5'}, {'html_url': '/m26123/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步08', 'page': '21'}, {'html_url': '/m26122/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步07', 'page': '10'}, {'html_url': '/m26121/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步06', 'page': '21'}, {'html_url': '/m26120/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步05', 'page': '19'}, {'html_url': '/m26119/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步03', 'page': '23'}, {'html_url': '/m26118/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步02', 'page': '23'}, {'html_url': '/m26117/', 'full_title': '', 'title': '成为史莱姆的那件事 漫步01', 'page': '33'}, {'html_url': '/m26125/', 'full_title': '', 'title': '第6卷', 'page': '8'}, {'html_url': '/m26116/', 'full_title': '', 'title': '第6卷', 'page': '188'}, {'html_url': '/m26111/', 'full_title': '', 'title': '第5卷', 'page': '188'}, {'html_url': '/m26103/', 'full_title': '', 'title': '第4卷', 'page': '187'}, {'html_url': '/m26094/', 'full_title': '', 'title': '第3卷', 'page': '219'}, {'html_url': '/m26083/', 'full_title': '', 'title': '第2卷', 'page': '197'}, {'html_url': '/m26072/', 'full_title': '', 'title': '第1卷', 'page': '244'}]
    if(sort == 2):
        return render(request, "detail_sort.html", {"chapter_data": chapter_data})
    elif(sort == 1):
        return render(request, "detail_sort.html", {"chapter_data": chapter_data.reverse})
