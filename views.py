# I have created this file
from django.http import  HttpResponse
from django.shortcuts import render
#simple code
# def index(request):
#     return HttpResponse(''' <h1>Youtube</h1>
#                         <a href = "https://www.youtube.com/"> Youtube link </a>''')
    
# def about(request):
#     return HttpResponse(''' <h1>Instagram</h1>
#                         <a href = "https://www.instagram.com/?hl=en"> IG link </a>''')
# def FB(request):
#     return HttpResponse(''' <h1 style ="color:red;background-color:yellow
#                         ">Facebook</h1>
#                         <a href = "https://www.facebook.com/"> FB link </a>''')
  
  
    
# def index(request):
#     return HttpResponse(''' <h1>Home</h1>
#                             <button> <a href = "/removepunc">RemovePUNC</a></button>
#                             <button><a href = "/capitalizefirst">CAPFirst</a></button>
                            
#                         ''')
    
# def  removepunc(request):
#     return HttpResponse(''' <h1>remove punc</h1>
#                             <button><a href = "http://127.0.0.1:8000/">Home</a></button>
#                             <button><a href = "/capitalizefirst">CAPFirst</a></button>''')


# def  capfirst(request):
#     return HttpResponse(''' <h1>capitalize first</h1>
#                             <button><a href = "http://127.0.0.1:8000/">Home</a></button>
#                             <button> <a href = "/removepunc">RemovePUNC</a></button>''')




def index(request):
    return render(request, 'index.html')
def analyze(request):
    # Get the text
    texts = request.POST.get('texts', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    # Check which checkbox is on
    # analyzed = texts
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in texts:
            if char not in punctuations:
                analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        texts = analyzed
        # return render(request, 'analyze.html', params)
    
    if(fullcap == 'on'):
        analyzed = ""
        for char in texts:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Change to Capitals', 'analyzed_text': analyzed}
        texts = analyzed
        # return render(request, 'analyze.html', params)
        
    if(newlineremove == 'on'):
        analyzed = ""
        for char in texts:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        print(params)
        texts = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)
    if(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(texts):
            if not(texts[index] == " " and texts[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'remove spaces', 'analyzed_text': analyzed}
        # Analyze the text

    if(removepunc!='on' and  newlineremove!='on' and fullcap!='on' and spaceremover!='on'):
            return HttpResponse("Plese Select any options")


    return render(request, 'analyze.html', params)
