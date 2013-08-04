#-*-coding: utf-8-*-

from xml.dom.expatbuilder import parseString

__author__ = 'hzengin'

import re
import urllib.request
import os
from Movie import *
from xml.dom.minidom import parse


class NameFinder:
    texts=[]
    def __init__(self):
        toDelete = open("toDelete","r")
        data=toDelete.read()
        for satir in data.splitlines():
            self.texts.append(satir)


    def stripName(self,dirname):
        text=dirname
        text=self.stripBrackets(text)
        text=self.char2space(text)
        text=self.stripYears(text)
        text=self.stripLabels(text)
        text=self.spaceStrip(text)
        text=self.text2url(text)
        print(text)
        return text

    def FindTitle(self,dirname):
        name = self.stripName(dirname)
        return self._searchTitles(name)

    def stripLabels(self,dirname):
        str=dirname
        for text in self.texts:
            str=str.replace(text,"")
        return str


    def stripBrackets(self,dirname):
        result = re.sub("\[.+\]"," ",dirname)
        result = re.sub("\(.+\)"," ",result)
        result = re.sub("\{.+\}"," ",result)

        return result


    def char2space(self,dirname):
        result=dirname.replace("."," ")
        result=result.replace("_"," ");
        result = result.replace("-"," ")
        return result


    def stripYears(self,dirname):
        result = re.sub("\\b\d\d\d\d\\b","",dirname)
        return result

    def text2url(self,text):
        text = text.replace("ş","s")
        text = text.replace("ç","c")
        text = text.replace("ğ","g")
        text = text.replace("ı","i")
        text = text.replace("ü","u")
        text = text.replace("ö","o")
        text = text.replace("Ş","S")
        text = text.replace("Ç","C")
        text = text.replace("Ğ","G")
        text = text.replace("İ","I")
        text = text.replace("Ü","U")
        text = text.replace("Ö","O")
        return text.replace(" ","+")

    def spaceStrip(self,text):
        text = re.sub(" +",' ',text)
        text = text.strip()
        return text

    def _searchTitles(self,title,limit="1",iteration=0):
        if(title.__len__()<2):
            return ""
        req = urllib.request.Request("http://mymovieapi.com/?type=xml&plot=none&episode=0&yg=0&mt=M&lang=en-US&offset=&aka=simple&release=simple&business=0&tech=0&title="+title+"&limit="+limit,headers={'User-Agent' : ""})
        con = urllib.request.urlopen(req)
        result=con.read()
        i=0
        dom = parseString(result)
        for node in dom.getElementsByTagName("IMDBDocumentList"):
            for node2 in node.getElementsByTagName("title"):
                movie=Movie()
                movie.title=node.getElementsByTagName("title")[i].firstChild.nodeValue
                movie.id=node.getElementsByTagName("imdb_id")[i].firstChild.nodeValue
                movie.rating=node.getElementsByTagName("rating")[i].firstChild.nodeValue
                movie.year=node.getElementsByTagName("year")[i].firstChild.nodeValue
                sonuc=movie
                i=i+1
                return sonuc
            #success
        return self.titleManipulateRight(title,limit,iteration+1)

    def titleManipulateRight(self,title,limit,iteration):
        if(iteration>2):
                return ""
        title=title.rsplit('+',1)[0]
        return self._searchTitles(title,limit,iteration+1)


def sub_dirs(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
