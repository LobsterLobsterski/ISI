import fetch from 'node-fetch';

export const getPhotos = async (req, res) => {
    const response = await fetch('https://jsonplaceholder.typicode.com/photos?_limit=4');
    const photos = await response.json();
    let html = '<h1>Photos</h1>';
    photos.forEach(photo => {
        html += `<div>
                    <h2>${photo.title}</h2>
                    <img src="${photo.url}" alt="${photo.title}" style="width:100px;height:100px;">
                 </div>`;
    });
    res.send(html);
};
