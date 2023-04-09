from typing import Any, List, Optional, Text

from rasa.nlu.components import Component
from rasa.nlu.tokenizers.tokenizer import Tokenizer
from rasa.nlu.training_data import Message, TrainingData
from rasa_addons.nlu.components.lookup_tables import LookupTable

@DefaultV1Recipe.register(LookupTableFeaturizer)
class LookupTableFeaturizer(Component):

    name = "lookup_table_featurizer"
    provides = ["text_features"]
    requires = ["tokens"]
    defaults = {}
    language_list = None

    def __init__(self, component_config=None):
        super().__init__(component_config)

        self.table_name = self.component_config.get("table_name")

        self.lookup_table = LookupTable.load(self.table_name)

    def train(self, training_data, cfg=None, **kwargs):
        for example in training_data.training_examples:
            tokens = example.get("tokens")
            features = self._get_features(tokens)
            example.set("text_features", features)

    def process(self, message, **kwargs):
        tokens = message.get("tokens")
        features = self._get_features(tokens)
        message.set("text_features", features, add_to_output=True)

    def _get_features(self, tokens):
        features = [0.0] * len(tokens)

        for idx, token in enumerate(tokens):
            if token.text in self.lookup_table:
                features[idx] = 1.0

        return features