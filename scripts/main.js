function go() {
    location.href = "./pages/" + rjust(input_text.value, 3, '0') + ".html"
}

function go_random() {
    var min = 1
    var max = 127
    var chosen = Math.floor(Math.random() * (max - min + 1)) + min
    var res = rjust(String(chosen), 3, '0')
    location.href = "./pages/" + res + ".html"
}

function key_down(event) {
    if (event.keyCode === 13) {
        go()
    }
}