#!/usr/bin/env python
# encoding: utf-8
import paramiko
import argparse


def cli_parse():
    parser = argparse.ArgumentParser("input your ssh information")
    parser.add_argument('-ip', dest='ip', type=str, default="127.0.0.1", help="ip address")
    parser.add_argument('-port', dest='port', type=int, default=22, help="ssh port")
    parser.add_argument('-user', dest='user', type=str, default="root", help="username")
    parser.add_argument('-password', dest='password', type=str, default="Hello=111!", help="ssh password")
    args = parser.parse_args()
    ssh_pars = dict()
    ssh_pars['ip'] = args.ip
    ssh_pars['port'] = args.port
    ssh_pars['user'] = args.user
    ssh_pars['password'] = args.password
    return ssh_pars


def ssh_cli(env, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(env['ip'], port=env['port'], username=env['user'], password=env['password'])
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read() if stdout.read() else stderr.read()
        result = result.decode()
        print(result)
        print("ssh %s OK\n" % env['ip'])
        ssh.close()
    except:
        print("ssh %s failed\n" % env['ip'])


if __name__ == "__main__":
    ssh_parameters = cli_parse()
    ssh_cli(ssh_parameters, "kubectl get pods")

