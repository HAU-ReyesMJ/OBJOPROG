from django import forms


from .models import Chatbox


class ChatboxForm(forms.ModelForm):
    class Meta:
        model = Chatbox
        fields = [
            # 'title',
            # 'description',
            # 'price',
            # 'name',
            'recepient',
            'messages',
            'date',
            'messageType',
        ]