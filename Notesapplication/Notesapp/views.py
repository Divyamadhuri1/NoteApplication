from django.shortcuts import render
from Notesapp.models import Notes
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from mongoengine import *
connect('notesapp',host='127.0.0.1',port=27017)

def index(request):
    print("Hello, world. Welcome to Notes Application")
    context= {"response":"hi"}
    return render(request, 'index.html', context)

@csrf_exempt
def addnote(request):
    print("we will add the note here")
    entity_Lastmodified = datetime.now()
    notehead = request.POST['notehead']
    note = request.POST['note']
    data_res = Notes.objects.filter(note_heading=notehead)
    if data_res:
        print("already added")
        return HttpResponse('Note already added')
    else:
        data = Notes(note_heading=notehead,note=note,note_time=entity_Lastmodified)
        result = data.save()
        print(result)
        return HttpResponse('Note added successfully')

@csrf_exempt
def updatenote(request):
    print("we will update the existing note here")
    return HttpResponse('Note updated successfully')

@csrf_exempt
def deletenote(request):
    print("we will delete the given note here")
    delete_status = Notes.objects(note_heading=request['note_heading']).delete()
    if delete_status:
        return HttpResponse('Note deleted successfully')
    else:
        return HttpResponse('Failed to delete')

@csrf_exempt
def getallnotes(request):
    print("we will return all the existing notes")
    result = Notes.objects.filter()
    noteslist=[]
    for note in result:
        notedict={"noteheading":note.note_heading,"note":note.note,"note_time":note.note_time}
        noteslist.append(notedict)
    return HttpResponse(noteslist)
    #return render(request, 'index.html', context)