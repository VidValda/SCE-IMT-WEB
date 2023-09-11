from django import forms

class ProjectCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = []

        final_attrs = self.build_attrs(self.attrs, attrs)
        output = []
        id_ = final_attrs.get('id', None)
        for i, choice in enumerate(self.choices):
            # Generate a unique ID for each checkbox
            if id_:
                final_attrs = dict(final_attrs, id=f"{id_}_{i}")
            cb = forms.CheckboxInput(final_attrs, check_test=lambda option_value: option_value in value)
            option_value = choice[0]
            project_title = choice[1]  # Access the project title
            rendered_cb = cb.render(name, option_value)
            output.append(f'<label for="{final_attrs["id"]}">{rendered_cb} {project_title}</label>')

        return '\n'.join(output)
    
class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'widgets/checkbox_select.html'  # Use a custom template

