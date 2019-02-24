var socket;

function addRow(course, i) {
    if (!document.getElementsByTagName) return;
    body = document.getElementsByTagName("tbody")[i];
    row = document.createElement("tr");
    courseNumber = document.createElement("td");
    courseName = document.createElement("td");
    creditHours = document.createElement("td");

    textnode1 = document.createTextNode(course["c"]);
    textnode2 = document.createTextNode(course["b"]);
    textnode3 = document.createTextNode(course["a"]);

    courseNumber.appendChild(textnode1);
    courseName.appendChild(textnode2);
    creditHours.appendChild(textnode3);

    row.appendChild(courseNumber);
    row.appendChild(courseName);
    row.appendChild(creditHours);

    body.appendChild(row);
}

function addTable(minor) {
    if (!document.getElementsByTagName) return;
    table = document.createElement("table");
    head = document.createElement("thead");
    body = document.createElement("tbody");
    head.classList.add("thead-light");
    table.classList.add("table");
    row = document.createElement("tr");

    courseNumber = document.createElement("th");
    courseName = document.createElement("th");
    creditHours = document.createElement("th");

    textnode1 = document.createTextNode("Course Number");
    textnode2 = document.createTextNode("Course Name");
    textnode3 = document.createTextNode("Credit Hours");

    courseNumber.appendChild(textnode1);
    courseName.appendChild(textnode2);
    creditHours.appendChild(textnode3);

    row.appendChild(courseNumber);
    row.appendChild(courseName);
    row.appendChild(creditHours);

    head.appendChild(row);

    table.appendChild(head);
    table.appendChild(body);

    title = document.createElement("h2");
    subtitle = document.createElement("h2");
    textnode3 = document.createTextNode(minor["name"]);
    textnode4 = document.createTextNode("Hours Left: " + minor["hoursLeft"]);

    title.appendChild(textnode3);
    subtitle.appendChild(textnode4);

    
    wrapper = document.getElementById("minors");
    wrapper.appendChild(title);
    wrapper.appendChild(subtitle);
    wrapper.appendChild(table);
}

$(document).ready(function () {
    socket = io.connect('http://127.0.0.1:5000/');

    socket.emit('ready');

    var btns = document.getElementsByClassName("btn");
    for (var i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function () {
            var current = document.getElementsByClassName("active");
            if (this.classList.contains("active"))
                this.classList.remove("active")
            else
                this.classList.add("active");
        });
    }


    socket.on('minors', function(minors) {
        for (var i = 0; i < minors.length; i++) {
            var minor = minors[i];
            addTable(minor);
            for (var j = 0; j < minor["courses"].length; j++) {
                addRow(minor["courses"][j], i);
            }
        }
    });
});