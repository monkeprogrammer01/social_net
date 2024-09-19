from django.shortcuts import render, redirect
from users.models import User, Post, FriendRequest
from users.views import accept_request
import time


def index(request):

    posts = Post.objects.all()
    context = {
        'posts': posts[::-1],
    }
    return render(request, 'main/news.html', context)


def account_search(request, *args, **kwargs):
    context = {}
    if request.method == "GET":
        search_query = request.GET.get("q")
        if search_query:
            search_results = User.objects.filter(username__icontains=search_query)
            accounts = []
            for account in search_results:
                try:
                    FriendRequest.objects.get(from_user=account, to_user=request.user)
                    accounts.append((account, is_friend(request,account.id), True))   # account, is_friend, was_sent
                except:
                    accounts.append((account, is_friend(request,account.id), False))

            context['accounts'] = accounts

    return render(request, 'main/search.html', context)


def friends(request):
    friend_list = []
    for friend in request.user.friends.all():
        friend_list.append(friend)
    context = {
        'friends': friend_list,
    }
    return render(request, 'main/friend_requests.html', context)


def is_friend(request, friend_id):
    try:
        request.user.friends.get(id=friend_id)
        return True
    except:
        return False
