from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse
from django.contrib import  messages
from django.db.models import Q
from django.core.paginator import Paginator

from datetime import datetime, timedelta,date
from .models import Advert,Withdraw
from .forms import Adsform
from accounts.models import Account



def home(request):
    return render(request, "users/home.html")


def ads(request):
    objects_list = Advert.objects.filter(active=True)
    paginator = Paginator(objects_list,10)
    page_number = request.GET.get('page')
    obj_list = paginator.get_page(page_number)
    return render(request, "users/ads.html",{"obj_list": obj_list})

def ads_detail(request, pk):
    if request.GET.get('user'):
        q = request.GET.get('user')
        id = request.GET.get('id')
        user = Account.objects.get(ref_code=q,pk=id)
        ip = request.META.get("REMOTE_ADDR")
        if ip == user.ip_address:
            print('yes')
        else:
            av = user.package
            perc = 10 / 100 * av
            user.balance += perc
            user.clicks += 1
            user.save()
            print(perc)
        print(id)
        print(q)
    obj = Advert.objects.get(pk=pk)
    obj.clicks += 1
    obj.save()
    return render(request, "users/ads_detail.html",{"obj":obj})


#advertiser dashboard
@login_required
def ad_dasboard(request):
    if request.user.is_advertiser == False:
        return redirect('pub-dashboard')
    ads = Advert.objects.filter(author=request.user)
    cli = 0
    for p  in ads:
        c = p.clicks
        cli += c
    context = {
        "ads":cli,
        "total_ads":  Advert.objects.filter(author=request.user).count(),
        "running_ads" : Advert.objects.filter(author=request.user,active=True).count(),
    }
    return render(request, "users/adverter/ad_dasboard.html",context)


#my ads
def my_ads(request):
    ads = Advert.objects.filter(author=request.user)
    return render(request,'users/adverter/my_ads.html',{"obj_list":ads})





def get_deadline():
	return datetime.today() + timedelta(days=1)

def amount_to_pay(days):
    if days == 3:
        amount = 2000
    elif days == 7:
        amount = 5000
    else:
        amount = 7000
    return amount

@login_required
def create_ad(request):
    if request.POST:
        form = Adsform(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            d = int(instance.days)
            print(d)
            instance.delete_date = datetime.today() + timedelta(days=d)
            instance.amount_paid = amount_to_pay(d)
            instance.save()
            pk = instance.ref_code
            #messages.success(request, f'Ads created  !')
            return redirect(f'/advertiser/create_ad/checkout/?query={pk}')
    else:
        form = Adsform()
    return render(request, "users/adverter/create_ad.html",{"form":form})

@login_required
def create_ad_checkout(request, **kwargs):
    '''pk = kwargs.get('ads_pk')
    obj = Advert.objects.get(pk=pk)'''
    query = request.GET.get('query')
    try:
        obj = Advert.objects.get(ref_code=query)
    except:
        obj = None
    print(obj.title)
    return render(request, "users/adverter/create_ad_checkout.html",{"obj":obj})


def create_ad_checkout_complete(request,pk):
    if  request.GET.get('status') == 'successful':
        obj = Advert.objects.get(pk=pk)
        obj.active = True
        obj.save()
    return render(request, "users/adverter/create_ad_checkout_complete.html")



#publisher dashboard
@login_required
def pub_dasboard(request):
    user = request.user
    if user.is_advertiser:
        return redirect('ad-dashboard')
    if request.GET.get('a'):
        am = int(request.GET.get('a'))
        if am == 5:
            price = 5000
        elif am == 2:
            price = 2000
        else:
            price = 10000
        user = request.user
        user.package = price
        user.save()
        return redirect('pub-dashboard')
    return render(request, "users/publisher/pub_dasboard.html")






#delete ads
def delete_ads(request):
    ads_id = request.POST.get('ads_id')
    try:
        obj = Advert.objects.get(pk=ads_id)
    except:
        obj = None
    if obj.active == True:
        obj.active = False
        obj.save()
        return JsonResponse({"data":'done'})
    else:
        return JsonResponse({"data":'none'})



#withdraw
@login_required
def withdraw(request):
    if request.POST:
        user = request.user
        acc_name = request.POST.get('acc_name')
        acc_num = request.POST.get('acc_num')
        bank = request.POST.get('bank')
        amount = int(request.POST.get('amount'))
        if amount < 5000:
            messages.success(request, f'minimum withdrawal is 5000!')
            return redirect('pub-withdraw')
        if user.balance > amount:
            Withdraw.objects.create(
                amount=amount,
                user=user,
                bank= bank,
                acc_name = acc_name,
                acc_num = acc_num
            )
            user.balance -= amount
            user.save()
            messages.success(request, f'Withdraw placed !')
            return redirect(f'pub-withdraw')
        else:
            messages.success(request, f'Insufficient funds!')
            return redirect('pub-withdraw')
    else:
        return render(request, "users/publisher/withdraw.html")


#subcribe
@login_required
def subcribe(request):
    if  request.POST:
        am = request.POST.get('am')
        user = request.user
        user.package = am
        user.save()
        return JsonResponse({"user":"done"})
    else:
        return render(request, "users/publisher/subscribe.html")




#withdraw history
@login_required
def with_history(request):
    user  = request.user
    withdraws = Withdraw.objects.filter(user=user)
    return  render(request,'users/publisher/with_history.html',{"objects":withdraws})