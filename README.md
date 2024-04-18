In **1_data_collection.py** I am collecting user basic details and storing them in a csv file, I am also capturing a picture of the user and saving it as {username}.jpg

In **2_inference.py** I am prompting the user to input username, we will fetch the corresponding image {username}.jpg and compare it with the face that is seen on live camera feed.
If the faces match, we display **MATCHED** otherwise **NOT MATCHED**

Now I want the inference on html page using flask, the **app.py** I have developed will display live camera feed, but the deepface face recognition is still to be integrated
