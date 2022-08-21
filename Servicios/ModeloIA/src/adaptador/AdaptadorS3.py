import sys
import os
import boto3
import io
from datetime import datetime

#sys.path.append(os.path.abspath(os.path.join('src/', 'configuraciones')))
#from configuraciones import aws
from dotenv import load_dotenv
load_dotenv(verbose=True)

aws = {
  "AWS_ACCESS_KEY_ID" : "AKIAVZASHVKLQFWOYP6X",
  "AWS_ACCESS_KEY_SECRET" : "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",
  "REGION_NAME" : "sa-east-1",
  "BUCKET_NAME" : "imagenes-tesis",
  "IMAGENES_PROCESADAS" : "procesada",
  "IMAGENES_NO_PROCESADAS" : "no_procesada",
  "RESOURCE" : "s3"
  }

class AdaptadorS3():

    session = boto3.session.Session(aws_access_key_id=aws["AWS_ACCESS_KEY_ID"],
                                    aws_secret_access_key=aws["AWS_ACCESS_KEY_SECRET"],
                                    region_name=aws["REGION_NAME"])
    s3_resource = session.resource('s3')
    bucket_name = aws['BUCKET_NAME']
    
    def __init__(self) :
        pass

    
    #con este se descarga, decodifica y se utiliza en memoria, falta encontrar un manejador de archivos nifty
    def download_data_from_bucket(self, s3_key):
        self.s3_resource = self.session.resource('s3')
        obj = self.s3_resource.Object(self.bucket_name, s3_key)
        io_stream = io.BytesIO()
        obj.download_fileobj(io_stream)
        io_stream.seek(0)
        #data = io_stream.read().decode('utf-8')
        return io_stream.read()

    #con este solo se descarga y se guarda directamente en memoria
    def download_file_from_bucket(self, s3_key, dst_path):
        s3_resource = self.session.resource('s3')
        bucket = self.s3_resource.Bucket(self.bucket_name)
        bucket.download_file(Key=s3_key, Filename=dst_path)


    #subir imagenes al s3
    def upload_data_to_bucket(self,bytes_data, s3_key):
        self.s3_resource = self.session.resource('s3')
        obj = self.s3_resource.Object(self.bucket_name, s3_key)
        obj.put(ACL='private', Body=bytes_data)

        s3_url = f"https://{self.bucket_name}.s3.amazonaws.com/{s3_key}"
        return s3_url
    

test =AdaptadorS3()
print(datetime.now())
about_data = test.download_data_from_bucket('procesada/Lanczosa=3_1_otra.nii')
print(datetime.now())
test.upload_data_to_bucket(about_data, 'prueba/Lanczosa=3_1_otra.nii')
print(datetime.now())