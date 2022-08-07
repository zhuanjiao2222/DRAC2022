# DRAC2022 Submission Guidance
This instruction provides the guidance of how to pack results into an acceptable submission in DRAC2022 Challenge. Please direct any questions or concerns about these instructions or the submission process generally to [DRAC2022 grand challenge forum](https://grand-challenge.org/forums/forum/diabetic-retinopathy-analysis-challenge-659/).

**Task 1 submission guidance:**

The submitted zip file should be formatted like the below.

```
Team_Name/
├─ 1.nii.gz
├─ 2.nii.gz
├─ 3.nii.gz
```

* The 1.nii.gz, 2.nii.gz and 3.nii.gz contain the predicted masks of class 1 (Intraretinal Microvascular Abnormalities), class 2 (Nonperfusion Areas) and class 3 (Neovascularization) respectively in test set. 
* For all three .nii.gz files, the predicted lesion area pixel value is 1, and the background pixel value is 0. The shape of each .nii.gz file is 65 × 1024 × 1024 where 65 is the number of images in test set, and 1024 is the height and width of the image. The order of the images in the .nii.gz file should be sorted according to the image name in test set from small to large, such as 086.png 285.png 402.png ... 1299.png. 
* We provide an example showing how to convert the predicted masks in test set to the .nii.gz file, see masks_to_nii.py.
* **The folder should be named with your Team_Name, and should be zipped before submission.**

**Task 2 & Task 3  submission guidance:**

* You are required to submit a .csv file containing the image name, predicted class, and predicted probability for each class. **The headers in the csv file should be consistent with the example, in which the case indicates the image name, the class indicates the predicted class, P0, P1 and P2 indicate the predicted probability for class 0, 1 and 2, respectively. Note that P0 + P1 + P2 = 1. **
* Make sure the predictions in the submitted csv file all be matched with the test images one-to-one, or are considered invalid submissions and no score will be generated.
* **The csv file should be named with your Team_Name.**
