if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi

#31 vermelho
#32 verde
#30 cinza
#35 rosa

PS1='\[\e[40;05;31m\]▛▝▝▝▝▝\[\e[40;05;31m\][\[\e[40;05;35m\]\w\[\e[40;05;31m\]]\n\[\e[40;05;31m\]▙▄▄▃▂▁[\e[40;05;31m\][\[\e[40;05;30m\]\d\[\e[40;05;31m\]]\[\e[40;05;31m\]--\[\e[40;05;31m\][\[\e[40;05;34m\]\W\[\e[40;05;31m\]]\[\e[40;05;32m\]\$»»» '   
