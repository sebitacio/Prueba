// const image_input = document.getElementById('front-input');
const image_inputs = document.getElementsByClassName('photo-input')

Array.from(image_inputs).forEach(image_input => {
  image_input.addEventListener("change", function () {
    var upload_image;
    var output = document.querySelector(`#${this.id} + div`)
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      upload_image = reader.result;
      output.style.backgroundImage = `url(${upload_image})`
    })
    reader.readAsDataURL(this.files[0])
  })
});