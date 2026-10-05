from ast import iter_fields
from itertools import count
from os import remove

from django.shortcuts import render, redirect
from django.template.defaultfilters import lower

from main.views import data
from select import select
from unicodedata import category

from .forms import SearchForm, EventForm


class Filtered:
    def __init__(self,_data,cat):
        self._data=_data
        self.cat=cat

    def cathegorized(self):
        temp=[]
        for i in self._data:
            if i["category"]==self.cat:
                temp.append(i)

            elif i["status"]==self.cat:
                temp.append(i)

        if len(temp)<1:
            return self._data
        else:
            return temp

    def getall(self):
        return len(self._data)

    def get_ongoing(self):
        event_count=0
        for i in self._data:
            if i["status"]=="ongoing":
                event_count+=1
        return event_count

    def get_cancelled(self):
        event_count=0
        for i in self._data:
            if i["status"]=="cancelled":
                event_count+=1
        return event_count

def events_page(request):
    selected = request.GET.get("category", "")
    filtered=Filtered(data,selected)
    temp=[]

    if request.method=='GET':
        form=SearchForm(request.GET)
        if form.is_valid():
            for i in data:
                if form.cleaned_data['title'].lower() in i["title"].lower() or form.cleaned_data['title'].lower() in i["location"].lower():
                    temp.append(i)

    else:
        form = SearchForm()

    context={
        "variable":filtered,
        "form":form,
        "list":temp,
    }
    return render(request,'events/eventspage.html',context)

def event_page(request,event_id: int):
    selected = request.GET.get("status", "")
    if selected=="cancelled":
        data[event_id-1]["status"]=selected

    context={
        "event":data[event_id-1]
    }

    return render(request,'events/event_detail.html',context)

def delete_page(request,event_id: int):
    confirm=request.GET.get("confirm","")
    if confirm=="true":
        for i in range(event_id-1,len(data)):
            if data[i]["id"]>data[event_id-1]["id"]:
                temp=data[i]["id"]
                data[i]["id"]=data[event_id - 1]["id"]
                data[event_id - 1]["id"]=temp
        del (data[event_id-1])
        return redirect('events')


    context={
        "event":data[event_id-1]
    }

    return render(request, 'events/delete_event.html',context)

def create_page(request):
    form=EventForm()

    if request.method=="POST":
        form=EventForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            data.append({
                "id": max(e["id"] for e in data) + 1,
                "title": cd["title"],
                "description": cd["description"],
                "category": cd["category"],
                "location": cd["location"],
                "status": cd["status"],
            })
            return redirect("events")

    return render(request, 'events/create_event.html', {"form": form})


