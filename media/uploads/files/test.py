
admin = {
    "sysdescr": "ECS2100-28T",
    "sysobjectid": "1.3.6.1.4.1.259.10.1.43.104",
    "sysuptime": "25606482",
    "syscontact": "9876543210",
    "sysname": "EDGE CORE",
    "syslocation": "NOIDA",
    "interfaces": {
        "1": {
            "ifindex": "1",
            "inOctect": 2080970,
            "outOctect": 1553009,
            "inErr": 0,
            "name": "Ethernet Port on unit 1, port 1",
            "mtu": "1518",
            "speed": "1000000000",
            "mac": [
                "60",
                "44",
                "153",
                "200",
                "213",
                "1"
            ],
            "adminstatus": "up",
            "operstatus": "lowerLayerDown",
            "description": ""
        },
        "2": {
            "ifindex": "2",
            "inOctect": 2198972452,
            "outOctect": 375837382,
            "inErr": 0,
            "name": "Ethernet Port on unit 1, port 2",
            "mtu": "1518",
            "speed": "1000000000",
            "mac": [
                "60",
                "44",
                "153",
                "200",
                "213",
                "2"
            ],
            "adminstatus": "up",
            "operstatus": "up",
            "description": ""
        }
    },
    "all_ipv4_addresses": [
        "192.168.1.10"
    ]
}

def uptime(sec):
    import datetime
    return  datetime.datetime.fromtimestamp(int(sec) / 1000)

interfaces = admin["interfaces"]

# print(interfaces)
uptime = uptime(admin["sysuptime"])
print(uptime)

adminUp = 0
adminDown = 0
print("Index\tIn Octet\tOut Octet\tMac\tAdmin Status")
for i in interfaces:
    index = interfaces[i]["ifindex"]
    inO = interfaces[i]["inOctect"]
    out = interfaces[i]["outOctect"]
    mac = ":".join(interfaces[i]["mac"])
    adminstatus = interfaces[i]["adminstatus"]

    if (adminstatus == "up"):
        adminUp += 1
    else:
        adminDown += 1
    print(index,"\t", inO, out, mac, adminstatus)

print("Admin UP:", adminUp)
print("Admin Down:", adminDown)