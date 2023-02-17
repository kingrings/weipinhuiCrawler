from xml.dom.minidom import parse
import xml.dom.minidom

file=xml.dom.minidom.parse("abstractExecution3.xml")
instance=file.getElementsByTagName("instance")
instance=instance.item(0)
sigEs=instance.getElementsByTagName("sig")
event=[]
for sigE in sigEs:
    if sigE.getAttribute("label")=="this/E":
        atomEs=sigE.getElementsByTagName("atom")
        for atomE in atomEs:
            event.append(atomE.getAttribute("label"))

def resolveAtom(field):
    tuples = field.getElementsByTagName("tuple")
    eventTemp=[]
    for tuple in tuples:
        atoms = tuple.getElementsByTagName("atom")
        str1 = atoms.item(0).getAttribute("label")
        str2 = atoms.item(1).getAttribute("label")
        if str1!=str2:
            temp = [str1,str2]
            eventTemp.append(temp)
    return eventTemp


def resolveRead(event):
    for rvalSub in range(len(eventRval)):
        rvalStrTemp=eventRval[rvalSub][0]+eventRval[rvalSub][1]
        if rvalStrTemp.find(event)>=0:
            ans=rvalStrTemp.replace(event,"")
            ans=ans.rstrip("0")
            return ans

def resolveWrite(event):
    for valueSub in range(len(eventValue)):
        valueStrTemp=eventValue[valueSub][0]+eventValue[valueSub][1]
        if valueStrTemp.find(event)>=0:
            ans=valueStrTemp.replace(event,"")
            ans=ans.rstrip("0")
            return ans

def resolveKey(strTemp):
    for keySub in range(len(eventKey)):
        keyStrTemp=eventKey[keySub][0]+eventKey[keySub][1]
        if keyStrTemp.find(strTemp)>=0:
            ans=keyStrTemp.replace(strTemp,"")
            ans=ans.rstrip("0")
            return ans

def selectPrint(linkData):
    if linkData in link_data_vis:
        if linkData in link_data_ar:
            return "vis ar"
        else :
            return "vis"
    elif linkData in link_data_ar:
        if linkData not in link_data_vis:
            return "ar"

def findKeyValue(start,end):
    estart=""
    eend=""
    for i in range(len(eventLast)):
        if eventLast[i].find(start)>=0:
            estart=eventLast[i]
            break
    for i in range(len(eventLast)):
        if eventLast[i].find(end)>=0:
            eend=eventLast[i]
            break
    return {"source":eend,"target":estart}

def findVisAr():
    for i in range(len(link_data_vis)):
        ld=link_data_vis[i]
        if ld in link_data_ar:
            link_data_vis_ar.append(ld)


def SessionColorInit():
    session={"0":"","1":"","2":"","3":""}
    for i in range(len(eventSession)):
        if "Session$0" in eventSession[i]:
            session["0"]=color[0]
        elif "Session$1" in eventSession[i]:
            session["1"]=color[1]
        elif "Session$2" in eventSession[i]:
            session["2"]=color[2]
        elif "Session$3" in eventSession[i]:
            session["3"]=color[3]
    return session

def selectColor(strTemp,session):
    ses=0
    for i in range(len(eventSession)):
        ele=eventSession[i][0].replace("$","")
        #print(ele)
        if strTemp.find(ele)>=0:
            ses=eventSession[i][1].replace("Session$","")
            #print(ses)
            break
    return session[ses]

def selectSession(strTemp):
    ses = 0
    for i in range(len(eventSession)):
        ele = eventSession[i][0].replace("$", "")
        # print(ele)
        if strTemp.find(ele) >= 0:
            ses = eventSession[i][1].replace("Session$", "")
            # print(ses)
            break
    return int(ses)



fields=instance.getElementsByTagName("field")
eventOp=[]
eventRval=[]
eventSo=[]
eventVis=[]
eventAr=[]
eventSession=[]
eventKey=[]
eventValue=[]

color=["#5470c6","#91cc75","#fac858","#ee6666"]
for field in fields:
    if field.getAttribute("label")=="op":
        eventOp=resolveAtom(field)
    elif field.getAttribute("label")=="rval":
        eventRval=resolveAtom(field)
    elif field.getAttribute("label")=="so":
        eventSo=resolveAtom(field)
    elif field.getAttribute("label")=="vis":
        eventVis=resolveAtom(field)
    elif field.getAttribute("label") == "ar":
        eventAr=resolveAtom(field)
    elif field.getAttribute("label") == "session":
        eventSession=resolveAtom(field)
    elif field.getAttribute("label")=="value":
        eventValue=resolveAtom(field)
    elif field.getAttribute("label") == "key":
        eventKey = resolveAtom(field)




