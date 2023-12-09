# import boto3

# s3 = boto3.resource('s3')

# # Define the bucket name
# bucket_name = 'famouspersonsq-images'

# # Specify the object key
# object_key = 'images/image1.jpg'


# # Get list of objects for indexing
# images=[('image1.jpg','Elon Musk'),
#       ('image2.jpg','Elon Musk'),
#       ('image3.jpg','Bill Gates'),
#       ('image4.jpg','Bill Gates'),
#       ('image5.jpg','Sundar Pichai'),
#       ('image6.jpg','Sundar Pichai')
#       ]

# # Iterate through list to upload objects to S3   
# for image in images:
#     file = open(image[0],'rb')
#     object = s3.Object("https://famouspersonsq-images.s3.us-east-1.amazonaws.com/images/image1.jpg",'index/'+ image[0])
#     ret = object.put(Body=file,Metadata={'FullName':image[1]})

import boto3

# S3 bucket details
bucket_name = 'famouspersonsq-images'
bucket_region = 'us-east-1'

# List of objects for indexing
images = [
    ('pranjaltest.jpg', 'Pranjal jain'),
]

# Initialize S3 client
s3 = boto3.client('s3', region_name=bucket_region)

# Iterate through the list to upload objects to S3
for image in images:
    file_name = image[0]
    full_name = image[1]
    object_key = 'index/' + file_name

    # Upload the file to S3 and add metadata
    s3.upload_file(file_name, bucket_name, object_key, ExtraArgs={'Metadata': {'FullName': full_name}})
