
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, request
from csv import reader

contents = []
input_file = open("a2_input.csv","r")
for row in reader(input_file):
	contents = contents + [row]

def htmlify(bgcolor,title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <style>
                    table{
                        background-color:%s;
                    }
                </style>
                <meta charset="utf-8" />
                <title>%s</title>
		<link rel="stylesheet" href="static/style.css"/>
            </head>
            <body>
	      
 	           %s
	      
            </body>
        </html>

    """ % (bgcolor,title,text)
    return page
def staticFiles(filePath):
    return static_file(filePath,root='.')

def index():
    options="""
<form action="/show" method="POST">
<fieldset class="cities">
    <legend>Select Cities you want to see that's population</legend>
<select name="city" size="10" multiple>;
"""

    a = 0
    for rows in contents:
        if a==0 or a>81:
            a+=1
            continue
        opt="""<option value=%d>%s</option>""" % (a,rows[0])
        options+=opt
        a+=1
    options+="""</select><br/>
    You can choose multiple pressing ctrl</fieldset><br/>
    <fieldset class="color">
    <legend>Select table background color</legend>
    <div class="clrdiv" id="left">
    <input type="radio" name="bgcolor" value="white" checked/>white<br/>
    <input type="radio" name="bgcolor" value="blue"/>blue<br/>
    <input type="radio" name="bgcolor" value="green"/>green<br/>
    </div>
    <div class="clrdiv" id="center"> 
    <input type="radio" name="bgcolor" value="red"/>red<br/>
    <input type="radio" name="bgcolor" value="yellow"/>yellow<br/>
    <input type="radio" name="bgcolor" value="grey"/>grey<br/>
    </div>
    <div class="clrdiv" id="right"> 
    <input type="radio" name="bgcolor" value="pink"/>pink<br/>
    <input type="radio" name="bgcolor" value="orange"/>orange<br/>
    <input type="radio" name="bgcolor" value="purple"/>purple<br/>
    </div>
    </fieldset>
    <br/>
    <input type="checkbox" name="total" value="show"/>Show total population<br/>
<input type="submit" value="test" />
</form>
"""
    return htmlify("white","Populations",options)

def show():
    cities=request.POST.getlist('city')
    cont="""<table>
    <tr><th>İl</th><th>2000</th><th>2001</th><th>2002</th><th>2003</th><th>2004</th><th>2005</th><th>2006</th><th>2007</th><th>2008</th><th>2009</th><th>2010</th></tr>
    %s
    </table>"""
    cityRow=""
    for city in cities:
        cityRow+="<tr>"
        for columns in contents[int(city)]:
            cityRow+="<td>%s</td>"%columns
        cityRow+"</tr>"
    cont=cont%cityRow
    return htmlify(request.POST.get("bgcolor"),"Populations",cont)

route('/', 'GET', index)
route('/static/<filePath>','GET', staticFiles)
route('/show', 'POST', show)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

