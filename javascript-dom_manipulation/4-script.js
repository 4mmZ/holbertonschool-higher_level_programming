document.getElementById("add_item").addEventListener("click", function() {
    var newItem = document.createElement("li");
    newItem.appendChild(document.createTextNode("Item"));
  
    var myList = document.querySelector(".my_list");
    myList.appendChild(newItem);
  });
  