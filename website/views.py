from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def home(request):
    lang_list = ["html", "markup", "css", "clike", "javascript", "c", "csharp", "cpp", "coffeescript", "django", "go", "java", "markup-templating", "matlab", "mongodb", "objectivec", "perl", "php", "powershell", "python", "r", "regex", "ruby", "rust", "sql", "swift", "typescript", "uri", "xml-doc", "yaml"]
    print(lang_list.sort())
    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']
        #check to make sure a lang picked
        if lang == "Select programming language":
            messages.success(request, "Please pick a language!")
            return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
            
            
        
        return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
    return render(request, 'home.html', {'lang_list':lang_list})