from flask import Flask
from pytrends.request import TrendReq
import io
import base64
import matplotlib.pyplot as plt


pytrends = TrendReq(hl='en-US', tz=360)

app = Flask(__name__)

    
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
    return prefix_google + "Hello World"


@app.route('/trend', methods=["GET"])
def trend():
    kw_list = ["chatGPT","dall e"]
    timeframe="2022-10-01 2023-01-01"
    pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='', gprop='')

    df = pytrends.interest_over_time()

    if all(df.isPartial == False):
        del df['isPartial']
    fig, ax = plt.subplots()
    for col in kw_list :
        df[col].plot.line(ax=ax)

    encoded = fig_to_base64(fig)
    my_html = '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))

    return my_html


def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())


