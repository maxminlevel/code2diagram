console.log("Console of Code to Diagram");

let uploadBtn = document.querySelector("input");

let textarea = document.querySelector("textarea");

let typeFileSelect = document.getElementById("type_file");

let srcImg = document.getElementById("image");

let contentTextArea = document.getElementById("contentTextArea");

uploadBtn.addEventListener("change", () => {
  let files = uploadBtn.files;

  if (files.length == 0) return;

  const file = files[0];

  let extensionFile = file.name.split(".").pop();

  typeFileSelect.value = extensionFile;

  let reader = new FileReader();

  reader.onload = (e) => {
    const file = e.target.result;

    // This is a regular expression to identify carriage
    // Returns and line breaks
    // const lines = file.split(/\r\n|\n/);
    // textarea.value = lines.join("\n");
    textarea.value = file;
  };

  reader.onerror = (e) => alert(e.target.error.name);

  reader.readAsText(file);
});

function downloadImage() {
  let data = srcImg.src;
  var a = document.createElement("a"); //Create <a>
  a.href = data; //Image Base64 Goes here
  a.download = "Image.png"; //File name Here
  a.click(); //Downloaded file
}

function convert() {
  let type = typeFileSelect.value;
  let data = contentTextArea.value.split(/\r\n|\n/);
  let message = { type, data };

  fetch("/convert", {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(message),
  })
    .then(function (response) {
      if (response.ok) {
        response.json().then(function (response) {
          console.log(response);
          let image = response.image;
          srcImg.src = image;
        });
      } else {
        throw Error("Something went wrong");
      }
    })
    .catch(function (error) {
      console.log(error);
    });
}
