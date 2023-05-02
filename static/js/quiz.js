let title = document.getElementById("title-for-js").innerHTML.toLowerCase()
title = title.replace(/&amp;/g, 'and')
title = title.replace(/ /g, '_')

const subtitle_to_image = {}

const getData = async () => {
    try{
        console.log(title)
        const response = await fetch(`/get_${title}_data`);
        const data = await response.json();
        return data;
    } catch {
        return {}
    }

}

function shuffle(array) {
    let currentIndex = array.length,  randomIndex;
  
    // While there remain elements to shuffle.
    while (currentIndex != 0) {
  
      // Pick a remaining element.
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex--;
  
      // And swap it with the current element.
      [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]];
    }
  
    return array;
}

const display_quiz = (images, subtitles, captions) =>{
    for (let i = 0; i < subtitles.length; i++) {
        let subtitle = subtitles[i]
        let subtitleElement = document.getElementById(`subtitle-${i+1}`)
        let answerElement = document.getElementById(`answer-${i+1}`)
        subtitleElement.innerHTML = `${i+1}. ${subtitle}`
        answerElement.innerHTML = subtitle
    }

    for (let i = 0; i < images.length; i++) {
        let image = images[i]
        let imageElement = document.getElementById(`img-${i+1}`)
        imageElement.src = `../static/${image}`
        imageElement.alt = captions[i]
    }
}

const checkInputs = () => {
    const inputs = document.getElementsByClassName("answer");
    console.log(inputs)
    for (let i = 0; i < inputs.length; i++) {
        let input = inputs[i]
        let value = input.value
        
        let answerElement = document.getElementById(`answer-${value}`)
        let isCorrect = false
        if (answerElement) {
            let answer = answerElement.innerHTML
            answer = answer.replace(/&amp;/g, '&')
            let realAnswer = subtitle_to_image[i+1]
            console.log(answer, realAnswer)
            if (answer == realAnswer) {
                isCorrect = true
            }
        }

        if (isCorrect) {
            if (input.classList.contains("is-invalid")) {
                input.classList.remove("is-invalid")
            }
            input.classList.add("is-valid")
        } else {
            if (input.classList.contains("is-valid")) {
                input.classList.remove("is-valid")
            }
            input.classList.add("is-invalid")
        }
        

    }
}
  
const init = async () =>{
    // Used like so
    let data = await getData()
    let images = []
    let subtitles = []
    let captions = []
    if (Object.keys(data).length != 0){
        images = data['images']
        let steps = data["steps"]
        for (let i = 0; i < steps.length; i++){
            let step = steps[i]
            subtitles.push(step["subtitle"])
            let subtitle = step["subtitle"]
            let caption = step["caption"]
            captions.push(caption)
            //subtitle = subtitle.replace(/&amp;/g, 'and')
            subtitle_to_image[i+1] = subtitle
        }
    }
    console.log(subtitles)
    //subtitles = shuffle(subtitles);
    display_quiz(images, subtitles, captions)

    const checkInputsBtn = document.getElementById("check-inputs-btn")
    checkInputsBtn.addEventListener("click", ()=>{
        checkInputs()
    });
}

init()


