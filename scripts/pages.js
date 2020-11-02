function go_back() {
    location.href = "../index.html"
}

function cycle(delta) {
    var res =  (id + delta + tot - 1) % tot + 1
    location.href = rjust(String(res), 3, '0') + ".html"
}

tot = image_list.length