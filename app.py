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
            "step": "Click on the Zoom tab to see the accessibility settings for Zoom",
            "subtitle": "Zoom"
         },
         {
                "step":  "Turning on the “Follow Focus” button moves the Zoom window to the text you are typing and will follow along as you type.",
                "subtitle": "Follow Focus"
            },
            {
                "step":  "Turning on “Smart Typing” moves the Zoom window when a keyboard pops up so that the text is zoomed in but the keyboard is not.",
                "subtitle": "Smart Typing"
            },
            {
                "step":  "With the keyboard shortcuts, you see that more functionality is available in the MacBook because the keyboard keys are more easily accessible there. Here are several zoom options depicted in the image below.",
                "subtitle": "Keyboard Shortcuts"
            },
            {
                "step":  "The Zoom controller can be dragged to be repositioned when zoomed out, and when zoomed in, the controller can be used to pan across the screen. The long press and drag can be used to reposition. There are three controller actions that are available: Show menu, Zoom In/Out, and Speak on Touch, and you can designate them as either single, double, or triple touch.",
                "subtitle": "Zoom Controller"
            },
            {
                "step":  "Double tap and slide on the controller to adjust the zoom level. You can also change the color and opacity of the Zoom Controller.",
                "subtitle": "Adjust the Zoom Level"
            },
            {
                "step":  "There are two kinds of zoom regions: full-screen zoom or window zoom. When Window Zoom is selected, the Zoom Menu options change to: Zoom In/Out (Zoom Out will remove the Zoom Window & the screen will convert to native size), and Full Screen Zoom (disables Zoom Window and full screen is magnified).",
                "subtitle": "Zoom Region"
            },
            {
                "step":  "This feature allows the user to determine the filter options: none, inverted, grayscale, grayscale inverted, and low light.",
                "subtitle": "Zoom Filter"
            },
            {
                "step":  "Controls whether zoom appears while sharing your screen and during screen recordings.",
                "subtitle": "Show while Mirroring"
            },
            {
                "step":  "This feature allows students to limit the amount of magnification. The maximum amount is 15x. Limiting the amount of magnification can be beneficial when using an iPod or iPhone due to the small screen sizes. Some students may benefit from having his/her TVI set to the maximum level of Zoom.",
                "subtitle": "Maximum Zoom Level"
            }
    ],
   "images": ["img/keyboard-shortcuts.jpeg","img/keyboard-shortcuts.jpeg","img/keyboard-shortcuts.jpeg","img/keyboard-shortcuts.jpeg","img/zoom-controller.jpeg", "img/zoom-controller.jpeg","img/zoom-region.jpeg", "img/zoom-filter.jpeg","img/mirror.jpeg", "img/max-zoom.jpeg"]
}
spoken_content_data = {
    "title":"Spoken Content",
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