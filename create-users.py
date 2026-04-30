#!/usr/bin/python3

# INET4031
# Evan S
# 4/20/26
# Date Last Modified

#REPLACE THIS COMMENT - identify what each of these imports is for.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        #REPLACE THIS COMMENT - this "regular expression" is searching for the presence of a character - what is it and why?
        #Check if line starts with # (skip it if so)
        match = re.match("^#",line)

        ## Strip the newline and split the line on : into a list of fields

        fields = line.strip().split(':')

        #Skip if line is commented out or doesn't have all 5 fields
        if match or len(fields) != 5:
            continue

        #Pull out username, password, and build the GECOS string from first + last name
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split the 5th field into a list of groups (handles users in multiple groups)

        groups = fields[4].split(',')

	# Status message

        print("==> Creating account for %s..." % (username))
	# Build the adduser command string
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

# Print to see the command, run it for real (commented out = dry run)

        print(cmd)
        os.system(cmd)

	# Status message

       print("==> Setting the password for %s..." % (username))
	# Build the passwd command (echoes the password twice into passwd)

        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

	
        print(cmd)
        os.system(cmd)

        for group in groups:
	    # Skip the assignment if the group field is just "-" (means no groups)

            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
