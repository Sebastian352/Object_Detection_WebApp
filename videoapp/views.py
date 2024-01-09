from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, "videoapp/index.html")


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


def video_feed(request):
    return StreamingHttpResponse(
        gen(VideoCamera()), content_type="multipart/x-mixed-replace; boundary=frame"
    )


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        else:
            return render(request, "videoapp/signup.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "videoapp/signup.html", {"form": form})


def home(request):
    return render(request, "videoapp/home.html")


def signin(request):
    if request.user.is_authenticated:
        return render(request, "videoapp/home.html")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # profile
        else:
            msg = "Error Login"
            form = AuthenticationForm(request.POST)
            return render(request, "videoapp/login.html", {"form": form, "msg": msg})
    else:
        form = AuthenticationForm()
        return render(request, "videoapp/login.html", {"form": form})


def profile(request):
    return render(request, "videoapp/profile.html")


def signout(request):
    logout(request)
    return redirect("/")
