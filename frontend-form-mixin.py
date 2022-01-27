from django import forms


class RenderableFormMixin:
    """
    A mixin that can be applied to Django 4 forms to get them to render more nicely 
    """
    template_name: str = "forms/default_form.html"
    method: str = "post"
    disable_csrf: bool = False
    html_id: str = ""
    css_class: str = ""
    submit_button_label: str = "Submit"
        
    def get_form_action(self):
        # Override this method if the form needs to post somewhere other than
        # the current view
        return None


class SearchForm(RenderableFormMixin, forms.Form):
    """
    An example form showing how easy it is to use RenderableFormMixin.
    """
    
    # RenderableFormMixin attribute overrides
    method = "get"
    html_id = "searchform"
    css_class = "form--search"
    submit_button_label: "Search"
    
    # Fields
    query = forms.CharField()
    category = forms.ChoiceField(choices=[('one', "Option one"), ('two', "Option two"), ("three", "Option three")])
    audience = forms.ChoiceField(choices=[('humans', "Humans"), ('robots", "Robots"), ("aliens", "Aliens")])
