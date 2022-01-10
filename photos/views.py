from django.shortcuts import render,redirect
from .models import Category, Photo

# Create your views here.
def index(request):
    category=request.GET.get('category')
    if category ==None:
        photos=Photo.objects.all()
    else:
        photos=Photo.objects.filter(category__name=category)


    categories=Category.objects.all()
    # print('category:',category)
    
    

    context={'categories':categories, 'photos':photos}
    return render(request, 'photos/index.html',context)

def viewPhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})


def addPhoto(request):
    categories=Category.objects.all()
    if request.method == 'POST':
        data =request.POST
        image=request.FILES.get('image')


        if data['category'] !='none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new'] !='':
            category,creted=Category.objects.get_or_create(name=data['category_new'])
        else:
            category=None

        photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )


        return redirect('index.html')






        # print('data:', data)
        # print('image:',image)



    context={'categories':categories}
    return render(request,'photos/add.html',context)