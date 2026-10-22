print("""
Task 2 - Linux Command Practice
Run these commands in a Linux terminal. Use the practice folder for file operations.

1. pwd - Display the current directory
   pwd

2. mkdir - Create a practice directory
   mkdir -p ~/linux_practice

3. cd - Change directory
   cd ~/linux_practice

4. ls - List files, including hidden files and details
   ls -la

5. touch - Create an empty file
   touch notes.txt

6. Redirection - Write, append and read input
   echo "First line" > notes.txt
   echo "Second line" >> notes.txt
   cat < notes.txt
   ls missing_file 2> errors.txt

7. cat - Display or combine files
   cat notes.txt
   cat notes.txt errors.txt > combined.txt

8. Reading - Read keyboard input into a variable
   read -r -p "Enter your name: " name
   echo "Hello, $name"

9. more - Read a file one screen at a time
   more notes.txt
   Press Space for the next screen or q to quit.

10. less - Browse a file forward and backward
    less notes.txt
    Use the arrow keys to scroll and q to quit.

11. head - Display the first lines of a file
    head -n 2 notes.txt

12. cp - Copy a file
    cp notes.txt notes_copy.txt

13. mv - Move or rename a file
    mv notes_copy.txt renamed_notes.txt

14. file - Identify a file's type
    file notes.txt

15. rm - Delete a file
    rm renamed_notes.txt

16. rmdir - Remove an empty directory
    mkdir empty_folder
    rmdir empty_folder

17. sudo - Run a command with administrator privileges
    sudo -l
    This lists the commands your account is allowed to run through sudo.

18. man - Open a command's manual
    man ls
    Press q to exit the manual.

19. alias - Create a command shortcut for this shell session
    alias ll='ls -la'
    ll

20. nano - Edit a text file
    nano notes.txt
    Press Ctrl+O, then Enter to save; press Ctrl+X to exit.

21. bash - Run a script with Bash
    echo 'echo "Hello from a shell script"' > hello.sh
    bash hello.sh

22. sh - Run a portable shell script
    sh hello.sh

23. chmod - Change file permissions
    chmod u+x hello.sh
    ls -l hello.sh

24. ps - Display running processes
    ps aux

25. kill - Send a signal to a process
    sleep 300 &
    practice_pid=$!
    ps -p "$practice_pid"
    kill "$practice_pid"
    This terminates the sleep process started for this exercise.

26. dpkg - Inspect packages on Debian or Ubuntu
    dpkg -l
    dpkg -s bash
    To install a downloaded local .deb package on Debian or Ubuntu:
    sudo dpkg -i ./package.deb
    Replace package.deb with the actual package filename.

27. shutdown - Schedule a system shutdown
    sudo shutdown -h +10
    Cancel the scheduled shutdown with:
    sudo shutdown -c
    Run this exercise only when you intend to schedule a shutdown.

28. Restart - Reboot the computer
    sudo reboot
    This restarts the computer immediately; save your work first.

Running this Python file displays the examples. It does not execute shell commands.
""")
