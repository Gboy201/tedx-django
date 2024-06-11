from django.shortcuts import render, redirect
from .models import sponsorRequests, teamMember, sponsorList, speaker


# Create your views here.
def home(request):
    bronze = sponsorList.objects.filter(tier='Bronze')
    silver = sponsorList.objects.filter(tier='Silver')
    gold = sponsorList.objects.filter(tier='Gold')
    platinum = sponsorList.objects.filter(tier='Platinum')
    print(platinum)
    context={'bronze': bronze, 'silver': silver, 'gold': gold, 'platinum': platinum}
    return render(request, "main/home.html", context)

def sponsor(request):
    return render(request, "main/sponsor.html")

def submit (request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        organization = request.POST['organization']
        tier = request.POST['level']
        message = request.POST['message']
        print(name,email,organization,tier,message)
        sponsorRequest = sponsorRequests(name=name, email=email, organization=organization, tier=tier, message=message)
        sponsorRequest.save()
        return render(request, 'main/submit.html')
    else:
        return redirect("home")

def team(request):
    teamMembers = teamMember.objects.all().values()
    context = {'teamMembers': teamMembers}
    return render(request, 'main/team.html', context)

def speakerShow(request):
    speakers = speaker.objects.all().values()
    context = {'speakers': speakers}
    return render(request, 'main/speaker.html', context)