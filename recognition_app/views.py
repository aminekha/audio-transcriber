from django.shortcuts import render
from .forms import UploadFileForm
from .src.audio_transcribe import transcribe

def index(request):
    template_name = "index.html"
    transcribed_text = ""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            transcribed_text = transcribe(request.FILES['file'])
            print("Transcription ----> ", transcribed_text)
    else:
        form = UploadFileForm()
        
    context = {
        "form": form,
        "transcription": transcribed_text,
    }
    return render(request, template_name, context)