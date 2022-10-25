const inputImg = document.getElementById("id_img");

inputImg.onchange = (e) => {
  const [file] = e.target.files
  if (fileValidation(file)) {
    document.getElementById("upload_button").removeAttribute("disabled");
    setFileNameValue(file.name);
  } else {
    alert("Please only image files");
    document.getElementById("upload_button").setAttribute("disabled", "");
  }
}

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  const [file] = ev.dataTransfer.files;
  const fileName = file.name;
  ev.preventDefault();
    if (fileValidation(file)) {
      setFileNameValue(fileName);
      setFile(file);
    }else{
      alert("Please only image files")
    }
}

function setFileNameValue(newName) {
  const inputUI = document.getElementById("input_ui");
  inputUI.innerText = `${newName}`
  inputUI.className = "text-danger"
}

function setFile(newFile) {
  const hiddenInput = document.getElementById("id_img");
  const dataTransfer = new DataTransfer();
  dataTransfer.items.add(new File([newFile], newFile.name));
  hiddenInput.files = dataTransfer.files;
}

function fileValidation(file) {
  // Regexp to validate extention file! Only Images formats
  const validExtentionsRegex = /\.(jpe?g|png|gif|bmp)$/i;
  if (validExtentionsRegex.test(file.name)){
    return true
  } else {
    return false
  }
}