from flask import Flask, render_template, url_for

# Create app
app= Flask(__name__)

display_and_text_size_data = {
    "title":"Display & Text Size",
    "steps": [
            {
            "step": "Click on the Display & Text Size tab to see the accessibility settings for Display & Text Size",
            "subtitle": "Display & Text Size",
            "caption":"Left Image: Red box highlights the 'Display & Text Size' tab in Accessbility settings.\n Right Image: we can view the 'Display & Text Size' settings options"
            },
            {
            "step": "Display the text in boldface characters.",
            "subtitle": "Bold Text",
            "caption":"Left Image: Red box highlights 'Bold Text' option.\n Right Image: Bold Text is toggled on and the text is boldend"
            },
            {
            "step": "Turn on Larger Accessibility Sizes, then adjust the text size using the slider. This setting adjusts to your preferred text size in apps that support Dynamic Type, such as Settings, Calendar, Contacts, Mail, Messages, and Notes.",
            "subtitle": "Larger Text",
            "caption":"Left Image: Red box highlights 'Larger Text' option.\n Right Image: 'Larger Text' is toggled on and enters a view with a text size slider at the bottom"
            },
            {
            "step": "This setting underlines text you can tap.",
            "subtitle": "Button Shapes",
            "caption":"Left Image: Red box highlights 'Button Shapes' option.\n Right Image: 'Button Shapes' is toggled on and the text is underlined"
            },
            {
            "step": "This setting indicates switches turned on with “1” and switches turned off with “0”.",
            "subtitle": "On/Off Labels",
            "caption":"Left Image: Red box highlights 'On/Off Labels' option.\n Right Image: 'On/Off Labels' is toggled on and displays '1' or '0' as an on or off indicator"
            },
            {
            "step": "This setting reduces the transparency and blurs on some backgrounds.",
            "subtitle": "Reduce Transparency",
            "caption":"Left Image: Red box highlights 'Reduce Transparency' option.\n Right Image: 'Reduce Transparency' is toggled on"
            },
            {
            "step": "This setting improves the contrast and legibility by altering color and text styling. Apps that support Dynamic Type—such as Settings, Calendar, Contacts, Mail, Messages, and Notes—adjust to your preferred text size.",
            "subtitle": "Increase Contrast",
            "caption":"Left Image: Red box highlights 'Increase Contrast' option.\n Right Image: 'Increase Contrast' is toggled on and the screen appears more constrasted"
            },
            {
            "step": "This setting replaces user interface items that rely on color to convey information with alternatives.",
            "subtitle": "Differentiate Without Color",
            "caption":"Left Image: Red box highlights 'Differentiate Without Color' option.\n Right Image: 'Differentiate Without Color' is toggled on"
            },
            {
            "step": "Smart Invert Colors reverses the colors of the display, except for images, media, and some apps that use dark color styles.",
            "subtitle": "Smart Invert",
            "caption":"Left Image: Red box highlights 'Smart Invert' option.\n Right Image: 'Smart Invert' is toggled on and reverses the colors of the display"
            },
            {
            "step": "Classic Invert Colors reverses the colors of the display, except for images, media, and some apps that use dark color styles.",
            "subtitle": "Classic Invert",
            "caption":"Left Image: Red box highlights 'Classic Invert' option.\n Right Image: 'Classic Invert' is toggled on and reverses the colors of the display"
            },
            {
            "step": "Tap a filter to apply it. To adjust the intensity or hue, drag the sliders.",
            "subtitle": "Color Filters",
            "caption":"Left Image: Red box highlights 'Color Filters' option.\n Right Image: 'Color Filters' is toggled on and options for color filters are displayed in addition to view slider"
            },
            {
            "step": "This setting reduces the intensity of bright colors.",
            "subtitle": "Reduce White Point",
            "caption":"Left Image: Red box highlights 'Reduce White Point' option.\n Right Image: 'Reduce White Point' is toggled on and reduces the intensity of bright colors"
            },
            {
            "step": "This setting automatically adjusts the screen brightness for current light conditions using the built-in ambient light sensor.",
            "subtitle": "Auto-Brightness",
            "caption":"Left Image: Red box highlights 'Auto-Brightness' option.\n Right Image: 'Auto-Brightness' is toggled on and enables auto-brightness"
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
            "subtitle": "Zoom",
            "caption":"Left Image: Red box highlights the 'Spoken Content' tab in Accessbility settings.\n Right Image: we can view the 'Spoken Content' settings options"
         },
         {
                "step":  "Turning on the “Follow Focus” button moves the Zoom window to the text you are typing and will follow along as you type.",
                "subtitle": "Follow Focus",
            "caption":"Image:'Follow Focus' is toggled on and enabled"
            },
            {
                "step":  "Turning on “Smart Typing” moves the Zoom window when a keyboard pops up so that the text is zoomed in but the keyboard is not.",
                "subtitle": "Smart Typing",
            "caption":"Image:'Follow Focus' is toggled on and enabled"
            },
            {
                "step":  "With the keyboard shortcuts, you see that more functionality is available in the MacBook because the keyboard keys are more easily accessible there. Here are several zoom options depicted in the image below.",
                "subtitle": "Keyboard Shortcuts",
            "caption":"Left Image: Red box highlights 'Keyboard Shortcuts' option.\n Right Image: 'Keyboard Shortcuts' is toggled on and options for keyboard shortcuts are displayed"
            },
            {
                "step":  "The Zoom controller can be dragged to be repositioned when zoomed out, and when zoomed in, the controller can be used to pan across the screen. The long press and drag can be used to reposition. There are three controller actions that are available: Show menu, Zoom In/Out, and Speak on Touch, and you can designate them as either single, double, or triple touch.",
                "subtitle": "Zoom Controller",
            "caption":"Left Image: Red box highlights 'Zoom Controller' option.\n Right Image: 'Zoom Controller' is toggled on and and options for the zoom controller are displayed"
            },
            {
                "step":  "Double tap and slide on the controller to adjust the zoom level. You can also change the color and opacity of the Zoom Controller.",
                "subtitle": "Adjust the Zoom Level",
            "caption":"Image: Red box highlights 'Adjust the Zoom Level' option which is toggled on and enabled."
            },
            {
                "step":  "There are two kinds of zoom regions: full-screen zoom or window zoom. When Window Zoom is toggled on, the Zoom Menu options change to: Zoom In/Out (Zoom Out will remove the Zoom Window & the screen will convert to native size), and Full Screen Zoom (disables Zoom Window and full screen is magnified).",
                "subtitle": "Zoom Region",
            "caption":"Left Image: Red box highlights 'Zoom Region' option.\n Right Image: 'Zoom Region' is toggled on and and options for the zoom region are displayed"
            },
            {
                "step":  "This feature allows the user to determine the filter options: none, inverted, grayscale, grayscale inverted, and low light.",
                "subtitle": "Zoom Filter",
                "caption":"Left Image: Red box highlights 'Zoom Filter' option.\n Right Image: 'Zoom Filter' is toggled on and and options for the 'Zoom Filter' are displayed"
            },
            {
                "step":  "Controls whether zoom appears while sharing your screen and during screen recordings.",
                "subtitle": "Show while Mirroring",
            "caption":"Image: Red circle highlights 'Show while Mirroring' option which is toggled on and enabled."
            },
            {
                "step":  "This feature allows students to limit the amount of magnification. The maximum amount is 15x. Limiting the amount of magnification can be beneficial when using an iPod or iPhone due to the small screen sizes. Some students may benefit from having his/her TVI set to the maximum level of Zoom.",
                "subtitle": "Maximum Zoom Level",
            "caption":"Image: Red circle highlights the slider for the Maximum Zoom Level option "
            }
    ],
   "images": ["img/zoom.jpeg","img/follow-focus.jpeg","img/smart-typing.jpeg","img/keyboard-shortcuts.jpeg","img/zoom-controller.jpeg", "img/adjust-zoom.jpeg","img/zoom-region.jpeg", "img/zoom-filter.jpeg","img/mirror.jpeg", "img/max-zoom.jpeg"]
}
spoken_content_data = {
    "title":"Spoken Content",
    "steps": [
        {
            "step": "Click on the Spoken Content tab to see the accessibility settings for Spoken Content",
            "subtitle": "Spoken Content",
            "caption":"Left Image: Red box highlights 'Zoom Region' option.\n Right Image: 'Zoom Region' is toggled on and and options for the zoom region are displayed"
         },
         {
                "step":  "To hear text you toggled on, tap the Speak button. Highlight Content is also visible in the options when this option is on.",
                "subtitle": "Speak Selection",
                "caption":"Left Image: Red box highlights 'Speak Selection' option on.\n Right Image: 'Speak Selection' is toggled on and yellow box highlighting the 'Highlight Content' option appears"
            },
            {
                "step":  "To hear the entire screen, swipe down with two fingers from the top of the screen. Speech Controller is also visible in the options when this option and Speak Selection are both on.",
                "subtitle": "Speak Screen",
                "caption":"Left Image: Red box highlights 'Speak Screen' option on.\n Right Image: 'Speak Screen' is toggled on and yellow box highlighting the 'Speech Controller' option appears"
            },
            {
                "step":  "Show the controller for quick access to Speak Screen and Speak on Touch. You are able to provide controller actions of to “Read all Content” or “Speak on Touch” to either Long Press or Double Tap options. You can also change the opacity of the widget.",
                "subtitle": "Speech Controller",
            "caption":"Left Image: Red box highlights 'Speech Controller' option is selected.\n Right Image: A yellow box highlighting the expanded speech controller option appears"
            },
            {
                "step":  "iPhone can highlight words, sentences, or both as they’re spoken. You can change the highlight color and style.",
                "subtitle": "Highlight Content",
            "caption":"Left Image: Red box highlights 'Highlight Content' option is selected.\n Right Image: 'Highlight Content' is toggled on and its options are displayed"
            },
            {
                "step":  "You can configure typing feedback for the onscreen and external keyboards and choose to have iPhone speak each character, entire words, auto-corrections, auto-capitalizations, and typing predictions. To hear typing predictions, you also need to go to Settings > General > Keyboards, then turn on Predictive.",
                "subtitle": "Typing Feedback",
            "caption":"Left Image: Red box highlights 'Typing Feedback' option is selected.\n Right Image: 'Typing Feedback' is toggled on and its options are displayed"
            },
            {
                "step":  "Choose a voice and dialect.",
                "subtitle": "Voices",
            "caption":"Left Image: Red box highlights 'Voices' option is selected.\n Right Image: 'Voices' options are displayed"
            },
            {
                "step":  "Select a default language.",
                "subtitle": "Default Language",
            "caption":"Left Image: Red box highlights 'Default Language' option is selected.\n Right Image: 'Default Language' options are displayed"
            },
            {
                "step":  "Detect what languages are being spoken.",
                "subtitle": "Detect Languages",
            "caption":"Image: Red box highlights 'Detect Languages' option is toggled on."
            },
            {
                "step":  "Drag the slider between slow speaking depicted by the tortoise to fast speaking depicted by the hare.",
                "subtitle": "Speaking Rate",
                "caption":"Image: Red box highlights 'Speaking Rate' slider."
            },
            {
                "step":  "Dictate or spell out how you want certain phrases to be spoken.",
                "subtitle": "Pronunciations",
            "caption":"Left Image: Red box highlights 'Pronunciations' option is selected.\n Right Image: Input screen for entering a new pornounciation replacement is displayed"
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