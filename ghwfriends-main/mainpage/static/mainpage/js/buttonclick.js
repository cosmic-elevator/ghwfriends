document.getElementById('item-b').addEventListener('click', function() {
    document.getElementById('popup').style.display = 'block';
});

document.getElementById('close-btn').addEventListener('click', function() {
    document.getElementById('popup').style.display = 'none';
});

let slides = [
    document.querySelector('.slide0'),
    document.querySelector('.slide1'),
    document.querySelector('.slide2')
];

function nextSlide() {
    slides[0].classList.remove('slide0');
    slides[0].classList.add('slide2');
    slides[0].classList.add('slide-all');

    slides[1].classList.remove('slide1');
    slides[1].classList.add('slide0');
    slides[1].classList.add('slide-all');

    slides[2].classList.remove('slide2');
    slides[2].classList.add('slide1');
    slides[2].classList.add('slide-all');
    

    slides = [
        document.querySelector('.slide0'),
        document.querySelector('.slide1'),
        document.querySelector('.slide2')
    ];
}

document.querySelector('.next').addEventListener('click', nextSlide);

function prevSlide() {
    slides[0].classList.remove('slide0');
    slides[0].classList.add('slide1');
    slides[0].classList.add('slide-all');

    slides[1].classList.remove('slide1');
    slides[1].classList.add('slide2');
    slides[1].classList.add('slide-all');

    slides[2].classList.remove('slide2');
    slides[2].classList.add('slide0');
    slides[2].classList.add('slide-all');

    slides = [
        document.querySelector('.slide0'),
        document.querySelector('.slide1'),
        document.querySelector('.slide2')
    ];
}

document.querySelector('.prev').addEventListener('click', prevSlide);
