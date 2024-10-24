from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from telegram import Bot

# Create your views here.
def index(request):
    return render(request, "index.html")


async def send_notif(request):
    if request.method == "POST":
        mobile = request.POST.get("phone")
        print(mobile)
        bot = Bot(token="7277154564:AAFpwtyjsq6sppLPQV4ws9uccCybSvoSAHs")
        await bot.send_message(chat_id=-1002277461198, text=mobile)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
