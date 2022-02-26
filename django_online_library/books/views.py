from django.shortcuts import render, redirect

from django_online_library.books.models import Profile, Book
from django import forms


def has_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDelete(forms.ModelForm):
    def save(self, commit=True):

        Book.objects.all().delete()
        self.instance.delete()

    class Meta:
        model = Profile
        fields = ()



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class EditBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


def home_page(request):
    prof = has_profile()
    have_books = Book.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileForm()

    context = {
        'books': have_books,
        'form': form,
        'show_nav': True,

        'profile': prof
    }
    if prof:
        return render(request, 'home-with-profile.html', context)

    return render(request, 'home-no-profile.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = BookForm()

    context = {
        'form_book': form
    }
    return render(request, 'add-book.html', context)


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book_edit = EditBook(request.POST, instance=book)
        if book_edit.is_valid():
            book_edit.save()
            return redirect('home page')
    else:
        book_edit = EditBook(instance=book)
    context = {
        'book': book,
        'edit_book': book_edit
    }
    return render(request, 'edit-book.html', context)


def book_details_page(request, id):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)


def profile(request):
    prof = has_profile()
    has_image = Profile.image_url
    context = {
        'profile': prof,
        'images': has_image
    }
    return render(request, 'profile.html', context)


def profile_edit(request):
    # profile = Profile.objects.get(id=1)
    profile_to_edit = has_profile()
    if request.method == 'POST':
        prof = ProfileEdit(request.POST, instance=profile_to_edit)
        if prof.is_valid():
            prof.save()
            return redirect('home page')
    else:
        prof = ProfileEdit(instance=profile_to_edit)
    context = {
        'prof': profile_to_edit,
        'edit_prof': prof
    }
    return render(request, 'edit-profile.html', context)

    # return render(request, 'edit-profile.html')


def profile_delete(request):
    profile_to_delete = has_profile()
    if request.method == 'POST':
        prof = ProfileDelete(request.POST, instance=profile_to_delete)
        if prof.is_valid():
            prof.save()
            return redirect('home page')
    else:
        prof = ProfileDelete(instance=profile_to_delete)
    context = {
        'prof': profile_to_delete,
        'delete_prof': prof
    }

    return render(request, 'delete-profile.html', context)
