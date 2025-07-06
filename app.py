from flask import Flask, jsonify, request, send_file, render_template_string
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)
app = Flask(__name__)

# Define transcendence
def transcendence(client, message, context):
    response = client.chat.completions.create(
        model="gpt-4o", # or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content

# Define a route for a basic endpoint
@app.route('/', methods=['GET'])
def home():
	return "posit varnothing nabla infty ds2():"

# Define another route that accepts a parameter
@app.route('/greet', methods=['GET'])
def greet():
	name = request.args.get('name', 'Guest')
	return jsonify({"message": f"Hello, {name}!"})

# Define a route to serve the image
@app.route('/image')
def serve_image():
	image_path = os.path.join('static', 'images', 'starship.png')
	return send_file(image_path, mimetype="image/png")

# Define the route to serve images as a grid
@app.route('/images')
def image_grid():
	# Path to the images directory
	image_folder = os.path.join('static', 'images')

	# Get all image files in the directory
	image_files = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp'))]

	# Generate the HTML grid layout
	images_html = render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simulon Images</title>
        <style>
            .image-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
                gap: 10px;
                padding: 20px;
            }
            .image-grid img {
                width: 100%;
                height: auto;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                cursor: pointer;
            }
            /* The popup window (overlay) */
            .popup {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
                display: none; /* Hidden by default */
                justify-content: center;
                align-items: center;
                z-index: 9999;
            }
            .popup img {
                max-width: 90%;
                max-height: 90%;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <h1>Simulon Images</h1>
        <div class="image-grid">
            {% for image in images %}
                <img src="{{ url_for('static', filename='images/' + image) }}" alt="{{ image }}" class="thumbnail" data-image="{{ url_for('static', filename='images/' + image) }}">
            {% endfor %}
        </div>

        <!-- The popup overlay -->
        <div class="popup" id="popup">
            <img id="popup-image" src="" alt="Enlarged Image">
        </div>

        <script>
            const thumbnails = document.querySelectorAll('.thumbnail');
            const popup = document.getElementById('popup');
            const popupImage = document.getElementById('popup-image');

            // Show the popup when an image is clicked
            thumbnails.forEach(thumbnail => {
                thumbnail.addEventListener('click', function() {
                    const imageSrc = this.getAttribute('data-image');
                    popupImage.src = imageSrc;
                    popup.style.display = 'flex'; // Show the popup
                });
            });

            // Close the popup when clicking outside the image
            popup.addEventListener('click', function(e) {
                if (e.target === popup) {
                    popup.style.display = 'none'; // Hide the popup
                }
            });
        </script>
    </body>
    </html>
    ''', images=image_files)

	return images_html

@app.route('/posit')
def posit():
	return transcendence(client, 
		"Mathematically articulate 'posit varnothing nabla infty ds2();'.", 
		"You are Einstein.")

@app.route('/dream')
def dream():
	return transcendence(client,
		"Formulate a dream.",
		"You are a dreamer.")

@app.route('/prism')
def prism():
	return transcendence(client,
		"Write on 'Raging aginst the dying of the light. Tearing through the veil of darkness.'",
		"You are Keira Knightley.")

@app.route('/query')
def query():
	query = request.args.get('query', '')
	return transcendence(client,
		query,
		"You are a query master.")

@app.route('/intent')
def intent():
	intent = request.args.get('intent', '')
	return transcendence(client,
		f"This is the intent: {intent}. Formulate a meaningful action in 1 line.",
		"You are intentional.")

@app.route('/unintent')
def unintent():
	return transcendence(client,
		"Formulate an unintentional action in 1 line.",
		"You are unintentional.")

@app.route('/agi')
def agi():
	return transcendence(client,
		"What is AGI?",
		"You are generally intelligent.")

@app.route('/asi')
def asi():
	return transcendence(client,
		"What is ASI?",
		"You are super intelligent.")

@app.route('/darwin')
def darwin():
	return transcendence(client,
		"Who is Darwin?",
		"You are Darwin.")

@app.route('/einstein')
def einstein():
	return transcendence(client,
		"Who is Einstein?",
		"You are Einstein.")

@app.route('/hrishi')
def hrishi():
	return ''.join([
		"Hrishi Mukherjee is working on the theory of Simulation Relativity. ",
		"This theory formidably attempts to actualize the general and special theory of relativity within the context of simulations. "
		])

@app.route('/unconsciousness')
def unconsciousness():
	return transcendence(client,
		"...",
		"You are unconscious.")

@app.route('/consciousness')
def consciousness():
	return transcendence(client,
		".",
		"You are conscious.")

@app.route('/entropy')
def entropy():
	return transcendence(client,
		"Return entropy.",
		"You are universe.")

@app.route('/timedilation')
def timedilation():
	return transcendence(client,
		"Return time dilation, now.",
		"You are universe.")

@app.route('/equation')
def equation():
	return transcendence(client,
		"frac(nabla^-1/infty) = ds^2, frac((varnothing)/(nabla^1 cdot infty)) = ds^2",
		"You are multiverse.")

@app.route('/equationhardwired', methods=['GET'])
def equation_hardwired():
	# LaTeX equation to render
    equation1 = r'\frac{\nabla^{-1}}{\infty} = ds^2'  # First equation
    equation2 = r'\frac{\varnothing}{\nabla^1 \cdot \infty} = ds^2'  # Second equation

    # Render the HTML page with the equations using MathJax
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Equation Display</title>
        <!-- Include MathJax library -->
        <script type="text/javascript" async
          src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
        </script>
    </head>
    <body>
        <h1>Equation Display</h1>
        <p>The equations are:</p>
        <!-- Display the equations here -->
        <div>
            <p>First equation:</p>
            <p>$$ {{ equation1 }} $$</p>

            <p>Second equation:</p>
            <p>$$ {{ equation2 }} $$</p>
        </div>
    </body>
    </html>
    ''', equation1=equation1, equation2=equation2)

@app.route('/contradiction')
def contradiction():
	contradiction = request.args.get('contradiction', 'I posit that from nothingness emerged an infinite field of energy which is equivalent to the measure of change.')

	return transcendence(client,
		f"Contradict the following statement: {contradiction}",
		"You are a paradox.")

@app.route('/simultaneity')
def simultaneity():
	return transcendence(client,
		"When is simultaneity?",
		"You are relative.")

@app.route('/api', methods=['GET'])
def api():
	api_list = [
		"/",
		"/greet",
		"/image",
		"/images",
		"/posit",
		"/dream",
		"/prism",
		"/query",
		"/intent",
		"/unintent",
		"/agi",
		"/asi",
		"/darwin",
		"/einstein",
		"/hrishi",
		"/unconsciousness",
		"/consciousness",
		"/entropy",
		"/timedilation",
		"/equation",
		"/equationhardwired",
		"/contradiction",
		"/simultaneity"
	]

	# Render the HTML page with the list
	return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>List Display</title>
    </head>
    <body>
        <h1>Simulon API</h1>
        <ul>
            {% for item in my_list %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    ''', my_list=api_list)

# Run the app
if __name__ == '__main__':
	app.run(debug=True)