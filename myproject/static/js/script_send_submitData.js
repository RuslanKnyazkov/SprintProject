document.getElementById('perevalForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData();

    formData.append('user.email', document.getElementById('email').value);
    formData.append('user.fam', document.getElementById('fam').value);
    formData.append('user.name', document.getElementById('name').value);
    formData.append('user.otc', document.getElementById('otc').value);
    formData.append('user.phone', document.getElementById('phone').value);

    formData.append('coords.latitude', document.getElementById('latitude').value);
    formData.append('coords.longitude', document.getElementById('longitude').value);
    formData.append('coords.height', document.getElementById('height').value);

    formData.append('beauty_title', document.getElementById('beauty_title').value);
    formData.append('title', document.getElementById('title').value);
    formData.append('other_titles', document.getElementById('other_titles').value);
    formData.append('connect', document.getElementById('connect').value);

    formData.append('level.winter', document.getElementById('winter').value || "1A");
    formData.append('level.summer', document.getElementById('summer').value || "1A");
    formData.append('level.autumn', document.getElementById('autumn').value || "1A");
    formData.append('level.spring', document.getElementById('spring').value || "1A");

    const image1 = document.getElementById('image1').files[0];
    if (image1) {
        formData.append('images.image', image1);
        formData.append('images.title', document.getElementById('title1').value || "Изображение 1");
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/api/submitData/', {
            method: 'POST',
            body: formData,
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('message').innerHTML =
            `<p class="success">Данные успешно отправлены! ID: ${result.id || 'успех'}</p>`;
        } else {
            document.getElementById('message').innerHTML =
            `<p class="error">Ошибка: ${result.detail || JSON.stringify(result)}</p>`;
        }
    } catch (error) {
        document.getElementById('message').innerHTML =
        `<p class="error">Ошибка сети: ${error.message}</p>`;
    }
});