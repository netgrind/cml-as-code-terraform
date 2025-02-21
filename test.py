from genie.testbed import load
import sys

testbed = load('testbed.yaml')
device = testbed.devices["Router1"]
device.connect(learn_hostname = True)

test = device.execute("Ping 10.1.1.72")

if "!!" in test:
    print("Ping successful")
else:
    print("Ping unsucessful")
    sys.exit
