sudo echo "options snd slots=snd_usb_audio,snd_bcm2835
options snd_usb_audio index=0
options snd_bcm2835 index=1" > /etc/modprobe.d/alsa-base.conf
sudo echo "export ALSADEV="plughw:0,0"" >> ~/.profile
sudo apt-get install alsa-utils sox libsox-fmt-all
sudo sh -c "echo snd-pcm >> /etc/modules"
