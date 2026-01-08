from codesmellhunter.smells.long_method import LongMethod
from codesmellhunter.smells.large_class import LargeClass
from codesmellhunter.smells.deep_nesting import DeepNesting
from codesmellhunter.smells.many_params import ManyParameters
from codesmellhunter.smells.magic_numbers import MagicNumbers
from codesmellhunter.smells.duplicate_code import DuplicateCode

def load_smells(config):
    return [
        LongMethod(config["long_method"]),
        LargeClass(config["large_class"]),
        DeepNesting(config["deep_nesting"]),
        ManyParameters(config["many_params"]),
        MagicNumbers(),
        DuplicateCode()
    ]
