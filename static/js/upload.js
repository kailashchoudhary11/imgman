const inputImg = document.getElementById("id_img");

inputImg.onchange = (e) => {
  const [file] = e.target.files
  const fileName = file.name;
  setFileNameValue(fileName);

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
  setFileNameValue(fileName);
  setFile(file);
}

function setFileNameValue(newName) {
  const inputUI = document.getElementById("input_ui");
  inputUI.innerText = `${newName}`
  inputUI.className = "text-danger"
}

function setFile(newFile) {
  console.info(newFile);
  const hiddenInput = document.getElementById("id_img");
  const dataTransfer = new DataTransfer();
  dataTransfer.items.add(new File([newFile], newFile.name));
  hiddenInput.files = dataTransfer.files;
}