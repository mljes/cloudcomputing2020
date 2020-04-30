from flask import Flask, request, jsonify, render_template
from flask_api import status
from flask_cors import CORS, cross_origin
import requests, sys, os
from pathlib import Path

sys.path.insert(0, open(str(Path.home()) + "/SHAREBOOK_PATH", "r").read())
from sharebook_common.sharebook_util import parse_token, token_is_valid, get_user_id_from_token, get_refresh_token
from models import ad, auth, review

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/test', methods=['GET'])
@cross_origin()
def getTest():
    print(request.args.get('name'))
    if (not token_is_valid(request)):
        return "CODE 403 - TOKEN IS INVALID OR MISSING.", 403

    return "THE TEST WAS SUCCESSFUL"

@app.route('/ad', methods=['GET', 'POST'])
@cross_origin()
def allAds():
    #useless comment
    if request.method == 'GET':
        return ad.getAllAds()

    # Check auth token for PUT, POST or DELETE
    if (not token_is_valid(request)):
        return "CODE 403 - AUTHORIZATION TOKEN IS INVALID OR MISSING.", 403
    else:
        # Take info from body of request, make an ad in the DB
        if request.method == 'POST':
            try:
                author = request.form['author']
                description = request.form['description']
                textbookTitle = request.form['textbookTitle']
                image = request.files['image']

                userId = get_user_id_from_token(parse_token(request.environ['HTTP_AUTHORIZATION']))

                return ad.addAd(author, description, textbookTitle, image, userId)

            except KeyError as err:
                return "CODE 400 - ATTRIBUTE MISSING FROM POST BODY.", 400
        else:
            return "CODE 405 - THAT METHOD IS NOT ALLOWED.", 405

@app.route('/ad/<string:adId>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin()
def singleAd(adId):
    adId = str(adId)

    # GET methods do not require auth tokens
    if request.method == 'GET':
        return ad.getAd(adId)

    # Check auth token for PUT, POST or DELETE
    if (not token_is_valid(request)):
        return "CODE 403 - AUTHORIZATION TOKEN IS INVALID OR MISSING.", 403 #403
    else:
        userId = get_user_id_from_token(parse_token(request.environ['HTTP_AUTHORIZATION']))

        if request.method == 'PUT':
            try:
                author = request.form['author']
                description = request.form['description']
                status = request.form['status']
                textbookTitle = request.form['textbookTitle']
                image = request.files['image']

                userId = get_user_id_from_token(parse_token(request.environ['HTTP_AUTHORIZATION']))

                return ad.editAd(adId, author, description, status, textbookTitle, image, userId)

            except KeyError as err:
                print(err)
                return "CODE 400 - ATTRIBUTE MISSING FROM POST BODY.", 400

        elif request.method == 'DELETE':
            return ad.removeAd(adId, userId)

        else:
            return "CODE 405 - THAT METHOD IS NOT ALLOWED.", 405

# Get all reviews associated with an Ad ID, or post a review for an Ad at that ID
#pass adId as a query param, use as search
@app.route('/review', methods=['GET', 'POST'])
@cross_origin()
def allReviews():
    adId = request.args.get('adId')
    if adId == None:
        return "CODE 400 - AD ID IS MISSING FROM QUERY PARAMETERS", 400

    if request.method == 'GET':
        return review.getAllReviews(adId)

    # Bearer token required to perform POST requests
    if (not token_is_valid(request)):
        return "CODE 403 - AUTHORIZATION TOKEN IS INVALID OR MISSING.", 403
    else:
        if request.method == 'POST':
            try:
                reviewText = request.form['reviewText']
                userId = get_user_id_from_token(parse_token(request.environ['HTTP_AUTHORIZATION']))

                return review.addReview(adId, reviewText, userId)
            except KeyError as err:
                return "CODE 400 - ATTRIBUTE MISSING FROM POST BODY.", 400
        else:
            return "CODE 405 - THAT METHOD IS NOT ALLOWED.", 405

#Every review has its own ID (along with adId and userId within its data)
@app.route('/review/<string:reviewId>', methods=['GET', 'PUT', 'DELETE'])
@cross_origin()
def singleReview(reviewId):
    reviewId = str(reviewId)

    if request.method == 'GET':
        return review.getReview(reviewId)

    # Bearer token required to perform PUT and DELETE requests
    if (not token_is_valid(request)):
        return "CODE 403 - AUTHORIZATION TOKEN IS INVALID OR MISSING.", 403
    else:
        userId = get_user_id_from_token(parse_token(request.environ['HTTP_AUTHORIZATION']))

        if request.method == 'PUT':
            try:
                reviewText = request.form['reviewText']
                return review.editReview(reviewId, reviewText, userId)

            except KeyError:
                return "CODE 400 - MUST PROVIDE REVIEWTEXT", 400
        elif request.method == 'DELETE':
            return review.removeReview(reviewId, userId)
        else:
            return "CODE 405 - THAT METHOD IS NOT ALLOWED.", 405

@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    if request.authorization == None:
        return "CODE 403 - Cannot login. Missing login information.", 403

    email = request.authorization['username']
    password = request.authorization['password']

    return auth.login(email, password)

@app.route('/refreshtoken', methods=['GET'])
@cross_origin()
def refresh_token():
    token = parse_token(request.environ['HTTP_AUTHORIZATION'])

    return auth.refresh_token(token)

@app.route('/createaccount', methods=['POST'])
@cross_origin()
def makeUser():
    try:
        email = request.form['email']
        password = request.form['password']
        firstName = request.form['firstName']
        lastName = request.form['lastName']

        return auth.create_user(email, password, firstName, lastName)
    except KeyError as err:
        print(err)
        return "CODE 400 - ATTRIBUTE MISSING FROM POST BODY.", 400
