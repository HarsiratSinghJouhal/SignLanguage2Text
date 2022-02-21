==============================================================================================================================================================================


I am Harsirat Singh Jouhal from Sant Ishar Singh Ji Memorial Public School Karamsar Rara Sahib (Ludhiana).


==============================================================================================================================================================================
I know this directory looks like a mess, I was going to make it look cleaner but since this project is so close to its due time I am currently not going to fix this (SORRY!).
But don't worry just open the main.py file and everything is ready for you.

I don't know if the results would be same on your side but on my side everything is fine.
I can only advice that if there is no output try changing the value in main.py line 60 from 0.7 to something bigger, but if there is wrong output try decreasing the value.
==============================================================================================================================================================================
I have collected the data by myself and curated it also. If you want to increase the accuracy then you can put some extra file into the TraingDataIMG folder from DataCollected/Full Data.
I haven't added it by myself because then  the whole output starts lagging (since 598 images aren't a joke).I hope you understand.
==============================================================================================================================================================================


Feel free to contact me at 2005harsirat@gmail.com

Link to GitHub Repository: https://github.com/HarsiratSinghJouhal/SignLanguage2Text.git
Google Drive link to Full Image Data Collected: https://drive.google.com/drive/folders/1bn8pglKKYmU-rfKrRCYECnH-6nocwsNW?usp=sharing



By the way it was a nice Bootcamp really loved it learnt so much new and the instructors were also very good as the helped at each step and explaind everything explicitly.







==============================================================================================================================================================================
**************Regarding changing the data and retraining the model**************

My project does contain some unnecessary code as I told you I am very close to the deadline. (I hope the due date got extended)
For adding more images:-----
Run the data_collection.py , there you would have to change the index for alpha_path (which would be [serialnumber of alphabet character - 1])
then your images will be stored in DataCollected/FullData/(Alphabet) folder
Next you would have to change the path in the preprocessing.py file to the folder whose images you want to preprocess.(But after I have changed the model there is no need to even use the preprocessing.py

The project is trained in the images in TrainingDataIMG ,so, you can put any image in it and rename it as your label then just run the main.py file and you are good to go.
==============================================================================================================================================================================