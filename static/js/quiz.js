let title = document.getElementById("title-for-js").innerHTML.toLowerCase()
title = title.replace(/&amp;/g, 'and')
title = title.replace(/ /g, '_')

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

const display_quiz = (images) =>{
    for (let i = 0; i < images.length; i++) {
        let image = images[i]
        let imageElement = document.getElementById(`img-${i+1}`)
        imageElement.src = `{{url_for('static',filename = /${image}}}`
    }
}
  
const init = async () =>{
    // Used like so
    let data = await getData()
    let images = []
    if (Object.keys(data).length != 0){
        images = data['images']
    }
    console.log(images)
    shuffle(images);
    display_quiz(images)
    

}

init()


