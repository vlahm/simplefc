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
4. Planned Updates
5. Contact the author

---
### **1. Requirements**
Python 3.2 or later
Tested on Ubuntu 14.04

---
### **2. Installation**
1. Open terminal/command prompt and enter: `pip install simplefc`. Must have pip installed.
2. Install from source tarball:
  1.Navigate to [https://github.com/vlahm/simplefc/tree/master/dist](https://github.com/vlahm/simplefc/tree/master/dist).
  2. Right-click `simplefc-1.0.3.tar.gz` and save link to desired location.
  3. Navigate to the folder where you saved the tarball, then execute:

  ```
  tar -xzvf simplefc-1.0.3.tar.gz #just right-click and extract if on Windows
  pip install simplefc-1.0.3/  
  ```
  (The slash is important in the above command.)
  
---
### **3. Usage**
Flash cards are stored as "entries" and are grouped in "sets".

```
Usage:
  simplefc [-h | --help]
  simplefc [-v | --version]
  simplefc create_set <setname>
  simplefc add_entry <setname> (-M <entry>... | -F <file>...)
  simplefc study [-tdbamfsr] <setname>
  simplefc view_set <setname>
  simplefc view_archive <setname>
  simplefc unarchive <setname> <ID>...
  simplefc delete_entry <setname> <ID>...
  simplefc list_sets
  simplefc delete_set <setname>
  simplefc reset_data <setname>

Arguments:
  <setname>      The name of a simplefc flashcard set. Cannot 
                 contain spaces or special characters. Must begin 
                 with a letter.
  <entry>        An entry of the form 'term;;definition'.
  <file>         A file containing unquoted entries of the 
                 above form. Each entry must have its own line.
  <ID>           The identification number of an entry.

Options:
  -h --help      Show this page.
  -v --version   Show version.
  -M             Add entries manually.
  -F             Add entries from a file.
  -t             Study terms.
  -d             Study definitions.
  -b             Study with randomized terms and definitions.
  -a             'All' - Include all entries.
  -m             'Many' - Exclude easy entries (those with 
                 correct:incorrect ratio >= 2). 
  -f             'Few' - Include only hard entries (those with 
                 correct:incorrect ratio <= 0.75).
  -s             Go through entries sequentially (in the order 
                 they were recorded).
  -r             Go through entries in random order.


Examples:
  simplefc create_set 'biology_450_final'
  simplefc add_entry biology 450 final -I 'xanthophyll;;a yellow or brown carotenoid pigment found in plants' 'anthocyanin;;a red flavonoid pigment found in plants'
  simplefc study -bmr biology 450 final
  simplefc delete_entry biology_450_final 1 2 7 9
```

---
###**4. Planned Updates**
+ Commands for writing/reading flash card sets to/from .csv files
+ Better error handling. If you get cryptic, internal errors, and the answers aren't in the docs, open an issue on my Github. See below.

---
### **5. Contact the author**
Mike Vlah: 
+ vlahm13@gmail[dot]com
+ [https://github.com/vlahm](https://github.com/vlahm)
+ [linkedin.com/in/michaelvlah](linkedin.com/in/michaelvlah)

