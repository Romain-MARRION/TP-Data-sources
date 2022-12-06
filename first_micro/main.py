from flask import Flask
import logging
import sys

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






