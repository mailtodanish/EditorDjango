from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import subprocess

# Create your views here.
def home_page(request):
     return render(request, "python_editor/home_page.html")

def run(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate() 
    return proc.returncode, stdout, stderr

def result(request):
    s = request.POST['script']
    with open(settings.STATIC_ROOT+"/" + "temp.py", 'w') as f:
             f.write(s)
             f.close()
    _, out, err = run(['python', settings.STATIC_ROOT+"/" + "temp.py"])           
    data = {'output': "{0} {1}".format(out.decode('utf-8'), err.decode('utf-8').split('temp.py",')[1] if err.decode('utf-8') != '' else '')}           
    return JsonResponse(data)
    