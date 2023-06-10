const body = document.querySelector("body"),
    nav = document.querySelector("nav"),
    modeToggle = document.querySelector(".dark-light"),
    searchButton = document.querySelector(".search-button"),
    sidebarOpen = document.querySelector(".sidebarOpen"),
    siderbarClose = document.querySelector(".siderbarClose");

let getMode = localStorage.getItem("mode");
if (getMode && getMode === "dark-mode") {
    body.classList.add("dark");
}

// js код для переключения темного и светлого режима
modeToggle.addEventListener("click", () => {
    modeToggle.classList.toggle("cedsamun");
    body.classList.toggle("dark");

    // js код, чтобы сохранить выбранный пользователем режим даже при обновлении страницы или повторном открытии файла
    if (!body.classList.contains("dark")) {
        localStorage.setItem("mode", "light-mode");
    } else {
        localStorage.setItem("mode", "dark-mode");
    }
});

// js код для переключения окна поиска
searchButton.addEventListener("click", () => {
    searchButton.classList.toggle("cedsamun");
});


// js код для переключения боковой панели
sidebarOpen.addEventListener("click", () => {
    nav.classList.add("cedsamun");
});

body.addEventListener("click", e => {
    let clickedElm = e.target;

    if (!clickedElm.classList.contains("sidebarOpen") && !clickedElm.classList.contains("menu")) {
        nav.classList.remove("cedsamun");
    }
});