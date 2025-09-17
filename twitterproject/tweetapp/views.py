from django.shortcuts import render
from .models import Tweet,comment,Profile
from .forms import TweetForm,UserRegistrationForm,CommentForm,ProfileForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
from django.contrib.auth.models import User 




# Create your views here.
def home(request):
    return render(request,'home.html')

def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets':tweets})


@login_required
def create_tweet(request):
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form':form})


@login_required
def edit_tweet(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk,user=request.user)
    if request.method=='POST':
        form=TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})


@login_required
def delete_tweet(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request,'tweet_delete.html',{'tweet':tweet})


def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')   
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

    
def search_bar(request):
    query=request.GET.get('q')  
    user_results=[]
    tweet_results=[]

    if query:
        user_results = User.objects.filter(username__icontains=query)
        tweet_results = Tweet.objects.filter(text__icontains=query)

    return render(request, "search_results.html", {"query": query,"user_results": user_results,"tweet_results": tweet_results})


@login_required
def like_tweet(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk)
    if request.user in tweet.likes.all():       #unlike
        tweet.likes.remove(request.user)        
    else:
        tweet.likes.add(request.user)           #like
    return redirect('tweet_list')

@login_required
def add_comment(request,pk):
    tweet=get_object_or_404(Tweet,pk=pk)
    comments = tweet.comment.all()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.tweet=tweet
            comment.user=request.user
            comment.save()
            return redirect('add_comment',pk=pk)
    else:
        form=CommentForm()
    return render(request,'tweet_comment.html',{'form':form,'tweet':tweet,'comments':comments})
        


@login_required
def profile_view(request,username):
    user=get_object_or_404(User,username=username)
    profile, created = Profile.objects.get_or_create(user=user)  # ensures profile exists
    # profile=user.profile                            #user.profile gives us that profile object (with extra fields like bio, picture, etc.).
    tweets=user.tweet_set.all().order_by('-created_at')                       #user.tweet_set.all() → fetches all tweets written by that user.
    return render(request,'profile.html',{'profile':profile,'tweets':tweets})




def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)  # get Profile object for logged-in user
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)  
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'form': form})

