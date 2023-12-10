Facial rekognition with AWSrekognition


AWS Rekognition Collection, S3 Bucket, DynamoDB, and Lambda Function Setup Documentation
1. Create AWS Rekognition Collection
Overview:
In this step, we will create an AWS Rekognition collection to store facial features for comparison.

Procedure:
Navigate to AWS Rekognition:

Open the AWS Rekognition Console.
Create a Collection:

Click on "Collections" in the left navigation pane.
Click the "Create collection" button.
Provide a name for your collection and create it.
Notes:
Make sure to note down the collection ARN, as you'll need it later.
2. Create S3 Bucket
Overview:
In this step, we will create an S3 bucket to store images for facial recognition.

Procedure:
Navigate to AWS S3:

Open the AWS S3 Console.
Create a Bucket:

Click on "Create bucket" button.
Provide a unique bucket name and select a region.
Configure additional settings as needed.
Click "Create bucket."
Notes:
Note down the S3 bucket name and region.
3. Create DynamoDB Database
Overview:
In this step, we will create a DynamoDB database to store information about images and their matches.

Procedure:
Navigate to AWS DynamoDB:

Open the AWS DynamoDB Console.
Create a Table:

Click on "Create table" button.
Provide a table name, primary key, and other settings.
Click "Create."
Notes:
Note down the DynamoDB table name.
4. Create Lambda Function
Overview:
In this step, we will create an AWS Lambda function that triggers on S3 events and processes images using AWS Rekognition.

Procedure:
Navigate to AWS Lambda:

Open the AWS Lambda Console.
Create a Lambda Function:

Click on "Create function" button.
Configure the function details, including name, runtime, role, etc.
Set up triggers by adding an S3 trigger.
Configure the function code (you'll need to write this based on your requirements).
Notes:
Note down the Lambda function name and ARN.
Configure the Lambda function environment variables with necessary information.
5. Usage of putimages.py
Overview:
This script is used to push photos to the S3 bucket and store information in DynamoDB.

Procedure:
Setup:

Install required libraries using pip install boto3.
Usage:

Execute the script: python putimages.py.
Provide necessary information when prompted (e.g., image path, S3 bucket name, DynamoDB table name).
The script will upload images to S3 and store information in DynamoDB.
6. Usage of testing.py
Overview:
This script is used to test the AWS Rekognition service by iterating through images in an S3 bucket and checking for matches.

Procedure:
Setup:

Install required libraries using pip install boto3.
Usage:

Execute the script: python testing.py.
Provide necessary information when prompted (e.g., S3 bucket name, Rekognition collection ARN).
The script will iterate through S3 images, perform facial recognition, and display results.