from pyecharts.charts import Graph
from pyecharts import options as opts



graph1=Graph(init_opts=opts.InitOpts(width="1600px",height="1000px"))
node_data=[]
link_data_vis=[]
eventLast=[]
findVisAr()
session=SessionColorInit()
print(session)
categories=[{"name":"session0","symbol_size":20},
            {"name":"session1","symbol_size":20},
            {"name":"session2","symbol_size":20},
            {"name":"session3","symbol_size":20}]
print(categories)
for subList in range(len(eventOp)):
    strTemp=eventOp[subList][0]+":"+eventOp[subList][1]
    if strTemp.find("Read$0")>=0:
        event=strTemp.replace(":Read$0","")
        rval=resolveRead(event)
        key = resolveKey("Read$0")
        ans = "R(" + key + ")"
        str = strTemp.replace("Read$0", ans)
        strTemp=str+":"+rval
    elif strTemp.find("Read$1")>=0:
        event = strTemp.replace(":Read$1", "")
        rval = resolveRead(event)
        key = resolveKey("Read$1")
        ans = "R(" + key + ")"
        str = strTemp.replace("Read$1", ans)
        strTemp = str + ":" + rval
    elif strTemp.find("Write$0")>=0:
        rval = resolveWrite("Write$0")
        key = resolveKey("Write$0")
        ans = "W(" + key + ")"
        str = strTemp.replace("Write$0", ans)
        strTemp = str + ":" + rval
    elif strTemp.find("Write$1")>=0:
        rval = resolveWrite("Write$1")
        key=resolveKey("Write$1")
        ans="W("+key+")"
        str=strTemp.replace("Write$1",ans)
        strTemp = str + ":" + rval

    strTemp = strTemp.replace("$", "")
    print(strTemp)
    col=selectColor(strTemp,session)
    ses=selectSession(strTemp)
    #print(ses)
    node_data.append({"name":strTemp,"symbolSize": 60,"itemStyle":{"color":col},"category":ses})
    eventLast.append(strTemp)





for i in range(len(eventVis)):
    eTempStart=eventVis[i][0].replace("$","")
    eTempEnd=eventVis[i][1].replace("$","")
    #print(eTempStart,eTempEnd,range(len(eventVis)))
    link_data_vis.append(findKeyValue(eTempStart,eTempEnd))


link_data_ar=[]

for i in range(len(eventAr)):
    eTempStart=eventAr[i][0].replace("$","")
    eTempEnd=eventAr[i][1].replace("$","")
    #print(eTempStart,eTempEnd)
    link_data_ar.append(findKeyValue(eTempStart,eTempEnd))

link_data_so=[]

for i in range(len(eventSo)):
    eTempStart = eventAr[i][0].replace("$", "")
    eTempEnd = eventAr[i][1].replace("$", "")
    # print(eTempStart,eTempEnd)
    link_data_so.append(findKeyValue(eTempStart, eTempEnd))




link_data_vis_ar=[]



print(link_data_vis_ar)

#.DataZoomOpts(range_start=50,range_end=100)


graph1.set_global_opts(title_opts=opts.TitleOpts(title="non-TransactionAbstractExecution"))
graph1.add("",node_data,link_data_ar,edge_length=100,repulsion=3000,edge_label=opts.LabelOpts(is_show=True,position="middle",font_size=16,formatter="ar"),
           linestyle_opts=opts.LineStyleOpts(type_="dashed"),edge_symbol=['arrow'],categories=categories)
graph1.add("",node_data,link_data_so,edge_length=100,repulsion=3000,edge_label=opts.LabelOpts(is_show=True,position="middle",font_size=16,formatter="so"),
            linestyle_opts=opts.LineStyleOpts(type_="solid"),edge_symbol=['arrow'],categories=categories)
graph1.add("",node_data,link_data_vis,edge_length=100,repulsion=3000,edge_label=opts.LabelOpts(is_show=True,position="middle",font_size=16,formatter="vis"),
          linestyle_opts=opts.LineStyleOpts(type_="solid"),edge_symbol=['arrow'],categories=categories)
graph1.set_global_opts(legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"))
graph1.render("./g2.html")







print(eventOp)
print(eventRval)
print(eventKey)
print(eventValue)
print(eventVis)
print(eventAr)
print(eventLast)
print(eventSession)
print(link_data_vis)
print(link_data_so)



