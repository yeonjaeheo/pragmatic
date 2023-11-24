from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        ## post 방식으로 보낸 입력값을 temp 변수를 만들어서 return 해낸다.
        temp = request.POST.get('hello_world_input')
        ## 입력값을 model 에 저장한다.
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()

        ## accountapp 에 있는 hello_world 로 재접속해라!
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list })