from django.shortcuts import redirect, render
from .forms import GameForm
from .models import Game

'''
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import GameForm
from .models import Game


class GameListView(ListView):
    model = Game
    context_object_name = 'all_the_games'  # Default: object_list
    template_name = 'game-list.html'  # Default: game_list.html


class GameDetailView(DetailView):
    model = Game
    context_object_name = 'that_one_game'  # Default: game
    template_name = 'game-detail.html'  # Default: game_detail.html


class GameDeleteView(DeleteView):
    model = Game
    template_name = 'game-delete.html'
    success_url = reverse_lazy('game-list')


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'game-create.html'  # Default: game_form.html
    success_url = reverse_lazy('game-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
'''


def game_list(request):
    all_the_games_in_my_function_based_view = Game.objects.all()
    # print('I am in game_list')
    # print(all_the_games_in_my_function_based_view)
    context = {'all_the_games': all_the_games_in_my_function_based_view}
    return render(request, 'game-list.html', context)


def game_detail(request, **kwargs):
    # print(kwargs)
    game_id = kwargs['pk']
    print(game_id)
    that_one_game_in_my_function_based_view = Game.objects.get(id=game_id)
    # print(str(game_id), " :: ", that_one_game_in_my_function_based_view)
    context = {'that_one_game': that_one_game_in_my_function_based_view}
    return render(request, 'game-detail.html', context)


def game_delete(request, **kwargs):
    print("test")
    game_id = kwargs['pk']
    print("test2")
    obj = Game.objects.get(id=game_id)
    context = {'that_one_computer': obj}
    print("test3")
    if request.method == "POST":
        print("test4")
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect('game-list')

    print("test5")
    return render(request, "game-delete.html", context)


def game_create(request):
    if request.method == 'POST':
        # print("I am in POST")
        form_in_my_function_based_view = GameForm(request.POST)
        form_in_my_function_based_view.instance.user = request.user

        if form_in_my_function_based_view.is_valid():
            form_in_my_function_based_view.save()
            # print("I saved new computer")
        else:
            pass
            # print(form_in_my_function_based_view.errors)

        return redirect('game-list')

    else:  # request.method == 'GET'
        # print("I am in GET")
        form_in_my_function_based_view = GameForm()
        context = {'form': form_in_my_function_based_view}
        return render(request, 'game-create-solo.html', context)
