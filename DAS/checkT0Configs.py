#!/usr/bin/env python

import sys,os,urllib2,json,getopt

run = None
# baseurl = 'https://cmsweb.cern.ch/'
baseurl = 'https://cmsweb-testbed.cern.ch/'

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["run="])
except getopt.GetoptError:
    print 'Please specify run: --run=132440'
    sys.exit(2)

# check command line parameter
for opt, arg in opts :
    if opt == "--run" :
        run = arg

if run == None:
    print 'Current configuration!'
    print ''

print ''
print 'EXPRESS'
print ''

if run == None:
    url = baseurl + 'tier0/express_config?run=&stream=Express'
else :
    url = baseurl + 'tier0/express_config?run='+run+'&stream=Express'

req = urllib2.Request(url)
req.add_header("User-Agent","ConditionOfflineDropBox/1.0 python/%d.%d.%d" % sys.version_info[:3])
req.add_header("Accept","application/json")
jsonCall = urllib2.urlopen(req)
jsonText = jsonCall.read()
result = json.loads(jsonText)

for entry in result:
    print 'run:',entry['run_id']
    print 'stream:',entry['stream']
    print 'proc_version:',entry['proc_version']
    print 'global_tag:',entry['global_tag']
    print 'scenario:',entry['scenario']
    print 'config_url:',entry['config_url']
    print ''

print 'Prompt'
print ''

if run == None:
    url = baseurl + 'tier0/reco_config?run=&dataset='
else :
    url = baseurl + 'tier0/reco_config?run='+run+'&dataset='

req = urllib2.Request(url)
req.add_header("User-Agent","ConditionOfflineDropBox/1.0 python/%d.%d.%d" % sys.version_info[:3])
req.add_header("Accept","application/json")
jsonCall = urllib2.urlopen(req)
jsonText = jsonCall.read()
result = json.loads(jsonText)

for entry in result:
    if entry['cmssw_version'] != 'Undefined':
        print 'run:',entry['run']
        print 'primary_dataset:',entry['primary_dataset']
        print 'proc_version:',entry['proc_version']
        print 'cmssw_version:',entry['cmssw_version']
        print 'global_tag:',entry['global_tag']
        print 'scenario:',entry['scenario']
        print 'config_url:',entry['config_url']
        print ''
