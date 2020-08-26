from django.shortcuts import render, redirect
from paginas import services
from django.contrib import messages
# from paginas import database


def index(request):
    return render(request, 'paginas/index.html')


def cliente(request):
    name = request.POST.get('name')
    document = request.POST.get('document')
    status = services.insert_cliente(name, document)
    print(f'status-> {status}')
    if int(status) == 201:
        messages.add_message(request, messages.SUCCESS, 'Funcionario cadastrado com sucesso')
        return redirect("cliente")

    return render(request, 'paginas/cliente.html')


def produto(request):
    product = request.POST.get('product')
    description = request.POST.get('description')
    cost = request.POST.get('cost')
    status = services.insert_produto(product, description, cost)
    print(f'status -> {status}')
    if int(status) == 201:
        messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso')
        return redirect("produto")

    return render(request, 'paginas/produto.html')

note = services.insert_note("19","2020-08-26")
print(note)

def nota(request):
    user = request.POST.get('user')
    date = request.POST.get('date')
    if not user or not date:
        messages.add_message(request, messages.SUCCESS, 'Preencha os campos!')
    else:
        note = services.insert_note(user, date)
        sessao = request.session['nota'] = note['id']
        user_sessao = request.session['user'] = note['user']
        date_sessao = request.session['date'] = note['date']
        messages.add_message(request, messages.SUCCESS, 'Nota cadastrada, inicie a venda!')
        return redirect("listaproduto")
    return render(request, 'paginas/nota.html')


def lista_user(request):
    lista = {'user': services.get_user()}
    return render(request, 'paginas/nota.html', lista['user'])


def lista_note(request):
    note = {'note': services.get_note()}
    return render(request, 'paginas/index.html', note['note'])


def lista(request):
    lista = {'product': services.get_item()}
    return render(request, 'paginas/listaproduto.html', lista['product'])



def listanota(request):
    note = request.session['nota']
    lista = {'note': services.list(note)}
    return render(request, 'paginas/listanota.html', lista['note'])


def updatenote(request):
    id = request.session['nota']
    user = request.sessio['user']
    print(f'sessao do usuario {user}')
    date = request.session['date']
    print(f'sessao da data {date}')
    total_cost = request.PUT.get('total_cost')

    if not user or not date or not total_cost:
        messages.add_message(request, messages.SUCCESS, 'Não foi encontrado dados da nota!')
    else:
        status = services.update_note(id, user, total_cost, date)
        messages.add_message(request, messages.SUCCESS, 'Venda finalizada ;)!')
        return redirect("index")
    return render(request, 'paginas/listanota.html')

def rota(request):
    note = request.session['nota']
    print(f'sessaooooo aqui --> {note}')
    item = request.POST.get('item')
    cost = request.POST.get('cost')
    amount = request.POST.get('amount')
    valor = float(cost) * int(amount)

    status = services.insert_noteitem(note, item, valor, amount)
    if int(status) == 201:
        messages.add_message(request, messages.SUCCESS, 'Produto adicionado ao carrinho!')
        return redirect("listaproduto")
    return render(request, 'paginas/listaproduto.html')
