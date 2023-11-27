from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from accountapp.forms import AccountUpdateForm

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "post":
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
    



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'
    
    
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    
    
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'