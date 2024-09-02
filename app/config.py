import os
import firebase_admin
from firebase_admin import credentials


# Initialize Firebase Admin SDK
cred = credentials.Certificate("smartlead_firebase_creds.json")
firebase_admin.initialize_app(cred)



