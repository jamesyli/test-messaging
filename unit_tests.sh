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

if [ $goodkey ]; then
  echo "$goodkey"
else
  echo "no goodkey"
fi

echo "+++end+++"

#exit 0
