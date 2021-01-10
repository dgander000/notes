# config-and-setup
repo for configuration and setup   

### install git  
```  
sudo apt install git   
```   

### install gnome tweak tool
```   
sudo apt install gnome-tweak-tool   
```

### install dash to dock   
Determine GNOME version   
- Open the Activities overview and start typing About.    
- Click on About to open the panel.  

https://micheleg.github.io/dash-to-dock/download.html     
copy dash-to-dock@micxgx.gmail.com inside ~/.local/share/gnome-shell/extensions/    
shell reload: Alt+F2 r    

### themes    
https://www.opendesktop.org/p/1284047/    
https://www.opendesktop.org/p/1297351    
Extract the zip file to the themes directory i.e. /usr/share/themes/ or ~/.themes/ (create it if necessary).     
Extract to your desktop environment, most commonly ~/.local/share/icons/ or /home/your_user/share/icons/    
In /usr/share/themes/Flat-Remix-GTK-Red-Dark/gtk-3.0/gtk.css change:
all #d41919 colors to #ac3939   
background-color: #d41919;    

change white to #C0C0C0

### firefox   
userChrome.css  
store to /chrome in firefox profile directory  
to find profile directory go to Help->Troubleshooting Information->Profile Directory   

if style sheet not being used:    
In address bar go to about:config    
Search for toolkit.legacyUserProfileCustomizations.stylesheets   
Toggle the preference    

### Anaconda  
https://www.anaconda.com/distribution/#download-section   

### Atom
https://atom.io/   
install packages:  
Edit -> Preferences -> Install (search for autocomplete-python (packages))    
Edit -> Preferences -> Install (search for platformio-ide-terminal (packages))  
Edit -> Preferences -> Install (search for remote-ftp (packages))  
Edit -> Preferences -> Install (search for atom-material-ui (themes))     




