console.log("Console of Code to Diagram");

// let btUpload = document.getElementById("upload");
// console.log(btUpload);
// btUpload.onClick = () => {};

// let btConvert = document.getElementById("convert");
// console.log(btConvert);
// btConvert.onClick = () => {};

// let btDownload = document.getElementById("download");
// console.log(btDownload);
// btUpload.onClick = () => {};


let input = document.querySelector('input')
 
let textarea = document.querySelector('textarea')

let typeFileSelect = document.getElementById('type_file')

let srcImg = document.getElementById('image')

input.addEventListener('change', () => {
    let files = input.files;
 
    if (files.length == 0) return;
 
    const file = files[0];

    let extensionFile = ((file.name).split(".")).pop();

    typeFileSelect.value = extensionFile
 
    let reader = new FileReader();
 
    reader.onload = (e) => {
        const file = e.target.result;
 
        // This is a regular expression to identify carriage
        // Returns and line breaks
        const lines = file.split(/\r\n|\n/);
        textarea.value = lines.join('\n');
 
    };
 
    reader.onerror = (e) => alert(e.target.error.name);

    reader.readAsText(file);
});

function downloadImage() {
    let data = srcImg.src;
    var a = document.createElement("a"); //Create <a>
    a.href = data //Image Base64 Goes here
    a.download = "Image.png"; //File name Here
    a.click(); //Downloaded file
};
