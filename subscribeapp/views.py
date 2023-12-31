from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView
from articleapp.models import Article
from projectapp.models import Project

from subscribeapp.models import Subscription



@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
    
    
    def get(self, request, *args, **kwargs):
        
        # 이 아래부터는 프로젝트랑 유저 정보 취합 작업!!
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, 
                                                   project=project)
        
        # 있으먄 지우고 없으면 만들고
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)
    
    
    
@method_decorator(login_required,'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5


    #def_queryset 을 통해 가지고 오는 게시물들에 조건을 추가해 커스터마이징 할 수 있다.
    def get_queryset(self):
        projects = Subscription.objects.filter(user = self.request.user).values_list('project')
        # __in은 필드 리스트인 projects 값들을 Article model의 project에서 일치하는 값들을 골라낸다
        article_list = Article.objects.filter(project__in=projects)
        return article_list