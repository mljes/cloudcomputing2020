# SHAREBOOK

## `/login`
### GET
#### _Authorization:_ Basic, use the email and password for your client account
#### _Params:_ None
#### _Body:_ None
#### _Responses:_
- 200 - Success - returns userToken, refreshToken, userId
```json
{
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyZTZiMWM5MjFmYTg2NzcwZjNkNTBjMTJjMTVkNmVhY2E4ZjBkMzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2hhcmVib29rLXRlc3QtOThmNWMiLCJhdWQiOiJzaGFyZWJvb2stdGVzdC05OGY1YyIsImF1dGhfdGltZSI6MTU4NDM3OTM1NSwidXNlcl9pZCI6InQzRjZ6bGhSVEphR3dYVzg2Rk5JbzVFTUQ0QTMiLCJzdWIiOiJ0M0Y2emxoUlRKYUd3WFc4NkZOSW81RU1ENEEzIiwiaWF0IjoxNTg0Mzc5MzU1LCJleHAiOjE1ODQzODI5NTUsImVtYWlsIjoianByb3RpY2hAZGFsLmNhIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImpwcm90aWNoQGRhbC5jYSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.tKmWL3zAHUoWWJl3e0vEJifVrIXS5j5Jm51-rcN8IYW8bF-fNxpqt7nlVvDeWBXsKsN6JaeIiTcRiaENYiQ0RKIMiuhDZMTrBtokiDvMgtn7mBJhytXB-J0yYKmvCe9MMc8CVxyHYIUiX-O9ajd_kwdwyW2EdSFeQQBgS_fKU9RGWTbFg6J6lnSKuOEAshjDDByPcDSVCJbvwciPyAerFoe5Ir2Ds1ELnj7P1Y9szgB2J-NSh4RbHpLyis-_U8oZveAUYj6W627UrJ4axsfzlhlz1V5FZyIDwOKRILbUxBhoL8RLd8KJz9pBDpAo1ithbw1MylyruG0Qss_YNmdVNw", 
    "refresh_token": "AEu4IL0hEGHgCPFDqCNNLSwwE7UKs3kTfTylF0vqrLdyH5x9mNilDgtwfKUZ2x3mmFZ0GViG0YhZuRxqxGMuMn_ouVRCmJEPO_P_hdXL-TBuk4rzmgr89jrvS5eDZw4wDIFij5J-FKv8n96_FV255EM6SFRCD-thuMyeDsMvzhYtA87OgScoB9KtxBGvXY9wRiFEdfgdlOz8l-nat0_57XUSo7HVVUYk-Q"
}
```
- 400 - Too many invalid attempts
- 400 - Invalid email address
- 403 - Incorrect email or password

## `/createaccount`
### POST
#### _Authorization:_ None
#### _Params:_ None
#### _Body:_
- email
- password
- firstName
- lastName

