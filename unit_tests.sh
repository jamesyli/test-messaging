#!/bin/bash

if [ $gooduser ]; then
  echo "$gooduser"
else
  echo "no gooduser"
fi

if [ $goodpassword ]; then
  echo "$goodpassword"
else
  echo "no goodpassword"
fi

echo "$goodkey"

echo "+++end+++"

#exit 0
