# Exercise 9.13 - From Collections - Ordered Dictionary

from collections import OrderedDict

glossary = OrderedDict()

glossary["BaaS"] = "Backup as a Service"
glossary["DRaaS"] = "Disaster Recovery as a Service"
glossary["SQL"] = "Database Engine"
glossary["EC2"] = "Elastic Cloud Computing"
glossary["IaaS"] = "Infrastructure as a Service"
glossary["AD"] = "Active Directory Services"

print("Ordered Dictionary Module - MAINTAINS ORDER")
for term in glossary:
    print(term)


glossary2 = {}
glossary2["BaaS"] = "Backup as a Service"
glossary2["DRaaS"] = "Disaster Recovery as a Service"
glossary2["SQL"] = "Database Engine"
glossary2["EC2"] = "Elastic Cloud Computing"
glossary2["IaaS"] = "Infrastructure as a Service"
glossary2["AD"] = "Active Directory Services"

print("\nStandard Python Dictionary - DOES NOT MAINTAIN ORDER")
for term in glossary2:
    print(term)
