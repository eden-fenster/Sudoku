# Set the path
import os
import sys
from flask import Manager, Server
from old_server.application import create_app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))
app = create_app()
manager = Manager(app)

# Turn on debugger and reloader.
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 5000)))
)

if __name__ == "__main__":
    manager.run()