import discord
from os import listdir
from os.path import isfile, join, dirname
from importlib.util import spec_from_file_location, module_from_spec

def handle_events(client: discord.Client):
    events_dir = join(dirname(__file__), '..', 'events')
    files = listdir(events_dir)

    for filename in files:

        if not filename.endswith('.py'):
                continue

        event_name = filename.removesuffix('.py')

        try:
            event_path = join(events_dir, filename)

            spec = spec_from_file_location(event_name, event_path)
            module = module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'run'):
                async def wrapper(*args, _run=module.run):
                    await _run(client, *args)
                
                setattr(client, event_name, wrapper)

            print(f"✅ Loaded event '{event_name}'")
        except Exception as exception:
            print(f"❌ Failed to load event '{event_name}': {exception}")
