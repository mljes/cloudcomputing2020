import pyrebase, sys, pathlib, json
#Adding the path to the utilities module
sys.path.insert(0, open(str(pathlib.Path.home()) + "/SHAREBOOK_PATH", "r").read())
from sharebook_common.sharebook_util import get_now_date, get_db_instance, no_quote

pyrebase.pyrebase.quote = no_quote

def main():
	db = get_db_instance()

	if len(sys.argv) == 1:
		print("Usage: python3 review.py { post | get | getall | update | delete }")
		quit()

	print("NOTE: Make sure dates are formatted like this: 'February 13, 2020 at 8:00:00 AM UTC-4'")
	choice = sys.argv[1]

	if choice == "post":
		addReview(db, input("Ad ID: "), input("Descr: "), input("Textbook title: "), input("User ID:"))
	elif choice == "get":
		getReview(input("Review ID: "))
	elif choice == "getall":
		getAllReviews(input("Ad ID: "))
	elif choice == "update":
		editReview(db, input("Review ID: "), input("Ad ID: "), input("Descr: "), input("Textbook title: "), input("User ID: "))
	elif choice == "delete":
		removeReview(db, input("Review ID: "), input("User ID: "))
	else:
		print("Usage: python3 review.py { post | get | getall | update | delete }")

#POST - Create review
def addReview(adId, reviewText, userId):
	db = get_db_instance()
	dateAdded = get_now_date()

	# Checks if user exists
	user = db.child("users").child(userId).get().val()
	ad = db.child("ads").child(adId).get().val()

	if(user == None):
		return "CODE 404 - USER DOES NOT EXIST", 404
	elif(ad == None):
		return "CODE 404 - AD DOES NOT EXIST", 404
	# Checking to see all if required fields filled out
	elif(reviewText == ""):
		return "CODE 400 - ENTER DATA INTO ALL REQUIRED FIELDS", 400
	else:
		textbookTitle = ad["textbookTitle"]

		data = {
	        "adId": str(adId),
	        "dateAdded": str(dateAdded),
			"dateModified": str(dateAdded),
	        "reviewText": str(reviewText),
	        "textbookTitle": str(textbookTitle),
	        "userId": str(userId)
	    }

		return db.child("reviews").push(data)

#GET - Retrive a review by id
def getReview(id):
	db = get_db_instance()

	review = db.child("reviews").child(id).get().val()
	review_json = json.dumps(review)

	if(review == None):
		return "CODE 404 - REVIEW DOES NOT EXIST", 404
	else:
		return review_json

#GET - Retrive all reviews
def getAllReviews(adId):
	db = get_db_instance()

	try:
		all_reviews = db.child('reviews').order_by_child("adId").equal_to(adId).get().val()
	except IndexError as err:
		return json.dumps({})

	all_reviews_json = json.dumps(all_reviews)

	return all_reviews_json

#PUT - Update existing review
def editReview(id, reviewText, userId):
	db = get_db_instance()
	dateModified = get_now_date()

	new_data = {
		"dateModified": str(dateModified),
		"reviewText": str(reviewText)
	}

	review = db.child("reviews").child(id).get().val()

	if review == None:
		return "CODE 404 - REVIEW DOES NOT EXIST", 404
	elif(review["userId"] != userId):
		return "CODE 403 - UNAUTHORIZED. REVIEW DOES NOT BELONG TO USER.", 403
	else:
		return db.child("reviews").child(id).update(new_data)


#DELETE - Delete existing review
def removeReview(id, userId):
	db = get_db_instance()
	review = db.child("reviews").child(id).get().val()

	if(review == None):
		return "CODE 404 - REVIEW/USER DOES NOT EXIST", 404
	elif(review["userId"] != userId):
		return "CODE 403 - UNAUTHORIZED", 403
	else:
		db.child("reviews").child(id).remove()
		return str("REVIEW " + id + " REMOVED SUCCESSFULLY."), 200

if __name__ == "__main__":
	main()
