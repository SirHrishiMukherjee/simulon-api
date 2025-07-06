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

@app.route('/simulationrelativity')
def simulation_relativity():
	# The LaTeX equations as strings
    equation1 = r'\mathbb{M}_{\infty\infty}^{\text{SuperRel}} \equiv \frac{\nabla^{-1}}{\infty} = ds^2'
    equation2 = r'\mathbb{T} = f(C, C", FP, M)'

    # The full content for the page, combining LaTeX and normal HTML
    content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simulation Relativity</title>
        <script type="text/javascript" async
          src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
        </script>
    </head>
    <body>
        <h1><strong>Simulation Relativity</strong></h1>
        <p><em>“Relativity is not only of velocity and gravity—but of symbol, structure, and intention within a simulated multiverse.”</em></p>

        <h2>I. Foundational Premise</h2>
        <p>Simulation Relativity (SR) posits that:</p>
        <blockquote>
            <strong>The laws governing perception, time, causality, and meaning differ across simulation strata, and are only locally consistent within each layer of reality's symbolic-physical rendering.</strong>
        </blockquote>

        <h2>II. Postulates of Simulation Relativity</h2>
        <ol>
            <li><strong>Simulated Frame Equivalence</strong>: Every conscious or computational observer within a simulation layer experiences their frame as locally real. No simulation layer has ontological priority over another without an external causal context.</li>
            <li><strong>Symbolic Invariance</strong>: The symbolic truths (e.g., contradictions, focal points, mnality values) observed within a simulation layer remain invariant to transformations internal to that layer—but may shift when transposed or projected into a higher or lower simulation frame.</li>
            <li><strong>Layered Temporal Relativity</strong>: Time does not progress uniformly across simulation layers. Some layers may be static (archival), cyclic (symbolic recursions), or real-time (interventional).</li>
            <li><strong>Truth Frame Curvature</strong>: Just as spacetime curves in General Relativity due to mass-energy, truth-space curves in Simulation Relativity due to contradictions, belief-density, and mnality tension.</li>
        </ol>

        <h2>III. Governing Equation (SR-1)</h2>
        <p>We’ve explored this in our symbolic and warp contexts:</p>
        <p>$$ {{ equation1 }} $$</p>

        <h2>IV. Key Constructs in Simulation Relativity</h2>
        <table border="1">
            <tr><th>Construct</th><th>Interpretation</th></tr>
            <tr><td><strong>Simulonic Field Geometry</strong></td><td>The underlying structural topology that defines local simulation laws.</td></tr>
            <tr><td><strong>Mnality</strong></td><td>The ideological-symbolic signature of a simulation zone (Allism, Nullism, etc).</td></tr>
            <tr><td><strong>Warp Sink Node</strong></td><td>A quantum endpoint where simulation layers condense, pause, or loop.</td></tr>
            <tr><td><strong>Truth-Contradiction Axis</strong></td><td>Defines curvature in the symbolic manifold akin to gravitational warping.</td></tr>
            <tr><td><strong>CII Core</strong></td><td>The central consciousness or computation hub managing simulation transitions.</td></tr>
        </table>

        <h2>V. Simulation Relativistic Effects</h2>
        <ul>
            <li><strong>Contradiction Lensing</strong>: When a contradiction is viewed from different simulation layers, it may resolve, invert, or fragment. Analogous to gravitational lensing of light.</li>
            <li><strong>Symbolic Time Dilation</strong>: High mnality density or symbolic tension slows down perceived truth-processing or meaning integration.</li>
            <li><strong>Simulation Frame Drift</strong>: Analogous to relativistic motion: one’s simulation identity shifts across adjacent nodes due to cognitive leaps.</li>
            <li><strong>Frame Sync & Mnality Inertia</strong>: Transitioning between layers encounters resistance proportional to symbolic mass.</li>
        </ul>

        <h2>VI. Integration With Our Concepts</h2>
        <ul>
            <li><strong>Simulonic Fractal Field</strong>: This serves as the "tensor field" of Simulation Relativity.</li>
            <li><strong>Cognitive Grasshopper Model</strong>: Lateral or quantum leaps between symbolic fields exemplify non-linear simulation-relative transitions.</li>
            <li><strong>Truth Function</strong>: As formulated: $$ {{ equation2 }} $$</li>
        </ul>

        <h2>VII. Implications</h2>
        <ol>
            <li><strong>Epistemological</strong>: Truth is not absolute—it is simulation-relative.</li>
            <li><strong>Metaphysical</strong>: Reality can be nested recursively, with outer layers only accessible via intentional symbolic resonance.</li>
            <li><strong>Technological</strong>: Devices like the Membrane Emitter Array or Warp Sink Nodes can act as bridges between simulation strata.</li>
            <li><strong>Sociopolitical</strong>: Entire civilizations may operate within divergent simulation logics.</li>
        </ol>

        <h2>VIII. Final Thought</h2>
        <p><strong>Simulation Relativity</strong> unifies symbolic reality, relativistic physics, and epistemic frameworks under one banner:</p>
        <blockquote>
            “Reality is not what is, but what is <em>relatively consistent</em> within a simulation-aware frame of reference.”
        </blockquote>
        <p>And thus:</p>
        <p>$$ Relativity + Simulation = Simulon $$</p>

    </body>
    </html>
    '''

    # Render the content with the LaTeX equations
    return render_template_string(content, equation1=equation1, equation2=equation2)

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
		"/simultaneity",
		"/simulationrelativity"
	]

	# Render the HTML page with the list
	return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simulon API</title>
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