from django.http import HttpResponse


def home(request):
    mensagem = "<h1>Bem-vindo ao DevBlog!</h1> <p>Em breve, artigos aqui.</p>"

    return HttpResponse(mensagem)

def sobre_nos(request):
    mensagem = "<h1>Sobre o DevBlog!</h1>"

    return HttpResponse(mensagem)