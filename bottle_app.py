
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file, request

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
		<link rel="stylesheet" href="static/style.css"/>
            </head>
            <body>
	      <div>
 	           %s
	      </div>
            </body>
        </html>

    """ % (title,text)
    return page
def staticFiles(filePath):
    return static_file(filePath,root='.')

def index():
    return htmlify("My lovely website",
"""
<form action="/show"method="POST">
<input type="text" name="city"/>
<input type="submit" value="test"/>
</form>
"""

)

def show():
    bbb=request.POST

    return bbb['city']

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