#### _Responses:_
- 200 - Success - returns userToken, refreshToken, userId
```json
{
    "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyZTZiMWM5MjFmYTg2NzcwZjNkNTBjMTJjMTVkNmVhY2E4ZjBkMzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2hhcmVib29rLXRlc3QtOThmNWMiLCJhdWQiOiJzaGFyZWJvb2stdGVzdC05OGY1YyIsImF1dGhfdGltZSI6MTU4NDM5NDYzMiwidXNlcl9pZCI6IkRaajlKTXQwaTJjQndPNnBYbUlwZlZTbmMxcjEiLCJzdWIiOiJEWmo5Sk10MGkyY0J3TzZwWG1JcGZWU25jMXIxIiwiaWF0IjoxNTg0Mzk0NjMyLCJleHAiOjE1ODQzOTgyMzIsImVtYWlsIjoiZGZramRrZm5nakBka2pmZ2RrZm5nLmNhIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImRma2pka2ZuZ2pAZGtqZmdka2ZuZy5jYSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.L_w5AzWXkVkMFGrsVDDNPi6HQ0J9wXd86kMwcCrJO4HSsJrfOMKrg0MWnrkyTsC2Yey-ckZXaOX4uFJt1UJDTnMVsYN1lbgi0s-fu2TwkA-u_2xyuUDWDaEBETlwvBljD-ogHQn5pH7zvm5dKBgvUhWVzN89u2zfV2tPnoNCinJyyLvDKtfPLSU1lQfdo_AZBQ3ex63bYdHzdU2XqKBSyvEQRC-5eXE357iw9pI0JZgrlmWnFzauz6CNABuBlpGnnI9W41ihZ3U84_IvKE7v_DTj7rw8TXR3Hwv9c1yUlYzpmavx6Ul08QtKFSogoNW-87S71dIp-buIyWeVlQcPLQ",
    "refresh_token": "AEu4IL2HB7VvOAuqQ2PhZ78Si9m5wTBdqCqBQMVLF00usObqlQZOMSwZ_n0uwo6g4VJuYyBoTEfMEvtj7Z4ws9u_dil4LA7lGEaOX9fN8BIuh42Y4KqzUAB-eJmkl_CIb5_QcUcoFG6WIHtLBGmQSMrXc33WISLKkKYGaNbLgBMCMkvJ57-2ydyxKqnA5fWQDmANez0lbs_HoK86qlZrNtMY0LjqWRLE5ZLu10AmjPwzL8An_KrWPkg",
    "uid": "DZj9JMt0i2cBwO6pXmIpfVSnc1r1"
}
```
- 400 - Attribute missing from POST body
- 400 - Email taken
- 400 - Invalid email
- 400 - Weak password

## `/refreshtoken`
### GET
#### _Authorization:_ Bearer, use refreshToken
#### _Params:_ None
#### _Body:_ None
#### _Responses:_
- 200 - Success - returns userToken, refreshToken, userId
```json
{
  "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyZTZiMWM5MjFmYTg2NzcwZjNkNTBjMTJjMTVkNmVhY2E4ZjBkMzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc2hhcmVib29rLXRlc3QtOThmNWMiLCJhdWQiOiJzaGFyZWJvb2stdGVzdC05OGY1YyIsImF1dGhfdGltZSI6MTU4NDM3OTM1NSwidXNlcl9pZCI6InQzRjZ6bGhSVEphR3dYVzg2Rk5JbzVFTUQ0QTMiLCJzdWIiOiJ0M0Y2emxoUlRKYUd3WFc4NkZOSW81RU1ENEEzIiwiaWF0IjoxNTg0Mzc5NTYxLCJleHAiOjE1ODQzODMxNjEsImVtYWlsIjoianByb3RpY2hAZGFsLmNhIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImpwcm90aWNoQGRhbC5jYSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.ml_F3ysmmZ1Bo4D5PDqm9_VllUkoAVxLW1dPVhC6t3NMEOlYbcyddK_2kOhvaHPMJ2nw6sJE61BsiH5NgjGsm2v8GTgXM1GNYG5ayR7ZY8ZYekg6_rWlV1slxiJHLpLdHrwUGqZyBtpA97ipZXkLDNdCxoDT1kIFXL_RsTzEmA8Xh8RTz3eEXZzTBrQPF-ywDQ9Qj7rVcKB9HrRfaYY9XiwEnCSriuRpt9cB4lIB_XXicEKROP-97yBC-5n_N7U82ZYDZz3Dhhzmc67qwTlSyr5JkgZnSy13Lt8YcuWzcQ4LZ1Huut-x33oMllVr6FPCrPiKw5dh7DuMchssDchrqg", 
  "refreshToken": "AEu4IL0hEGHgCPFDqCNNLSwwE7UKs3kTfTylF0vqrLdyH5x9mNilDgtwfKUZ2x3mmFZ0GViG0YhZuRxqxGMuMn_ouVRCmJEPO_P_hdXL-TBuk4rzmgr89jrvS5eDZw4wDIFij5J-FKv8n96_FV255EM6SFRCD-thuMyeDsMvzhYtA87OgScoB9KtxBGvXY9wRiFEdfgdlOz8l-nat0_57XUSo7HVVUYk-Q", 
  "userId": "t3F6zlhRTJaGwXW86FNIo5EMD4A3"
}
```

