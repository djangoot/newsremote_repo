from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsAPP/index.html')

def moviesinfo(request):
    head_msg='Latest movies information'
    msg1='Radhey,Titanic,KGF-2'
    msg2='slaman going to marry'
    msg3='modi wants acts in movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsAPP/news.html',context=my_dict)

def sportsinfo(request):
    head_msg='Latest Sports information'
    msg1='cricket'
    msg2='footbal'
    msg3='kabadi'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsAPP/news.html',context=my_dict)


def politicsinfo(request):
    head_msg='Latest politics information'
    msg1='oxgen suppy is very low'
    msg2='acche din aa gya'
    msg3='modi visit west bengal'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return render(request,'newsAPP/news.html',context=my_dict)
