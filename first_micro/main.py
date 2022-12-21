from flask import Flask, render_template
import logging
import sys
import requests

app = Flask(__name__)


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-KC97QE5JFN"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', ' G-KC97QE5JFN');
    </script>
    """
    
    suffixe_google= """
    <button onClick="ga('send', 'event', 'button', 'click', 'Label');">Click</button>
    """
    return  prefix_google  + "Hello World" + suffixe_google

@app.route('/Logger', methods=["GET"])
def logger():
    page="""
    <script> console.log('aie')</script>
    """
    return 'console'+page

## textbox
@app.route('/textbox')
def home():
    page="""
    <head>
    <meta charset="UTF-8">
    <title>
        Textbox
    </title>
</head>
<body>
<p>
            this is a Textbox
        </p>
    <form name='form' method="get">
        
        <input name= "t1"  placeholder="Text">
        <input type=submit>
    </form>
    
</body>
    """
    return page


@app.route('/google',methods=["GET"])
def request_google():
    req =requests.get("https://analytics.google.com/analytics/web/#/p344224094/reports/reportinghub?params=_u..nav%3Dmaui")

    return req.text


