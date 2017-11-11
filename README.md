# logs_analysis_udacity
The 3rd projects made as a part of Udacity Full Stack Web Development Nanodegree
# Required software
Vagrant and VirtualBox are needed to be installed before running the program to provide Linux environment. In order to install Vagrant go to their website: https://www.vagrantup.com/, and VirtualBox - https://www.virtualbox.org/. If you face some problems during installation of Vagrant, you can find answers either at Stack OverFlow https://stackoverflow.com/search?q=vagrant or in the GitHub repo of Vagrant itself: https://github.com/hashicorp/vagrant. 
Also, installed Python is required. https://www.python.org/downloads/
# How to start
* After the installation, create your Virtual Machine by running in command line 
'vagrant up'

* Enter  your Virtual Machine after the previous command by 
'''
vagrant ssh
'''
* [Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

Unzip the file and put newsdata.sql into your vagrant directory
* Download the data to your VM using 
'''
psql -d news -f newsdata.sql
'''
* Connect to your DB using: 
 psql -d news
