from flask import Flask, render_template_string

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    with open('./index.html', 'r') as file:
        html_content = file.read()
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)
