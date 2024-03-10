from django.shortcuts import render ,HttpResponse,redirect

# Create your views here.
def index(request):
    code1 = request.session.get('code1', None)  # Retrieve code1 from session or None if not found
    if request.method == 'GET':
        new_code1 = request.GET.get('code')
        if new_code1 is not None:  # Check if new_code1 is not None
            request.session['code1'] = new_code1  # Store new_code1 in session
            code1 = new_code1
        #print("code1:", code1)
    return render(request, 'index.html', {'code1': code1})
def about(request):
    code1 = request.session.get('code1')  # Retrieve code1 from session
    return render(request, 'about.html', {'code1': code1})
  
def services(request):
     return render(request,'services.html')
 
def contact(request):
     return render(request,'contact.html')
  