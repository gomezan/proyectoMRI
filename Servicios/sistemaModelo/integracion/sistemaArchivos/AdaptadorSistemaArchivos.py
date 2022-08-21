
#utils
import io
from time import sleep
import boto3
import numpy as np
from io import BytesIO
from PIL import Image
from configuracion.AtributosConfiguracion import aws
from integracion.sistemaArchivos.AdaptadorSistemaArchivosInterfaz import AdaptadorSistemaArchivosInterfaz

class AdaptadorSistemaArchivos(AdaptadorSistemaArchivosInterfaz):
    session = boto3.session.Session(aws_access_key_id=aws["AWS_ACCESS_KEY_ID"],
                                    aws_secret_access_key=aws["AWS_ACCESS_KEY_SECRET"],
                                    region_name=aws["REGION_NAME"])
    s3_resource = session.resource('s3')
    bucket_name = aws['BUCKET_NAME']

    def __init__(self):
        pass

    # con este se descarga, decodifica y se utiliza en memoria
    def download_data_from_bucket(self, s3_key):
        
        intentos= 0
        while intentos<20:
            try:
                self.s3_resource = self.session.resource('s3')
                obj = self.s3_resource.Object(self.bucket_name, s3_key)
                io_stream = io.BytesIO()
                print("descargando la imagens de s3")
                obj.download_fileobj(io_stream)
                io_stream.seek(0)
                print("intento de descasrga numero: ",intentos+1 )
                return io_stream.read()
                # data = io_stream.read().decode('utf-8')

            except:
                intentos+=1
                sleep(10)
        return False
        

         

    # con este solo se descarga y se guarda directamente en memoria
    def download_file_from_bucket(self, s3_key, dst_path):
        s3_resource = self.session.resource('s3')
        bucket = self.s3_resource.Bucket(self.bucket_name)
        bucket.download_file(Key=s3_key, Filename=dst_path)

    # subir imagenes al s3
    def upload_data_to_bucket(self, bytes_data, s3_key):
        data_transformed=bytes_data
        self.s3_resource = self.session.resource('s3')
        obj = self.s3_resource.Object(self.bucket_name, s3_key)
        obj.put(ACL='private', Body=data_transformed)

        s3_url = f"https://{self.bucket_name}.s3.amazonaws.com/{s3_key}"
        return s3_url