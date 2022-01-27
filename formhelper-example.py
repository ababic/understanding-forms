from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit


class CrispyFormMixin:
    method: str = "POST"
    disable_csrf: bool = False
    html_id: str = ""
    css_class: str = ""
        
    def get_form_action(self):
        return None
        
    def get_form_helper(self):
        return FormHelper(
            form_action=self.get_form_action(),
            form_class=self.css_class,
            form_id=self.html_id,
            form_method=self.method,
            disable_csrf=self.method == "GET" or self.disable_csrf,
            render_hidden_fields=True,
        )
    helper = property(get_form_helper)

   


class SearchForm(CrispyFormMixin, forms.Form):
    method = "GET"
    html_id = "searchform"
    css_class = "form--search"
    
    query = forms.CharField()
    category = forms.ChoiceField(choices=[('one', "Option one"), ('two', "Option two"), ("three", "Option three")])
    audience = forms.ChoiceField(choices=[('humans', "Humans"), ('robots", "Robots"), ("aliens", "Aliens")])
                                                                 
    def get_form_helper(self):
        helper = super().get_form_helper()
        helper.layout = Layout(
            "query"
            Fieldset(
                "Filter results by",
                "category",
                "audience",
            ),
            HTML("<p>Don't forget to click the button below:</p>")
            Submit("Search"),
        )
        return helper
                                                       
                                                                 
                                                              
