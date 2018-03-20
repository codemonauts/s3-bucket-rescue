#! /bin/bash

while read line
do
  FILEPATH=`echo "$line" | cut -d"|" -f1`
  VERSION=`echo "$line" | cut -d"|" -f2`
  echo "Recovering version $VERSION for file $FILEPATH..."
  aws s3api get-object --bucket "bucketname" --version-id "$VERSION" --key "$FILEPATH" "$FILEPATH"
done < /dev/stdin
