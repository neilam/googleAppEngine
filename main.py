import webapp2

def checkText(inp):
        WORDLIST=["maverick","ranger","rocket","chicago","bear","wizard","seattle","atlanta","miami","austin","boston","pittsburgh","heat","saint","hawk","king"]
        array=inp.strip().split()
        output=""
        for word in array:
            tempword=word
            for newWord in WORDLIST:                
                if word.find(newWord) >=0:
                    while (tempword.find(newWord) >= 0):
                        tempword=tempword[0:tempword.find(newWord)]+tempword[tempword.find(newWord)+len(newWord):]
            if tempword=='':
                l=len(word)
                temp=""
                while(l>0):
                    temp+="*"
                    l-=1
                        
                output+=temp+" "
            else:
                output+=tempword+" "
        return output               

class MainHandler(webapp2.RequestHandler):

  def get(self):
    self.response.out.write(open("index.html").read())

  def post(self):
    input1 = self.request.get('input1')

    self.response.out.write("Processed Text: %s" % checkText(input1))

APP = webapp2.WSGIApplication([
    ('/.*', MainHandler),
], debug=True)
