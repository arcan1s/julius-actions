#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-

import os, sys


try:
    vocab_file = sys.argv[1]
except:
    vocab_file = os.path.abspath("julius-actions.conf")


def create_vocab(vocab_file):
    """function that reads input file"""
    if not os.path.exists(vocab_file):
        print "File doesn't exist"
        sys.exit(1)
    vocabulary = {}
    with open(vocab_file, "r") as vocab:
        for line in vocab:
            vocabulary[line.split("=")[0]] = line.split("=")[1]
    return vocabulary


vocabulary = create_vocab(vocab_file)
while True:
    line = sys.stdin.readline()
    if line == '':
        break
    elif (line.find("sentence1:") > -1):
        command = line.split("<s> ")[1].split(" </s>")[0]
        command_found = False
        for phrase in vocabulary.keys():
            if (command == phrase):
                os.system(vocabulary[phrase])
                command_found = True
                break
        if not command_found:
            print "Command not found"
