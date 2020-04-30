import pyrebase, sys, pathlib, json
from requests import HTTPError

#Adding the path to the utilities module
sys.path.insert(0, open(str(pathlib.Path.home()) + "/SHAREBOOK_PATH", "r").read())
from sharebook_common.sharebook_util import get_now_date, DB_CONFIG, get_refresh_token

#for local testing
def main():
    if len(sys.argv) == 1:
        print("Usage: python3 auth.py { create | login }")
        quit()

    choice = sys.argv[1]
    token = ""
    if str(choice) == "create":
        token = create_user(input("Email: "), input("Password: "), input("First name: "), input("Last name: "))
    elif str(choice) == "login":
        login("group2.dbtester@gmail.com", "cl0udYYY$")
        token = login(input("Email: "), input("Password: "))
    else:
        print("Usage: python3 auth.py { create | login }")

    print(token)

#login using email and password
def login(email, password):
    try:
        firebase = pyrebase.initialize_app(DB_CONFIG)
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)

        return json.dumps({"id_token": user['idToken'],"refresh_token": user['refreshToken']})

    except HTTPError as err:
        err_data = err.args[0].response.json()["error"]
        err_string = err_data["message"]
        err_code = err_data["code"]

        if ("TOO_MANY_ATTEMPTS" in err_string):
            return "CODE 400 - TOO MANY ATTEMPTS"
        elif ("INVALID_PASSWORD" in err_string) or ("EMAIL_NOT_FOUND" in err_string):
            return "CODE 403 - EMAIL AND/OR PASSWORD INCORRECT"
        elif ("INVALID_EMAIL" in err_string):
            return "CODE 400 - INVALID EMAIL ADDRESS"

#create a new user in the Firebase system
def create_user(email, password, firstName, lastName):
    firebase = pyrebase.initialize_app(DB_CONFIG)
    auth = firebase.auth()

    try:
        auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)

        db = firebase.database()

        dateCreated = get_now_date()

        data = {
            "email": str(email),
            "firstName": str(firstName),
            "lastName": str(lastName),
            "dateCreated": str(dateCreated)
        }

        db.child("users").child(user['localId']).set(data)

        return_data = {
            "id_token": user['idToken'],
            "refresh_token": user['refreshToken'],
            "uid": user["localId"]
        }

        return json.dumps(return_data), 200

    except HTTPError as err:
        err_data = err.args[0].response.json()["error"]
        err_string = err_data["message"]
        err_code = err_data["code"]

        if ("EMAIL_EXISTS" in err_string):
            return "CODE 400 - EMAIL IS TAKEN", 400
        elif ("INVALID_EMAIL" in err_string):
            return "CODE 400 - INVALID EMAIL ADDRESS", 400
        elif ("WEAK_PASSWORD" in err_string):
            return "CODE 400 - PASSWORD MUST BE AT LEAST 6 CHARACTERS.", 400

def refresh_token(userId):
    firebase = pyrebase.initialize_app(DB_CONFIG)
    auth = firebase.auth()

    print(userId)

    return auth.refresh(userId)

if __name__ == "__main__":
    main()
