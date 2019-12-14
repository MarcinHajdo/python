from xml.dom import minidom

doc = minidom.parse("example.xml")

name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
doc.getElementsByTagName("nickname")[0].childNodes[0].nodeValue = "XXX"
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))

file = open("filename.xml","w")
xml = doc.toxml()
file.write(xml)
