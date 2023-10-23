const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry.boundingClientRect);
        if (entry.isIntersecting) {
            entry.tartget.classlist.add("show");
            console.log("show");
        }
    });
});

const hiddenElements = document.querySelectorAll("path");
hiddenElements.forEach((el) => observer.observe(el));

