# face_recognition
Bài tập lớn Chuyên đề<br/>
## Libraries
1. cmake
2. opencv-python
3. dlib
4. face_recognition
5. imutils
6. numpy
## Dataset
[Libor Spacek's Facial Images Databases](http://cmp.felk.cvut.cz/~spacelib/faces/ "Face Recognition Data")
## Usage
Name | Usage | What's it for?
--- | --- | --- |
copy.cmd | Open PowerShell or Command Prompt then `cd` to the directory of project.<br>After that, type `.\copy.cmd` and press enter. | This is a script for copy a random image of each instance to examples folder to test.<br>And it would save to `examples` folder. |
encode_faces.py | `python encode_faces.py -i <path to dataset> -e <path to serialized db of facial encodings .e.g encodings.pickle> [-d] [<face detection model to use: either 'hog' or 'cnn'. Default is 'cnn'>]` | This will serialize dataset to a facial encodings file, that use for recognize. |
filter_faces.py | `python filter_faces.py -i <path to dataset> [-d] [<face detection model to use: either 'hog' or 'cnn'. Default is 'cnn'>]` | This will filter the dataset by loop over each image. If a image that can not recognize is a face, then it could be delete. Else it will show how it be recognize, and you can press `r` button for delete it, or `enter` for continue. |
generate_copy_command.py | `python generate_copy_command.py -i <path to dataset>` | This will generate a copy command content for copy.cmd.<br>It using `get_examples.py` for get a example of each instance. |
get_accuracy.py | `python get_accuracy.py -e <path to serialized db of facial encodings .e.g encodings.pickle> -t <path to examples folder> [-d] [<face detection model to use: either 'hog' or 'cnn'. Default is 'cnn'>]` | This will recognize all faces in examples folder and calculate the percentage of accuracy.<br>It is written based on `recognize_faces_image.py` |
get_examples.py | `python get_examples.py -i <path to dataset> -d <path to destination folder to store example .e.g examples>` | This will get a random image in dataset then copy it to the destination folder. |
recognize_faces_image.py | `python recognize_faces_image.py -e <path to serialized db of facial encodings .e.g encodings.pickle> -i <path to image for recognize> [-d] [<face detection model to use: either 'hog' or 'cnn'. Default is 'cnn'>]` | This will using `face_recognize` library that built from `dlib` library to recognize a face on a image. |
