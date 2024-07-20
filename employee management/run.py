# run.py
from app import create_app, db

app = create_app()

if _name_ == '_main_':
    app.run(debug=True)