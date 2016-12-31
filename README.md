# **Simplefc**

### A simple command-line flash card interface.
### **Description**

Beyond grade school, rote memorization vanishes from many of our 
lives, but it happens to be a very valuable tool for retention. 
Train yourself to remember new words, friends' birthdays, or 
important political figures with simplefc. When you happen upon a 
factoid, add it to a simplefc flash card set, then practice nightly
or weekly. Practice by term, definition, or both. You can even hone
your study sessions according to how well you've performed on each 
entry.

### **Contents**
1. Requirements
2. Installation
3. Usage
4. Notes
5. Contact the author

---
### **1. Requirements**
Python 3.2 or later
Tested on Ubuntu 14.04

---
### **2. Installation**
+ `pip install simplefc`

+ Navigate to [https://github.com/vlahm/linux_utils/tree/master/Chime/dist](https://github.com/vlahm/linux_utils/tree/master/Chime/dist)
2. Right-click `chime-1.0.0.tar.gz` and save link to desired location.
3. Navigate to the folder where you saved the tarball, then execute:

  ```
  tar -xzvf chime-1.0.0.tar.gz  
  pip install chime-1.0.0/  
  ```
  (The slash is important in the above command.)

---
### **3. Usage**
Chime takes two arguments: a duration and an error message.  The duration is specified as a single string containing a number followed by ‘h’, ‘m’, or ‘s’, for ‘hours’, ‘minutes’, or ‘seconds’. You can also combine units, as in '1h20m3s'. The error message is a separate string, which is returned when the time is up.

#### 1. Basic (using `python` command from shell)
`python path/to/chime.py <duration> <reminder message>`  

Note that this usage may return benign error messages.
##### **_Examples:_**
`python chime.py 2m45s`  
`python ~/chime.py 1h5m 'get laundry'`
#### 2. Run from anywhere with alias
Add the following function to your `.bashrc` file:
```bash
function chime { 
    python path/to/chime.py $1 $2
}
```
Then execute from any terminal with, e.g. `chime 1h15m 'start dinner'`.
#### 3. Run from anywhere as daemon (disconnect from shell)
For full functionality (and suppression of potential noncritical error messages),
it is best to run Chime as a daemon process, which
places it in the "background" and allows you to close the terminal that
spawned it without terminating its process.

Add the following function to your `.bashrc` file.
You'll need to update the filepath for `chime.py`. You can put the output file
`nohup.py` in the same directory as `chime.py` or anywhere you like. Just note
that it's referred to twice in this function definition, and both will have to be
modified.
```bash
function chime { 
    nohup python example/path/chime.py $1 $2 > \
    example/path/nohup.out 2>/dev/null & disown $!
    sleep 1s
    tail --lines=1 example/path/nohup.out
}    
```
Then execute from any terminal with, e.g. `chime 1h15m 'start dinner'`.  
It will now be safe to exit the terminal.

---
### **4. Contact the author**
Mike Vlah: 
+ vlahm13@gmail[dot]com
+ [linkedin.com/in/michaelvlah](linkedin.com/in/michaelvlah)

