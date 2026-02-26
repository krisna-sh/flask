alert("hello world");
function endtheworld() {
  const mainTextElement = document.getElementById("main-text");
  if(mainTextElement.innerText === "By by world")
  {
    mainTextElement.innerText = "helloo world";
  }
  else
  {
    mainTextElement.innerText = "by by world";
  }
}