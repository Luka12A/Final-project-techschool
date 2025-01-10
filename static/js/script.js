const backBtn = document.getElementById("backBtn");
const nextBtn = document.getElementById("nextBtn");
const carouselInner = document.querySelector(".carousel-inner");
const items = document.querySelectorAll(".carousel-item");
const itemsPerRow = 3;
let currentIndex = 0;

const updateCarousel = () => {
  const itemWidth = items[0].offsetWidth;
  carouselInner.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
};

nextBtn.addEventListener("click", () => {
  if (currentIndex < items.length - itemsPerRow) {
    currentIndex += itemsPerRow;
    updateCarousel();
  }
});

backBtn.addEventListener("click", () => {
  if (currentIndex > 0) {
    currentIndex -= itemsPerRow;
    updateCarousel();
  }
});

updateCarousel();
