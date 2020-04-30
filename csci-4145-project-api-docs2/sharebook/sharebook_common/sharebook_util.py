import datetime, jwt, pyrebase, pathlib

serviceAccountPath = open(str(pathlib.Path.home()) + "/SHAREBOOK_PATH", "r").read() + "/models/sharebook-test-98f5c-firebase-adminsdk-ts88x-2aba47b2e0.json"

DB_CONFIG = {
	"apiKey": "AIzaSyAdjYqwqbCdIsqfQ8E1aNpYmFTmq8OHk-I",
	"authDomain": "sharebook-test-98f5c.firebaseapp.com",
	"databaseURL": "https://sharebook-test-98f5c.firebaseio.com",
	"storageBucket": "sharebook-test-98f5c.appspot.com",
	"serviceAccount": str(serviceAccountPath)
	}

def get_firebase_instance():
	firebase = pyrebase.initialize_app(DB_CONFIG)
	auth = firebase.auth()
	user = auth.sign_in_with_email_and_password("group2.dbtester@gmail.com", "cl0udYYY$")
	return firebase

def get_db_instance():
	firebase = get_firebase_instance()
	return firebase.database()

def get_storage_instance():
	firebase = get_firebase_instance()
	return firebase.storage()

#get current time and format it for Firebase
def get_now_date():
    # grab correct utc offset
    offset = int(datetime.datetime.now().strftime("%H")) - int(datetime.datetime.utcnow().strftime("%H"))

    x = datetime.datetime.now().strftime("%B %-d, %Y at %-I:%M:%S %p UTC" + str(offset))

    return x

def token_is_valid(request):
    try:
        encoded_token = parse_token(request.environ['HTTP_AUTHORIZATION'])
        return check_token(encoded_token)
    except KeyError: # Authorization header is missing
        return False

def get_user_id_from_token(encoded_token):
    try:
        decoded_token = jwt.decode(encoded_token, verify=False)
        user_id = decoded_token["user_id"]
        return user_id
    except:
        return None

def get_refresh_token(encoded_token):
	try:
		decoded_token = jwt.decode(encoded_token, verify=False)
		refresh_token = decoded_token["refreshToken"]
		return refresh_token
	except:
		return None

def check_token(encoded_token):
    try:
        decoded_token = jwt.decode(encoded_token, verify=False)
        token_exp_date = datetime.datetime.fromtimestamp(decoded_token["exp"])
        now_date = datetime.datetime.now()

        print(token_exp_date)
        print(now_date)

        # Check if token is "fresh"
        return (token_exp_date > now_date)
    except: # Authorization header is missing or invalid
        return False

def parse_token(token_str):
    #print(token_str)
    if (token_str[0:6] == "Bearer"):
        return token_str[7:]
    else:
        print("INVALID TOKEN")
        return None

def no_quote(s):
	return s

def main():
    TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjhjZjBjNjQyZDQwOWRlODJlY2M5MjI4ZTRiZDc5OTkzOTZiNTY3NDAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2hhcmVib29rLXRlc3QtOThmNWMiLCJhdWQiOiJzaGFyZWJvb2stdGVzdC05OGY1YyIsImF1dGhfdGltZSI6MTU4Mzc5MTMxNiwidXNlcl9pZCI6IlVTdWJSVzF0aktVeVZIVk5XVXFHandOQkpEYTIiLCJzdWIiOiJVU3ViUlcxdGpLVXlWSFZOV1VxR2p3TkJKRGEyIiwiaWF0IjoxNTgzNzkxMzE2LCJleHAiOjE1ODM3OTQ5MTYsImVtYWlsIjoiMzI3Lm1sakBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyIzMjcubWxqQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.r7KcmnDMualvnVdHgAp7g5Tv-pIubMzpCZIznc4LU_kRwZlwzuqBjBxhm08Y47AJ1O4AWsEDNF3r3B9krQfjpHITlPFpSG8ty1oXrjeJSlYd0mqJrrlsUiw2F9xNKUGzK2A8eosBuWMzxe9_rJNw8e9LPRy2BAR3A-FkPj-4GPUvSf3maKBMPBrnOThYd_trUjIHvhcBl2tQA4WHZ3VzZZClwU9-idomnaq5LxvZ1d9fLpCogpbcbCIspRn9MmxhkhyRo23VeXQAhE_40fquceeoDq6ZjT56P05FOWg8jPaBCBdJRvp3tRyHML5-7WqbmBhSxHvfP8kbVY6lMWQZdA"

    print(token_is_valid(TOKEN))

if __name__ == "__main__":
    main()
