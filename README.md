##Rasberry Pi Garage Door Opener

Clone https://github.com/joan2937/pigpio
make
make install

Create/copy init.d script

Install python
Install lighttpd
Configure python:

server.modules              = (
#                                       "mod_simple_vhost",
#                                       "mod_evhost",
#                                       "mod_userdir",
                                         "mod_cgi",
#                                       "mod_compress"
                                       )

cgi.assign =(

                      ".pl"  => "/usr/bin/perl",
                      ".cgi" => "/usr/bin/perl",
                      ".py"  => "C:/Python26/python.exe"

                    )


