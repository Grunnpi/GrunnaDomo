# Installation

Find a tutorial on the internet...

# Additional stuff

* For "old" Raspberry :
    * Switch to Buster Raspbian distribution
        * Google it !
        * something like : ``grep -rl stretch /etc/apt/ | sudo xargs sed -i 's/stretch/buster/g'``
        * then : ``sudo apt update && sudo apt dist-upgrade``
        * sometimes need also : ``sudo apt-get --fix-broken --fix-missing --assume-yes install``
        * at last reboot
    * Bit of cleanup
        * ``sudo apt autoremove``
    * openssl (for dtgbot https call to Telegram)
        * ``sudo apt-get install openssl libssl1.0.0 openssh-client openssh-server ssh``
* LUA 5.3
    * ``sudo apt-get install lua5.3``
* LUA "socket" module
    * ``sudo apt-get install lua-socket``
* LUA "sec" module
    * ``sudo apt-get install lua-sec``
* JSON lib for dtgbot missing in lua5.3
    * ``sudo sudo cp /usr/local/share/lua/5.2/JSON.lua /usr/share/lua/5.3/JSON.lua``
