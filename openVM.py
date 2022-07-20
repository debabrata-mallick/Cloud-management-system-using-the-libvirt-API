import libvirt

#connect to hypervisor running on localhost
conn = libvirt.open('qemu:///system')

dom0 = conn.lookupByName('vm1')
dom0.create()
dom1 = conn.lookupByName('vm2')
dom1.create()

#Referance: https://stackoverflow.com/questions/12251881/kvm-api-to-start-virtual-machine#:~:text=Using%20libvirt%2C%20you%20will%20first,domain%20by%20calling%20virt%2Dinstall.&text=Once%20you%20create%20the%20domain,easier%20to%20manage%20the%20VM.&text=you%20can%20use%20the%20help,start%20option%20might%20help%20you.




