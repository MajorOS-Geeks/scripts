(kill -STOP $$; kill -CONT $$) &
sleep 1
mkdir -p /home/$USER/Archives
mkdir -p /home/$USER/Images
mkdir -p /home/$USER/Images

while :
do
    mv /home/$USER/Downloads/*.zip /home/$USER/Archives 2>/dev/null
    mv /home/$USER/Downloads/*.tar /home/$USER/Archives 2>/dev/null
    mv /home/$USER/Downloads/*.gz /home/$USER/Archives 2>/dev/null
    mv /home/$USER/Downloads/*.png /home/$USER/"Images(PNG)" 2>/dev/null
    mv /home/$USER/Downloads/*.jpg /home/$USER/"Images(JPG)" 2>/dev/null
    mv /home/$USER/Downloads/*.pdf /home/$USER/Documents 2>/dev/null
    sleep 10
done