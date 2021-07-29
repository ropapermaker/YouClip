#!/bin/bash


txtrst=$(tput sgr0) # Text reset
txtred=$(tput setaf 1) # Red
txtgrn=$(tput setaf 2) # Green
txtylw=$(tput setaf 3) # Yellow
txtblu=$(tput setaf 4) # Blue
txtpur=$(tput setaf 5) # Purple
txtcyn=$(tput setaf 6) # Cyan
txtwht=$(tput setaf 7) # White

declare -A osInfo;
osInfo[/etc/redhat-release]="yum install"
osInfo[/etc/arch-release]="pacman -S"
osInfo[/etc/gentoo-release]="emerge"
osInfo[/etc/debian_version]="apt-get install"

for f in ${!osInfo[@]}
do
    if [[ -f $f ]];then
        package_manager=${osInfo[$f]}
    fi
done

package="ffmpeg"

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
 
"
echo "[ IMPORTANT! ] THIS SCRIPT REQUIRES FOR YOU TO HAVE PYTHON3 WITH PIP INSTALLED,
IF YOU DON'T HAVE THOSE INSTALLED PLEASE INSTALL THEM AND PROCEED WITH THIS INSTALLATION${txtrst}"
echo "${txtylw}[*] Installing requirements for YouClip.${txtrst}"
echo "${txtblu}[1] Pip Packages:
 -> DateTime
 -> eel
 -> youtube-dl
 -> moviepy
${txtrst}"

# installing pip packages
(pip3 install datetime || echo "Could not install datetime") && \
(pip3 install eel || echo "Could not install eel") && \
(pip3 install youtube_dl || echo "Could not install youtube-dl") && \
(pip3 install moviepy || echo "Could not install moviepy")

echo "${txtgrn}[SUCCESS] All pip packages are installed on your system.${txtrst}"
echo " "
echo "[2]${txtblu} Installing FFMPEG${txtrst}"

sudo ${package_manager} ${package} || echo "Could not find OS type"

echo "${txtgrn}[SUCCESS] FFMPEG is installed on your system."
echo "${txtgrn}[FIN] Now you should be able to use YouClip, have fun!${txtrst}"