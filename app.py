from flask import Flask, render_template, url_for

# Create app
app= Flask(__name__)

display_and_text_size_data = {
    "title":"Display & Text Size",
    "steps": [
        {
                "step": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Et sollicitudin ac orci phasellus egestas tellus rutrum. Pellentesque sit amet porttitor eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Et malesuada fames ac turpis egestas maecenas pharetra convallis. In eu mi bibendum neque egestas. Non nisi est sit amet facilisis magna etiam tempor orci. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lacus vestibulum sed arcu non odio euismod. Tellus molestie nunc non blandit massa. Massa id neque aliquam vestibulum morbi blandit cursus risus.",
                "subtitle": "sub1"
            },
            {
                "step":  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Et sollicitudin ac orci phasellus egestas tellus rutrum. Pellentesque sit amet porttitor eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Et malesuada fames ac turpis egestas maecenas pharetra convallis. In eu mi bibendum neque egestas. Non nisi est sit amet facilisis magna etiam tempor orci. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lacus vestibulum sed arcu non odio euismod. Tellusum morbi blandit cursus risus.",
                "subtitle": "sub2"
            }      
    ],
    "images": ["https://gratisography.com/wp-content/uploads/2023/02/gratisography-colorful-kittenfree-stock-photo-800x525.jpg", "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"]
}

zoom_data = {
    "title":"Zoom",
        "steps": [
            {
                "step": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Et sollicitudin ac orci phasellus egestas tellus rutrum. Pellentesque sit amet porttitor eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Et malesuada fames ac turpis egestas maecenas pharetra convallis. In eu mi bibendum neque egestas. Non nisi est sit amet facilisis magna etiam tempor orci. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lacus vestibulum sed arcu non odio euismod. Tellus molestie nunc non blandit massa. Massa id neque aliquam vestibulum morbi blandit cursus risus.",
                "subtitle": "sub1"
            },
            {
                "step":  "Lorem ipsumr sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Et sollicitudin ac orci phasellus egestas tellus rutrum. Pellentesque sit amet porttitor eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Et malesuada fames ac turpis egestas maecenas pharetra convallis. In eu mi bibendum neque egestas. Non nisi est sit amet facilisis magna etiam tempor orci. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lacus vestibulum sed arcu non odio euismod. Tellusum morbi blandit cursus risus.",
                "subtitle": "sub2"
            }            
    ],
    "images": ["https://gratisography.com/wp-content/uploads/2023/02/gratisography-colorful-kittenfree-stock-photo-800x525.jpg", "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"]
}
spoken_content_data = {
    "title":"Spoken Content",
    "steps": [
         {
                "step":  "Lorem ipsum r sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Et sollicitudin ac orci phasellus egestas tellus rutrum. Pellentesque sit amet porttitor eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Et malesuada fames ac turpis egestas maecenas pharetra convallis. In eu mi bibendum neque egestas. Non nisi est sit amet facilisis magna etiam tempor orci. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lacus vestibulum sed arcu non odio euismod. Tellus molestie nunc non blandit massa. Massa id neque aliquam vestibulum morbi blandit cursus risus.",
                "subtitle": "sub1"
            },
            {
                "step":  "Lorem ipsum dolor sit amet, conetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus. Et sollicitudin ac orci phasellus egestas tellus rutrum. Pellentesque sit amet porttitor eget. Ultrices mi tempus imperdiet nulla malesuada pellentesque. Etiam non quam lacus suspendisse faucibus interdum posuere. Et malesuada fames ac turpis egestas maecenas pharetra convallis. In eu mi bibendum neque egestas. Non nisi est sit amet facilisis magna etiam tempor orci. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit sed. Lacus vestibulum sed arcu non odio euismod. Tellusum morbi blandit cursus risus.",
                "subtitle": "sub2"
            }      
    ],
   "images": ["https://gratisography.com/wp-content/uploads/2023/02/gratisography-colorful-kittenfree-stock-photo-800x525.jpg", "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"]
}

accessibility_template = "accessibilityTemplate.html"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/display_and_text_size')
def display_and_text_size():
    return render_template(accessibility_template, data = display_and_text_size_data)

@app.route('/zoom')
def zoom():
    return render_template(accessibility_template, data = zoom_data)

@app.route('/spoken_content')
def spoken_content():
    return render_template(accessibility_template, data = spoken_content_data)

if __name__=="__main__":
    app.run(port=8000, debug=True)