from app import APP
from app.controllers import person_controllers




print("inside server")

if __name__ == "__main__":
    APP.run(debug=True)