from django.shortcuts import render
import random
# Create your views here.

# View 함수의 첫번째 파라미터는 무조건 request
# url로 부터 받아온 요청이다.
def index(request):

    # 하나의 문서를 보여준다.
    # render 함수로 template을 보여준다.
    #render 함수의 첫번째 인자도 무조건 request, 두번째 인자는 Template의 경로
    
    return render(request, "index.html") 

def greeting(request):

    # Context(변수)는 3번째 인자로 들어간다.
    foods = ['apple', 'banana', 'coconut',]
    
    info = {
        'name': 'Harry',
    }

    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, "greeting.html", context)

def dinner(request):

    foods = ["족발", "피자", "햄버거", "학식",]
    pick = random.choice(foods)

    context = {
        'pick': pick,
        'foods': foods,
    }

    return render(request, "dinner.html", context)