- 403 - Token error

## `/ad`
### GET
#### _Authorization:_ None
#### _Params:_ None
#### _Body:_
#### _Responses:_
- 200 - Success - returns all of the ads in the DB
```json
{
  "-M1fysl_BOEZFG4rt8T-": {
    "author": "John Johnson",
    "dateModified": "February 13, 2020 at 8:00:00 AM UTC-4",
    "datePosted": "February 13, 2020 at 8:00:00 AM UTC-4",
    "description": "This is a book on systems",
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/sharebook-test-98f5c.appspot.com/o/images%2Fdefault.jpg?alt=media&token=f93bd8e1-a82a-4be9-ba9a-44c017bf6aba",
    "status": "available",
    "textbookTitle": "Systems and Why They're Cool",
    "userId": "USubRW1tjKUyVHVNWUqGjwNBJDa2"
  },
  "-M1qvfMuF2mvUZX_t1PO": {
    "author": "Maurice Ravel",
    "dateModified": "March 7, 2020 at 5:37:42 PM UTC-4",
    "datePosted": "March 7, 2020 at 5:37:42 PM UTC-4",
    "description": "Urtext Edition, edited by Roger Nichols, Edition Peters",
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/sharebook-test-98f5c.appspot.com/o/images%2Fdefault.jpg?alt=media&token=f93bd8e1-a82a-4be9-ba9a-44c017bf6aba",
    "status": "available",
    "textbookTitle": "Miroirs for Piano Solo",
    "userId": "orJ32YwmKeOdtQMsMxhV648krBJ3"
  },
  "-M1rT59VsveGvCf2G7dS": {
    "author": "John Bookguy",
    "dateModified": "March 8, 2020 at 12:08:04 AM UTC0",
    "datePosted": "March 8, 2020 at 12:08:04 AM UTC0",
    "description": "eh it's a book I guess",
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/sharebook-test-98f5c.appspot.com/o/images%2Fdefault.jpg?alt=media&token=f93bd8e1-a82a-4be9-ba9a-44c017bf6aba",
    "status": "available",
    "textbookTitle": "Title ",
    "userId": "orJ32YwmKeOdtQMsMxhV648krBJ3"
  }
}
```
- 404 - No ads available //THIS I'M NOT SURE ABOUT, 404 IS USUALLY LIKE A "NULL POINTER" ERROR

### POST
#### _Authorization:_ Bearer, use idToken
#### _Params:_ None
#### _Body:_
- author
- description
- textbookTitle
- image
#### _Responses:_
- 200 - Success - makes a new ad, returns its ID
```json
{
  "name": "-M2ZOaEeYWKdlczHlK7k"
}
```
- 400 - Attribute missing from POST body
- 403 - Authorization token error
- 404 - User does not exist

## `/ad/{string:adid}`
### GET
#### _Authorization:_ Bearer, use idToken
#### _Params:_
__(path)__ adId
#### _Body:_ None
#### _Responses:_
- 200 - Success - returns the requested ad
```json
{
    "author": "Bob Smith", 
    "dateModified": "March 16, 2020 at 5:31:19 PM UTC0", 
    "datePosted": "March 16, 2020 at 5:31:19 PM UTC0", 
    "description": "This is a book about calculus.", 
    "status": "available", 
    "textbookTitle": "All About Calculus", 
    "userId": "t3F6zlhRTJaGwXW86FNIo5EMD4A3"
}
```
- 404 - Ad doesn't exist

