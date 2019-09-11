# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class cgrammer(Component):
    """A cgrammer component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks
- label (string; required): A label that will be printed when this component is rendered.
- network_data (dict; required): The JSON data that Clustergrammer takes in as input"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, network_data=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'label', 'network_data']
        self._type = 'cgrammer'
        self._namespace = 'cgrammer'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'label', 'network_data']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['label', 'network_data']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(cgrammer, self).__init__(**args)
