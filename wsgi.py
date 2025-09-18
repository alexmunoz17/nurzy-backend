from app import create_app

app = create_app()

########## Dev only - For production use gunicorn ##########
if __name__ == "__main__":
    app.run(debug=True)
