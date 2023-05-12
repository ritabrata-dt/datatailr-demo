import io
import dt.user
from dt.cloud.blob_storage import BlobStorage



def read_dataframe(name: str, reader: callable = None, bucket: str = None):
    '''
    Load a dataframe from a file in the blob storage.
    - name: The name of the file in the blob storage.
    - bucket: The name of the bucket in the blob storage. By default, the user's bucket.
    - reader: A function that reads the file and returns a dataframe.
    - Returns: A pandas DataFrame.

    example usage:

    >>>df1 = load_dataframe('my_file.csv', pd.read_csv, bucket='my_bucket)
    >>>df2 = pd.read_parquet(load_dataframe('my_file.parquet'))
    '''
    dt.user.set_current_user(dt.user.signed_user())
    try:
        blob = io.StringIO(BlobStorage().get_object(name, bucket).decode())
    except UnicodeDecodeError:
        blob = io.BytesIO(BlobStorage().get_object(name, bucket))
    if reader:
        return reader(blob)
    else:
        return blob

def write_dataframe(df, name: str, bucket: str = None, format: str = 'parquet'):
    '''
    Write a dataframe to a file in the blob storage.
    - df: The dataframe to write.
    - name: The name of the file in the blob storage.
    - bucket: The name of the bucket in the blob storage. By default, the user's bucket.
    - format: The format to write the dataframe in. Default is parquet. Supported formats are csv, parquet, json, and pickle.
    '''
    dt.user.set_current_user(dt.user.signed_user())
    if format == 'csv':
        blob = io.StringIO()
        df.to_csv(blob)
        BlobStorage().put_object(str.encode(blob.getvalue()), name, bucket)
    elif format == 'parquet':
        blob = io.BytesIO()
        df.to_parquet(blob)
        BlobStorage().put_object(blob.getvalue(), name, bucket)
    elif format == 'json':
        blob = io.StringIO()
        df.to_json(blob)
        BlobStorage().put_object(str.encode(blob.getvalue()), name, bucket)
    elif format == 'pickle':
        blob = io.BytesIO()
        df.to_pickle(blob)
        BlobStorage().put_object(blob.getvalue(), name, bucket)
    else:
        raise ValueError('Unsupported format: ' + format)
