import builtins
from helpers import set_config, activate_virtual_environment, set_localization

args = set_config('simple.json')
if args.get('environment') != "":
    activate_virtual_environment(**args)
set_localization(**args)
_ = builtins.__dict__.get('_', lambda x: x)
