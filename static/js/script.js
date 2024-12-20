let scrollContainer = document.querySelector(".carousel");
let backBtn = document.getElementById("backBtn");
let nextBtn = document.getElementById("nextBtn");

nextBtn.addEventListener("click", () => {
  scrollContainer.scrollLeft += 900;
});

backBtn.addEventListener("click", () => {
  scrollContainer.scrollLeft -= 900;
});
