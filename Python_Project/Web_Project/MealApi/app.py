from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

def get_meals(dt):
    p = {
        'Type' : 'json',
        'ATPT_OFCDC_SC_CODE' : 'J10',
        'SD_SCHUL_CODE' : '7530167',
        'MLSV_YMD' : dt
    }

    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'
    result = requests.get(url, params=p)

    try:
        if result.status_code == 200:
            meals = result.json()
            meal = meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        else:
            meal = ''
        return meal
    except:
        return ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        date = request.form['date']
        meal = get_meals(date)
        if meal == '':
            meal = '자료가 없습니다.'
        else:
            meal = meal.replace('<br/>', '\n')
        return render_template('index.html', meal=meal)
    else:
        today = datetime.today().strftime('%Y-%m-%d')
        meal = get_meals(today)
        if meal == '':
            meal = '자료가 없습니다.'
        else:
            meal = meal.replace('<br/>', '\n')
        return render_template('index.html', meal=meal)

if __name__ == '__main__':
    app.run(debug=True)
