# """A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp
import pulumi.runtime

bucket_name = "nice-etching-pulumi-bucket"

def get_bucket(bucket_name):
    try:
        bucket = gcp.storage.get_bucket(bucket_name)
        return bucket
    except:
        return None

bucket = get_bucket(bucket_name)

if bucket:
    existing_bucket = gcp.storage.Bucket.get("existing-bucket", bucket.id)
else:
    # Create a new bucket if it does not exist
    existing_bucket = gcp.storage.Bucket("new-bucket",
        name=bucket_name,
        location="US")

# Exporting bucket info
pulumi.export("bucket_name", existing_bucket.url)
pulumi.export("bucket_self_link", existing_bucket.self_link)
