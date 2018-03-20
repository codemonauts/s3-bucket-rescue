# bucket-rescue

## Usecase
You have an S3 Bucket with activated versioning but you deleted/corrupted/... EVERY file in it.

## What it does
This tool will find the newest version of a file which has a filesize > 0 bytes and will download it to this folder.

## How to use
```
aws s3api list-object-versions --bucket <buckername> | ./find_version.py | ./download.sh
```

## ToDo, Known Bugs
  - Bucket name has to be changed in the source of both scripts
  - No filter. It will download every file in the bucket
  - `download.sh` crashes on nested folder strcutures because it can't create the file if the parent folder is missing
