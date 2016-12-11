### Photo Verifier
Detects if upload images has human faces.



## Usages
* Install cv
* Clone this repo into a directory
* Install dependencies like using the following command:
```
pip install -r requirements.txt
```

* Run the server using the following command:
```
python manage.py runserver
```
then visit http://127.0.0.1:8000

* Select the file using Browser/Choose file button.
* Click **Verify**
* On next page, it'll verify if image has face.

## Example outputs
If faces are detected:
```
{"num_faces": 1, "success": true}
```

If no face found,
{"success": false}
