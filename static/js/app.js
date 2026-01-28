const blobs = document.querySelectorAll(".bg-blobs span");

document.addEventListener("mousemove", (e) => {
  blobs.forEach((blob, index) => {
    const speed = (index + 1) * 0.02;
    blob.style.transform = `
      translate(${e.clientX * speed}px, ${e.clientY * speed}px)
    `;
  });
});

// Mobile touch support
document.addEventListener("touchmove", (e) => {
  const touch = e.touches[0];
  blobs.forEach((blob, index) => {
    const speed = (index + 1) * 0.03;
    blob.style.transform = `
      translate(${touch.clientX * speed}px, ${touch.clientY * speed}px)
    `;
  });
});

function showResult() {
  document.getElementById("results").scrollIntoView({ behavior: "smooth" });
}
