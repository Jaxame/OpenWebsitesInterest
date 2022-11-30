# OpenWebsitesInterest

Execute in your prompt this activate_open_website.sh bash script after making your .sh file executable : 
```linux
# Make your file executable
chmod +x activate_open_website.sh
# Execute this main bash script with your goal in argument
./activate_open_website.sh courses
```  
Or use this command to open websites of your choice (in Goal, first column of your file.txt containing your favourite websites) :
```linux
python3 open_website.py -p /home/jacky/projects/OpenWebsitesInterest/ -f list_websites.txt -c courses
```
Here I want to open websites included in my file. I can only open those whose name in the first column matches.