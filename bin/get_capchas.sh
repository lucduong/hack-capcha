#!/bin/bash
URL=https://chuyencuadev.com/captcha
total=100

start=`date +%s`

counter=0
for i in {0..100}
do
    wget -O $1/chuyencuadev_$i.jpg https://chuyencuadev.com/captcha
    counter=$((counter+1))
done

end=`date +%s`
runtime=$((end-start))
echo "There are $counter capchas were downloaded in $runtime."

