from __future__ import print_function
import sys
import libvirt

connection = libvirt.open('qemu:///system')
print('\n')
print("Virtual Box Guest OS Name VM1")
print('\n')
domainName = 'vm1'


if connection == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
    
#domain = connection.lookupByID(2)
domain = connection.lookupByName(domainName)

if domain == None:
    print('Failed to find the domain '+domainName, file=sys.stderr)
    exit(1)

id = domain.ID()
if id == -1:
    print('The domain is not running so has no ID.')
     
CPUstats = domain.getCPUStats(True)

print('cpu_usage_time: '+str(CPUstats[0]['cpu_time']/1000000000))
print('system_usage_time: '+str(CPUstats[0]['system_time']/1000000000))
print('user_estimate_time: '+str(CPUstats[0]['user_time']/1000000000))

#connection.close()
print('\n')
print("=============================")
print('\n')
print("Virtual Box Guest OS Name VM2")
print('\n')
domainName = 'vm2'


if connection == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
    
#domain = connection.lookupByID(2)
domain = connection.lookupByName(domainName)

if domain == None:
    print('Failed to find the domain '+domainName, file=sys.stderr)
    exit(1)

id = domain.ID()
if id == -1:
    print('The domain is not running so has no ID.')
     
CPUstats = domain.getCPUStats(True)

print('cpu_usage_time: '+str(CPUstats[0]['cpu_time']/1000000000))
print('system_usage_time: '+str(CPUstats[0]['system_time']/1000000000))
print('user_estimate_time: '+str(CPUstats[0]['user_time']/1000000000))
print('\n')
connection.close()
exit(0)



#Referance: https://libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/libvirt_application_development_guide_using_python-Guest_Domains-Monitoring-vCPU.html
