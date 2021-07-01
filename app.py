from dotenv import load_dotenv

from uni_std_arc import create_app

load_dotenv('.env')

app = create_app()

if __name__ == '__main__':
    app.run()
