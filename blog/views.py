from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, FormView
from blog.forms import NewsForm, UserRegisterForm, EditNewsForm
from django.contrib.auth import login
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from datetime import datetime

from blog.models import News, Category

User = get_user_model()

def index(request):
    news = News.objects.all()

    paginator = Paginator(news, 3)
    page_number = request.GET.get("page")
    news = paginator.get_page(page_number)
    return render(request, "main/index.html", {"news": news})


class ViewNews(DetailView):
    model = News
    context_object_name = 'item'
    #  pk_url_kwarg = 'news_id'
    template_name = 'main/view_news.html'



class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'main/add_news.html'
    success_url = reverse_lazy('home')
    # login_url = '/admin/'
    raise_exception = True

   # добавляет в поле автор id текущего юзера автоматически
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        print(form.instance.author_id)
        return super(CreateNews, self).form_valid(form)




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('home')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register_user.html', {"form": form})

# def add_news(request):
#     #  cоздал экземпляр 'active_user' класса Cart с активным пользователем
#     #  обратился к id экземпляра  Cart при добавлении в БД
#     active_user = request.user.id
#     print(active_user)
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             news = News.objects.create(**form.cleaned_data, author_id=active_user)
#             return redirect('home')
#     else:
#         form = NewsForm()
#     return render(request, 'main/add_news.html', {'form': form})


#  профиль пользователя
def profile(request):
    my_movie = News.objects.all().filter(author_id=request.user.pk).order_by('-updated_at')
    #print(request.user.pk)
    paginator = Paginator(my_movie, 4)
    page_number = request.GET.get("page")
    my_news = paginator.get_page(page_number)
    return render(request, './main/profile.html', {'my_news': my_news})


#  фильтр фильмов по жанру
def choise_category(request, name):
    category = Category.objects.get(title=name)
    print(category.pk)
    news = News.objects.filter(category_id=category.pk)
    num_news = news.count()
    print(num_news)
    paginator = Paginator(news, 3)
    page_number = request.GET.get("page")
    news = paginator.get_page(page_number)
    return render(request, 'main/category_news.html', { 'name': name, 'news': news, 'num_news': num_news})


def delete_news(request, news_pk):
    #active_user = News.objects.get(author_id=request.user.pk)
    News.objects.get(author_id=request.user.pk, id=news_pk).delete()
    print(news_pk)
    print(request.user.pk)
    return redirect('profile')



#  редактирование коментария
def edit_news(request, news_pk):
    #  cоздал экземпляр 'active_user' класса Cart с активным пользователем
    #  обратился к id экземпляра  Cart при добавлении в БД
    #  active_user = News.objects.get(author_id=request.user.pk)
    if request.method == 'POST':
        form = EditNewsForm(request.POST)
        if form.is_valid():
            News.objects.filter(author_id=request.user.pk, id=news_pk).update(**form.cleaned_data, updated_at=datetime.today())
            return redirect('profile')
            pass
    else:
        form = EditNewsForm()
    news = News.objects.filter(author_id=request.user.pk, id=news_pk)
    return render(request, 'main/edit_news.html', {'news': news, 'form': form})

