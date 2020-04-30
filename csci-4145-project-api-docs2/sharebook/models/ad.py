import pyrebase, sys, pathlib, os, json, uuid
from requests.exceptions import HTTPError
from collections import OrderedDict
import firebase_admin
from firebase_admin import credentials

#Adding the path to the utilities module
SHAREBOOK_PATH = open(str(pathlib.Path.home()) + "/SHAREBOOK_PATH", "r").read()

print("SHAREBOOK IS HERE: " + SHAREBOOK_PATH)

sys.path.insert(0, SHAREBOOK_PATH)
from sharebook_common.sharebook_util import get_now_date, get_db_instance, get_storage_instance, serviceAccountPath

cred = credentials.Certificate(serviceAccountPath)
firebase_admin.initialize_app(cred)

def no_quote(s, safe=''):
	return s

orig_quote = pyrebase.pyrebase.quote
pyrebase.pyrebase.quote = no_quote

def main():
	if len(sys.argv) == 1:
		print("Usage: python3 ad.py { post | get | getall | update | delete }")
		quit()

	print("NOTE: Make sure dates are formatted like this: 'February 13, 2020 at 8:00:00 AM UTC-4'")
	choice = sys.argv[1]

	if choice == "post":
		result = addAd(input("Author: "), input("Descr: "), input("Textbook title: "), input("User ID:"))
		print(result)
	elif choice == "get":
		print(getAd(input("Ad ID: ")))
	elif choice == "getall":
		print(getAllAds())
	elif choice == "update":
		result = editAd(input("Ad ID: "), input("Author: "), input("Descr: "), input("Status: "), input("Textbook title: "), input("User ID: "))
		print(result)
	elif choice == "delete":
		print(removeAd(db, input("Ad ID: "), input("userId: ")))
	else:
		print("Usage: python3 ad.py { post | get | getall | update | delete }")

#POST - Create ad
def addAd(author, description, textbookTitle, image, userId):
	datePosted = get_now_date()
	db = get_db_instance()

	# Checks if user exists
	user = db.child("users").child(userId).get().val()

	if(user == None):
		return "CODE 404 - USER DOES NOT EXIST", 404
	# Checking to see all if fields filled ou
	elif(author == "" or description == "" or textbookTitle == ""):
		return "CODE 400 - ENTER DATA INTO ALL REQUIRED FIELDS", 400
	else:
		new_ad_id = str(uuid.uuid1())

		imageUrl = ""
		if image.filename != "":
			imageUrl = uploadAdImage(new_ad_id, image)
		else:
			imageUrl = "https://firebasestorage.googleapis.com/v0/b/sharebook-test-98f5c.appspot.com/o/images%2Fdefault.jpg?alt=media&token=f93bd8e1-a82a-4be9-ba9a-44c017bf6aba"

		data = {
	        "author": str(author),
	        "datePosted": str(datePosted),
			"dateModified": str(datePosted),
	        "description": str(description),
	        "status": "available",
	        "textbookTitle": str(textbookTitle),
	        "userId": str(userId),
			"imageUrl": str(imageUrl)
	    }

		db.child("ads").child(new_ad_id).set(data)

		data["id"] = str(new_ad_id)

		return json.dumps(data)

# put submitted ad image into storage with name that matches corresponding ad's ID
def uploadAdImage(adId, image):
	storage = get_storage_instance()
	local_path = str(SHAREBOOK_PATH + "/models/ad_images/")

	try:
		image.save(os.path.join(local_path, image.filename))
		image_path = "images/" + str(adId) + ".jpg"
		storage.child(image_path).put(local_path + image.filename)
		removal_command = "rm -f " + str(local_path) + str(image.filename)
		print(removal_command)
		os.system(removal_command)

		return getImageUrl(adId)
	except IsADirectoryError:
		print("NO IMAGE SUBMITTED!")
	except:
		print("\n###\n###\n###SOMETHING ELSE BROKE.\n###\n###\n###")

# remove ad image
def deleteAdImage(adId):
	storage = get_storage_instance()

	try:
		image_path = "images/" + str(adId) + ".jpg"
		storage.delete(image_path)
	except:
		print("###\nDIDN'T WORK\n###")

#GET - Retrieve an ad by id
def getAd(id):
	db = get_db_instance()

	ad = db.child("ads").child(id).get().val()

	ad_json = json.dumps(ad)

	if(ad == None):
		return "CODE 404 - AD DOES NOT EXIST", 404
	else:
		return ad_json

# Retrieve URL for ad image to send to front-end
def getImageUrl(adId):
	pyrebase.pyrebase.quote = orig_quote
	storage = get_storage_instance()
	url = ""
	try:
		url = storage.child("images/" + str(adId) + ".jpg").get_url(token="f8cc45ae-4d1e-43b8-9097-cb8b3b32318c")
	except:
		url = "https://firebasestorage.googleapis.com/v0/b/sharebook-test-98f5c.appspot.com/o/images%2Fdefault.jpg?alt=media&token=f93bd8e1-a82a-4be9-ba9a-44c017bf6aba"

	pyrebase.pyrebase.quote = no_quote

	return str(url)

#GET - Retrieve all ads
def getAllAds():
	db = get_db_instance()

	all_ads = db.child("ads").get().val()

	all_ads_json = json.dumps(all_ads)

	if(all_ads == None):
		return "CODE 404 - THERE ARE CURRENTLY NO ADS", 404
	else:
		return all_ads_json

#PUT - Update existing ad
def editAd(id, author, description, status, textbookTitle, image, userId):
	dateModified = get_now_date()
	db = get_db_instance()

	try:
		ad = db.child("ads").child(id).get().val()

		if (ad == None):
			return "CODE 404 - AD/USER DOES NOT EXIST", 404
		elif(ad["userId"] != userId):
			return "CODE 403 - UNAUTHORIZED", 403
		else:
			new_data = {
		        "author": str(author),
		        "description": str(description),
				"dateModified": str(dateModified),
		        "status": str(status),
		        "textbookTitle": str(textbookTitle),
				"userId": str(userId)
			}

			if image != None:
				uploadAdImage(id, image)

			return db.child("ads").child(id).update(new_data)

	except HTTPError as err:
		return "CODE 400 - Invalid ad ID submitted.", 400


#DELETE - Delete existing ad
def removeAd(id, userId):
	db = get_db_instance()

	try:
		ad = db.child("ads").child(id).get().val()

		if(ad == None):
			return "CODE 404 - AD/USER DOES NOT EXIST", 404
		elif(ad["userId"] != userId):
			return "CODE 403 - UNAUTHORIZED", 403
		else:
			deleteAdImage(id)
			removeReviewsForAd(db, id)
			db.child("ads").child(id).remove(), 200
			return str("AD " + id + " REMOVED SUCCESSFULLY."), 200

	except HTTPError as err:
		return "CODE 400 - Invalid ad ID submitted.", 400

def removeReviewsForAd(db, adId):
	try:
		associated_reviews = db.child('reviews').order_by_child("adId").equal_to(adId).get().val()
		print(json.dumps(associated_reviews))

		for item in associated_reviews:
			print("ALSO REMOVING REVIEW: " + item)
			db.child("reviews").child(item).remove()
	except:
		print("NO REVIEWS ASSOCIATED WITH AD TO BE DELETED.")

if __name__ == "__main__":
	main()
