from flask import Flask, render_template, url_for

# Create app
app= Flask(__name__)

display_and_text_size_data = {
    "title":"Display & Text Size",
    "steps": [
            {
            "step": "Click on the Display & Text Size tab to see the accessibility settings for Display & Text Size",
            "subtitle": "Display & Text Size"
            },
            {
            "step": "Display the text in boldface characters.",
            "subtitle": "Bold Text"
            },
            {
            "step": "Turn on Larger Accessibility Sizes, then adjust the text size using the slider. This setting adjusts to your preferred text size in apps that support Dynamic Type, such as Settings, Calendar, Contacts, Mail, Messages, and Notes.",
            "subtitle": "Larger Text"
            },
            {
            "step": "This setting underlines text you can tap.",
            "subtitle": "Button Shapes"
            },
            {
            "step": "This setting indicates switches turned on with “1” and switches turned off with “0”.",
            "subtitle": "On/Off Labels"
            },
            {
            "step": "This setting reduces the transparency and blurs on some backgrounds.",
            "subtitle": "Reduce Transparency"
            },
            {
            "step": "This setting improves the contrast and legibility by altering color and text styling. Apps that support Dynamic Type—such as Settings, Calendar, Contacts, Mail, Messages, and Notes—adjust to your preferred text size.",
            "subtitle": "Increase Contrast"
            },
            {
            "step": "This setting replaces user interface items that rely on color to convey information with alternatives.",
            "subtitle": "Differentiate Without Color"
            },
            {
            "step": "Smart Invert Colors reverses the colors of the display, except for images, media, and some apps that use dark color styles.",
            "subtitle": "Smart Invert"
            },
            {
            "step": "Classic Invert Colors reverses the colors of the display, except for images, media, and some apps that use dark color styles.",
            "subtitle": "Classic Invert",
            },
            {
            "step": "Tap a filter to apply it. To adjust the intensity or hue, drag the sliders.",
            "subtitle": "Color Filters"
            },
            {
            "step": "This setting reduces the intensity of bright colors.",
            "subtitle": "Reduce White Point"
            },
            {
            "step": "This setting automatically adjusts the screen brightness for current light conditions using the built-in ambient light sensor.",
            "subtitle": "Auto-Brightness"
            }
    ],
    "images": ["img/displaytext.jpeg",
                "img/boldtext.jpeg",
                "img/larger.jpeg",
                "img/buttonshape.jpeg",
                "img/onoff.jpeg",
                "img/reduce.jpeg",
                "img/increasecontrast.jpeg",
                "img/diffwocolor.jpg",
                "img/smartinvert.jpg",
                "img/classicinvert.jpg",
                "img/colorfilter.jpg",
                "img/whitept.jpg",
                "img/auto.jpg"]
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
   "images": ["img/zoom.jpeg","img/follow-focus.jpeg","img/smart-typing.jpeg","img/keyboard-shortcuts.jpeg","img/zoom-controller.jpeg", "img/adjust-zoom.jpeg","img/zoom-region.jpeg", "img/zoom-filter.jpeg","img/mirror.jpeg", "img/max-zoom.jpeg"]
}
spoken_content_data = {
    "title":"Spoken Content",
    "steps": [
        {
            "step": "Click on the Spoken Content tab to see the accessibility settings for Spoken Content",
            "subtitle": "Spoken Content"
         },
         {
                "step":  "To hear text you selected, tap the Speak button. Highlight Content is also visible in the options when this option is on.",
                "subtitle": "Speak Selection"
            },
            {
                "step":  "To hear the entire screen, swipe down with two fingers from the top of the screen. Speech Controller is also visible in the options when this option and Speak Selection are both on.",
                "subtitle": "Speak Screen"
            },
            {
                "step":  "Show the controller for quick access to Speak Screen and Speak on Touch. You are able to provide controller actions of to “Read all Content” or “Speak on Touch” to either Long Press or Double Tap options. You can also change the opacity of the widget.",
                "subtitle": "Speech Controller"
            },
            {
                "step":  "iPhone can highlight words, sentences, or both as they’re spoken. You can change the highlight color and style.",
                "subtitle": "Highlight Content"
            },
            {
                "step":  "You can configure typing feedback for the onscreen and external keyboards and choose to have iPhone speak each character, entire words, auto-corrections, auto-capitalizations, and typing predictions. To hear typing predictions, you also need to go to Settings > General > Keyboards, then turn on Predictive.",
                "subtitle": "Typing Feedback"
            },
            {
                "step":  "Choose a voice and dialect.",
                "subtitle": "Voices"
            },
            {
                "step":  "Select a default language.",
                "subtitle": "Default Language"
            },
            {
                "step":  "Detect what languages are being spoken.",
                "subtitle": "Detect Languages"
            },
            {
                "step":  "Drag the slider between slow speaking depicted by the tortoise to fast speaking depicted by the hare.",
                "subtitle": "Speaking Rate"
            },
            {
                "step":  "Dictate or spell out how you want certain phrases to be spoken.",
                "subtitle": "Pronunciations"
            }
    ],
    "images": ["img/spokencontent.jpg",
                "img/speakselection.jpg",
               "img/speakscreen.jpg",
               "img/speechcontroller.jpg",
               "img/highlight content.jpg",
               "img/typingfeedback.jpg",
               "img/voices.jpg",
               "img/defaultlang.jpg",
               "img/detect.jpeg",
               "img/speakrate.jpg",
               "img/pronunciations.jpg"    
               ]
}

accessibility_template = "accessibilityTemplate.html"
quiz_html = "quiz.html"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/display_and_text_size')
def display_and_text_size():
    return render_template(accessibility_template, data = display_and_text_size_data)

@app.route('/get_display_and_text_size_data')
def get_display_and_text_size_data():
    return display_and_text_size_data

@app.route('/zoom')
def zoom():
    return render_template(accessibility_template, data = zoom_data)

@app.route('/get_zoom_data')
def get_zoom_data():
    return zoom_data

@app.route('/spoken_content')
def spoken_content():
    return render_template(accessibility_template, data = spoken_content_data)


@app.route('/get_spoken_content_data')
def get_spoken_content_data():
    return spoken_content_data

@app.route('/quiz/<id>')
def quiz(id):
    if id == "Display & Text Size":
        return render_template(quiz_html, data = display_and_text_size_data)
    elif id == "Spoken Content":
        return render_template(quiz_html, data = spoken_content_data)
    return render_template(quiz_html, data = zoom_data)





if __name__=="__main__":
    app.run(port=8000, debug=True)