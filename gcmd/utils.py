# -*- coding: utf-8 -*-

import sys
import os.path
from optparse import OptionParser


def parsing():
    parser = OptionParser()
    parser.add_option("-d", "--destinator", action="store", dest="destinator",
        help="set a destination address to send e-mail, else send to default:\
             yourself mail")
    parser.add_option("-c", "--carboncopy", action="store", dest="cc",
        help="add a carboncopy destinator.")
    parser.add_option("-b", "--blindcarboncopy", action="store", dest="bcc",
        help="set a destination as blind cc.")
    parser.add_option("-a", "--attachpath", action="store", dest="attach",
        help="Attach  a file to email.")
    parser.add_option("-m", "--message", action="store", dest="message",
        help="The message that you want to send.")
    parser.add_option("-u", "--usermail", action="store", dest="usermail",
        help="Set up your user email of Gmail here. Neecery set in the first \
                time that use this  program.")
    parser.add_option("-s", "--subject", action="store", dest="subject",
        help="The email's subject.")
    parser.add_option("-p", "--password", action="store", dest="password",
        help="User's password")

    (opts, args) = parser.parse_args()
    paramms = dict()

    file_path = os.path.join(os.environ.get('HOME'), '.mailuser')
    if opts.usermail is None:
        print("Please use -u to set a gmail user, eg.: -u jonhnydoo@gmail.com.")
        print("It is necessary just once.")
        sys.exit()
    else:
        paramms['user_email'] = opts.usermail

    if opts.subject is not None:
        paramms['sub'] = opts.subject
    else:
        paramms['sub'] = "No Subject"

    if opts.message is not None and opts.destinator is not None:
        paramms['msg'] = opts.message
        paramms['dest'] = opts.destinator
        paramms['cc'] = opts.cc
        paramms['bcc'] = opts.bcc

        if opts.attach is not None:
            paramms['attach'] = opts.attach
        else:
            paramms['attach'] = None
        paramms['passwd'] = opts.password

    else:
        print("Missing: message or destination argumentsare necessary!")
        print("To more information use: gmailcommandline -h")
        sys.exit()

    return paramms
