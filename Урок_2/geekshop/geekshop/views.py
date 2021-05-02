from django.shortcuts import render

def main(request):
    context = {
        'slogan': 'Мега-удобные стулья',
        'topic': 'Тренды'
    }


    return render(request, 'index.html', context=context)

def contact(request):
    return render(request, 'contact.html')