### PUT
#### _Authorization:_ Bearer, use idToken
#### _Params:_
__(path)__ adId
#### _Body:_
- author
- description
- status
- textbookTitle
- image
#### _Responses:_
- 200 - Success - edits the ad, returns the changed attributes
```json
{
  "author": "Bob Smith", 
  "dateModified": "March 16, 2020 at 5:35:34 PM UTC0", 
  "description": "This book about is all about calculus!", 
  "status": "available", 
  "textbookTitle": "All About Calculus", 
  "userId": "t3F6zlhRTJaGwXW86FNIo5EMD4A3"
}
```
- 400 - Attribute missing from POST body
- 400 - Invalid ad ID
- 403 - Unauthorized
- 404 - user does not exist

### DELETE
#### _Authorization:_ Bearer, use idToken
#### _Params:_
__(path)__ adId
#### _Body:_ None
#### _Responses:_
- 200 - Successful - deletes the ad AND any associated reviews, returns a message about this
```json
"AD -M2ZOaEeYWKdlczHlK7k REMOVED SUCCESSFULLY."
```
- 400 - Invalid ad ID
- 403 - Unauthorized
- 404 - Ad or user does not exist

## `/review`
### GET
#### _Authorization:_ None
#### _Params:_
__(query)__ adId
#### _Body:_ None
#### _Responses:_
- 200 - Success - returns all reviews corresponding to the adId submitted (NONE if none exist)
```json
{
  "-M2ZR0z2Bj1h2CF_rW-_": {
    "adId": "-M2ZOaEeYWKdlczHlK7k",
    "dateAdded": "March 16, 2020 at 5:41:57 PM UTC0",
    "dateModified": "March 16, 2020 at 5:41:57 PM UTC0",
    "reviewText": "This book is super useful!",
    "textbookTitle": "All About Calculus",
    "userId": "t3F6zlhRTJaGwXW86FNIo5EMD4A3"
  }
}
```
- 404 - No reviews found

### POST
#### _Authorization:_ Bearer, use idToken
#### _Params:_
__(query)__ adId
#### _Body:_
- reviewText
#### _Responses:_
- 200 - Success - creates a review associated with the adId provided. Returns new review ID
```json
{
  "name": "-M2ZR0z2Bj1h2CF_rW-_"
}
```
- 400 - Missing attribute from POST body
- 403 - Unauthorized
- 404 - User or Ad does not exist

## `/review/{string:reviewid}`
### GET
#### _Authorization:_ None
#### _Params:_
__(path)__ reviewId
#### _Body:_ None
#### _Responses:_
- 200 - Success - returns the requested review
```json
{
  "adId": "-M2ZOaEeYWKdlczHlK7k",
  "dateAdded": "March 16, 2020 at 5:41:57 PM UTC0",
  "dateModified": "March 16, 2020 at 5:41:57 PM UTC0",
  "reviewText": "This book is super useful!",
  "textbookTitle": "All About Calculus",
  "userId": "t3F6zlhRTJaGwXW86FNIo5EMD4A3"
}
```
- 404 - Review does not exist

### PUT
#### _Authorization:_ Bearer, use idToken
#### _Params:_
__(path)__ reviewId
#### _Body:_
- reviewText

#### _Responses:_
- 200 - Success - edits the requested at using the submitted data, returns changed attributes
```json
{
  "dateModified": "March 16, 2020 at 5:53:55 PM UTC0", 
  "reviewText": "This book is very very useful for my class!!"
}
```
- 400 - Must provide reviewText
- 403 - Unauthorized
- 404 - Review does not exist

### DELETE
#### _Authorization:_ Bearer, use idToken
#### _Params:_
__(path)__ reviewId
#### _Body:_ None
#### _Responses:_
- 200 - Success - removes the requested review, returns message about that
```json
"REVIEW -M2ZS9n_x0owUYfZriHe REMOVED SUCCESSFULLY."
```
- 403 - Unauthorized
- 404 - Review does not exist