from django import forms


class RenderableFormMixin:
    """
    A mixin that can be applied to Django 4 forms to get them to render more nicely 
    """
    template_name: str = "forms/default_form.html"
    method: str = "post"
    disable_csrf: bool = True
    html_id: str = None
    css_class: str = ""
  


class SearchForm(RenderableFormMixin, forms.Form):
    """
    An example form showing how easy it is to use RenderableFormMixin.
    """
    method = "get"
    
    # Fields added as usual
    query = forms.CharField()
    category = forms.ChoiceField(choices=[('one', "Option one"), ('two', "Option two"), ("three", "Option three")])
    audience = forms.ChoiceField(choices=[('humans', "Humans"), ('robots", "Robots"), ("aliens", "Aliens")])
