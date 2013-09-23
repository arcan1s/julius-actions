#!/usr/bin/python2
# -*- coding: utf-8 -*-

import argparse, os, sys


def add_new(commands_act, commands_voca, actions):
    """function that add new julius actions to the file"""
    for com_voca in commands_voca:
        try:
            test = commands_act.keys().index(com_voca)
        except ValueError:
            print "Found a new phrase: '%s'" % (com_voca)
            commands_act[com_voca] = raw_input("Command for the phrase: ")
            with open(actions, "a") as actions_file:
                actions_file.write(com_voca + "=" + commands_act[com_voca] + "\n")
    return commands_act


def edit_all(commands_act, commands_voca, actions):
    """function that edit all julius actions"""
    commands = [com_act for com_act in commands_act.keys()]
    choise = "y"
    while (choise == "y"):
        for com_act in commands:
            print "%i. %s = %s" %(commands.index(com_act)+1, com_act, commands_act[com_act])
        choise = raw_input("Choose the command: ")
        try:
            num = int(choise)
            commands_act[commands[num-1]] = raw_input("Command for the phrase: ")
        except ValueError:
            print "Invalid number"
        choise = "q"
        while ((choise != "y") and (choise != "n")):
            choise = raw_input("Continue [y/n]? ")
    with open(actions, "w") as actions_file:
        for com_act in commands_act.keys():
            actions_file.write(com_act + "=" + commands_act[com_act] + "\n")
    commands_act = add_new(commands_act, commands_voca, actions)
    return commands_act


def find_actions(actions):
    """function that reads julius actions"""
    with open(actions, "r") as actions_file:
        commands_act = {line.split("=")[0]:line.split("=")[1][:-1] for line in actions_file if (line.find("#") == -1)}
    return commands_act


def find_commands(dfa_file):
    """function that reads julius vocabulary"""
    os.chdir(os.path.dirname(dfa_file))
    command = "generate -n 1024 " + os.path.basename(dfa_file).split(".dfa")[0] + " 2> /dev/null"
    with os.popen(command, "r") as gen:
        commands_voca = [line.split("<s> ")[1].split(" </s>")[0] for line in gen if (line.find("<s>") > -1)]
    return commands_voca


def find_dfa_file(config):
    """function that reads julius configuration file"""
    os.chdir(os.path.dirname(config))
    with open(config, "r") as config_file:
        for line in config_file:
            if (line[0] != '#') and (line.find("-dfa") > -1):
                dfa_file = os.path.abspath(line[5:])
    return dfa_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Edit actions for julius')
    parser.add_argument('-a', '--actions-file', dest = 'actions',
            help = 'file with julius actions',
            action = 'store', default = False)
    parser.add_argument('-c', '--config-file', dest = 'config',
            help = 'file with julius configurations',
            action = 'store', default = False)
    parser.add_argument('-e', '--edit-all', dest = 'edit_all',
            help = 'edit actions',
            action = 'store_true', default = False)
    args = parser.parse_args()
    
    if ((not args.actions) or (not args.config)):
        sys.exit(1)
    
    actions = os.path.abspath(os.path.expanduser(args.actions))
    config = os.path.abspath(os.path.expanduser(args.config))
    
    dfa_file = find_dfa_file(config)
    commands_act = find_actions(actions)
    commands_voca = find_commands(dfa_file)
    if (args.edit_all):
        commands_act = edit_all(commands_act, commands_voca, actions)
    else:
        commands_act = add_new(commands_act, commands_voca, actions)
