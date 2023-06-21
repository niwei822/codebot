from django.shortcuts import render
from django.contrib import messages
import openai
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
        #check to make sure a lang picked
        if lang == "Select programming language":
            messages.success(request, "Please pick a language!")
            return render(request, 'suggest.html', {'lang_list':lang_list, 'code':code, 'lang':lang})
        else:
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