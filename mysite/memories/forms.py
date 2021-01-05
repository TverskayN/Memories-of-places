from django import forms


class AddMemoryForm(forms.Form):
    geo_point = forms.CharField(label='Координаты места',
                                max_length=30,
                                widget=forms.TextInput(attrs={'id': "point",
                                                              'class': "form-control",
                                                              'readonly': '',
                                                              'title': "Выбирите место на карте"}))
    location_name = forms.CharField(label='Название',
                                    max_length=255,
                                    widget=forms.TextInput(attrs={'class': "form-control"}))
    comment = forms.CharField(label='Описание',
                              widget=forms.Textarea(attrs={'class': "form-control"}))

