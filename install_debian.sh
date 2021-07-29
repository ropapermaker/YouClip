#!/bin/bash


txtrst=$(tput sgr0) # Text reset
txtred=$(tput setaf 1) # Red
txtgrn=$(tput setaf 2) # Green
txtylw=$(tput setaf 3) # Yellow
txtblu=$(tput setaf 4) # Blue
txtpur=$(tput setaf 5) # Purple
txtcyn=$(tput setaf 6) # Cyan
txtwht=$(tput setaf 7) # White

echo "
${txtred}
__     __          _____ _ _       
\ \   / /         / ____| (_)      
 \ \_/ /__  _   _| |    | |_ _ __  
  \   / _ \| | | | |    | | | '_ \ 
   | | (_) | |_| | |____| | | |_) |
   |_|\___/ \__,_|\_____|_|_| .__/ 
                            | |    
                            |_|    
${txtrst} 
"
echo "${txtylw}[*] Installing requirements for YouClip.${txtrst}"
echo "${txtblu}[1] Pip Packages:
 -> DateTime
 -> eel
 -> youtube-dl
 -> moviepy
${txtrst}"
 
pip3 install datetime
pip3 install eel
pip3 install youtube_dl
pip3 install moviepy

echo "${txtgrn}[SUCCESS] All pip packages are installed on your system.${txtrst}"
echo " "
echo "[2]${txtblu} Installing FFMPEG${txtrst}"
sudo apt-get install ffmpeg
echo "${txtgrn}[SUCCESS] FFMPEG is installed on your system."
echo "${txtgrn}[FIN] Now you should be able to use YouClip, have fun!${txtrst}"
