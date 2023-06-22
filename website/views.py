from django.shortcuts import render, redirect
from django.contrib import messages
import openai
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from .models import Code
# Create your views here.

def home(request):
    #api key: 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
    lang_list = ["html", "markup", "css", "clike", "javascript", "c", "csharp", "cpp", "coffeescript", "django", "go", "java", "markup-templating", "matlab", "mongodb", "objectivec", "perl", "php", "powershell", "python", "r", "regex", "ruby", "rust", "sql", "swift", "typescript", "uri", "xml-doc", "yaml"]
    print(lang_list.sort())
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        #check to make sure a lang picked
        if lang == "Select programming language":
            messages.success(request, "Please pick a language!")
            return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
        else:
            openai.api_key = "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"
            openai.Model.list()
            try:
                response = openai.Completion.create(
                    engine='text-davinci-003',
                    prompt=f"Respond only with code. Fix this {lang} code: {code}",
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    presence_penalty=0.0,
                    frequency_penalty=0.0,
                    )
                response = (response["choices"][0]["text"]).strip()
                return render(request, 'home.html', {'lang_list':lang_list, 'response':response, 'lang':lang})
            except Exception as e:
                print(e)
                return render(request, 'home.html', {'lang_list':lang_list, 'code':e, 'lang':lang})
    return render(request, 'home.html', {'lang_list':lang_list})

def suggest(request):
    lang_list = ["html", "markup", "css", "clike", "javascript", "c", "csharp", "cpp", "coffeescript", "django", "go", "java", "markup-templating", "matlab", "mongodb", "objectivec", "perl", "php", "powershell", "python", "r", "regex", "ruby", "rust", "sql", "swift", "typescript", "uri", "xml-doc", "yaml"]
    print(lang_list.sort())
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        # #check to make sure a lang picked
        # if lang == "Select programming language":
        #     messages.success(request, "Please pick a language!")
        #     return render(request, 'suggest.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
        # else:
        openai.api_key = "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"
        openai.Model.list()
        try:
            response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f"Respond only with code. {code}",
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            presence_penalty=0.0,
            frequency_penalty=0.0,
                )
            response = (response["choices"][0]["text"]).strip()
            return render(request, 'suggest.html', {'lang_list':lang_list, 'response':response, 'lang':lang})
        except Exception as e:
            print(e)
            return render(request, 'suggest.html', {'lang_list':lang_list, 'code':e, 'lang':lang})
    return render(request, 'suggest.html', {'lang_list':lang_list})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect('home')
        else:
            messages.success(request, "error logging in")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registered!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {"form": form})

def past(request):
	if request.user.is_authenticated:
		code = Code.objects.filter(user_id=request.user.id)
		return render(request, 'past.html', {"code":code})	
	else:
		messages.success(request, "You Must Be Logged In To View This Page")
		return redirect('home')


def delete_past(request, Past_id):
	past = Code.objects.get(pk=Past_id)
	past.delete()
	messages.success(request, "Deleted Successfully...")
	return redirect('past')     