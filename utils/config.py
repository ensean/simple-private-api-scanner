import os

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sqlite_info = {
    'DB': os.path.join(project_dir, 'ios_private.db'),
}
