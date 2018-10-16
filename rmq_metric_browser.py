#!/usr/bin/env python

import urllib2
import base64
import json
import argparse
import time

class RabbitmqApiReader:
    def __init__(self, username, password, servers):
        self.username = username
        self.password = password
        self.servers = servers
        self.dictVals = {}

    def makeRequest(self, baseurl):
        request = urllib2.Request(baseurl)
        base64string = base64.b64encode('%s:%s' % (self.username,self.password))
        request.add_header("Authorization", "Basic %s" % base64string)
        self.result = json.load(urllib2.urlopen(request))
        self.servername = server.replace(".prod.walmart.com", "")
        self.timenow = int(time.time())
        return self.result

    def parseMsgStats(self, target):
        cmdlist = []
        if 'overview' in target:
            path = 'overview'
            self.dictVals['node'] = self.result.get('node')
            self.dictVals['messages'] = self.result.get('queue_totals')['messages']
            self.dictVals['messages_ready'] = self.result.get('queue_totals')['messages_ready']
            self.dictVals['messages_unacknowledged'] = self.result.get('queue_totals')['messages_unacknowledged']
        elif 'keepalives' in target:
            path = 'keepalives'
            self.dictVals['messages'] = self.result.get('messages')
            self.dictVals['messages_ready'] = self.result.get('messages_ready')
            self.dictVals['messages_unacknowledged'] = self.result.get('messages_unacknowledged')
        elif 'results' in target:
            path = 'results'
            self.dictVals['messages'] = self.result.get('messages')
            self.dictVals['messages_ready'] = self.result.get('messages_ready')
            self.dictVals['messages_unacknowledged'] = self.result.get('messages_unacknowledged')
        cmdlist.append("echo \"sensu.{0}.rabbitmq.{1}.messages {2} {3}".format(self.servername, path, r1.dictVals.get('messages'), self.timenow))
        cmdlist.append("echo \"sensu.{0}.rabbitmq.{1}.messages_ready {2} {3}".format(self.servername, path, r1.dictVals.get('messages_ready'), self.timenow))
        cmdlist.append("echo \"sensu.{0}.rabbitmq.{1}.messages_unacknowledged {2} {3}".format(self.servername, path, r1.dictVals.get('messages_unacknowledged'), self.timenow))
        print(cmdlist)
        return

    def getMemory(self):
        cmdlist = []
        mem_used = self.result.get('mem_used')
        mem_limit = self.result.get('mem_limit')
        divisor = 1024.0 * 1024 * 1024
        self.dictVals['mem_used'] = "%.1f" % float(mem_used/divisor)
        self.dictVals['mem_limit'] = "%.0f" % float(mem_limit/divisor)
        servername = server.replace(".prod.walmart.com", "")
        timenow = int(time.time())
        cmdlist.append("echo \"sensu.{0}.rabbitmq.memlimit {1} {2}".format(self.servername, r1.dictVals.get('mem_limit'), self.timenow))
        cmdlist.append("echo \"sensu.{0}.rabbitmq.memused {1} {2}".format(self.servername, r1.dictVals.get('mem_used'), self.timenow))
        print(cmdlist)
        return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True, help='RMQ username')
    parser.add_argument('-p', '--password', required=True, help='RMQ password')
    parser.add_argument('-s', '--servers', type=str, required=True, help='RMQ servers')
    args = parser.parse_args()

    targets = ['overview', 'queues/%2Fsensu/results', 'queues/%2Fsensu/keepalives']
    for server in args.servers.split(','):
        baseurl = "http://{0}:15672/api/".format(server)
        print(server)

        for target in targets:
            r1 = RabbitmqApiReader(args.username, args.password, server)
            r1.makeRequest(baseurl + target)
            if 'overview' in target:
                r1.parseMsgStats(target)
                r1.makeRequest(baseurl + 'nodes/' + r1.dictVals['node'])
                r1.getMemory()
            else:
                r1.parseMsgStats(target)
        del r1
