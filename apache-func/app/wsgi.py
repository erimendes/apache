# from app import app

# if __name__ == "__main__":
#     app.run(debug=True, port=8080)

from app import create_app

# Inicializa o objeto `app` chamando a função `create_app()`
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # Apenas para o desenvolvimento, não necessário no Gunicorn
