#!/bin/bash
URL=https://chuyencuadev.com/captcha

start=`date +%s`

counter=0
for i in {0..3}
do
    wget -O chuyencuadev_$i.jpg https://chuyencuadev.com/captcha
    counter=$((counter+1))
done

end=`date +%s`
runtime=$((end-start))
echo "There are $counter capchas were downloaded in $runtime."

