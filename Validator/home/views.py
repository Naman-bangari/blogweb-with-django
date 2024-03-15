from django.shortcuts import render ,HttpResponse,redirect

# Create your views here.
def index(request):
    items = request.session.get('items', []) 
    code1 = request.session.get('code1', None)  # Retrieve code1 from session or None if not found

    if request.method == 'POST':
        new_code1 = request.POST.get('code')
        if new_code1 is not None:  # Check if new_code1 is not None
            request.session['code1'] = new_code1  # Store new_code1 in session
            code1 = new_code1
    return render(request, 'index.html', {'code1': code1,'items':items})

def full_review(request):
    code1 = request.session.get('code1')  # Retrieve code1 from session
    return render(request, 'full_review.html', {'code1': code1})
  
def services(request):
    return render(request,'services.html')
def auto_code(request):
    return render(request,'auto_code.html')

def about_us(request):
    return render(request,'about_us.html') 
def contact(request):
    return render(request,'contact.html')
def home1(request):
    if request.method == 'POST':
        items = []  # Initialize an empty list
        selected_items = [value for name, value in request.POST.items() if name.startswith('item')]
        items.extend(selected_items)
        request.session['items'] = items
        return redirect('index')  # Assuming 'index' is the name of the URL pattern for the index view

    return render(request, 'home1.html')

  