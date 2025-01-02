from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label="Select an author",
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'
            })
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'date_posted', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm'
                }),
            'content': forms.Textarea(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm h-32'
                }),
            'date_posted': forms.DateTimeInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm',
                'type': 'datetime-local'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-500'
            })
        }