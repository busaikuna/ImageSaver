document.addEventListener('DOMContentLoaded', function() {
    const divs = document.querySelectorAll(".image");
    const full = document.querySelector(".full");
    let currentIndex = 0;

    divs.forEach((div, index) => {
        div.addEventListener("click", () => {
            let imagem = div.querySelector("img");

            if (imagem) {
                currentIndex = index;
                showFullscreenImage(imagem.src, div);
                this.body.style.overflow = "hidden"
            }
        });
    });

    document.addEventListener('keydown', (e)=> {
        switch (e.key){
            case "ArrowLeft":
                currentIndex = (currentIndex === 0) ? divs.length - 1 : currentIndex - 1;
                showFullscreenImage(divs[currentIndex].querySelector("img").src, divs[currentIndex]);
                this.body.style.overflow = "hidden"
                break;
            case "ArrowRight":
                currentIndex = (currentIndex === divs.length - 1) ? 0 : currentIndex + 1;
                showFullscreenImage(divs[currentIndex].querySelector("img").src, divs[currentIndex]);
                this.body.style.overflow = "hidden"
                break;
            case "Escape":
                full.style.display = "none";
                this.body.style.overflowY = "auto"
                break;
        }
    });

    function showFullscreenImage(src, originalDiv) {
        full.style.display = "flex";
        full.innerHTML = "";

        let imageFull = document.createElement("div");
        imageFull.classList.add("image-full");

        let imgFullscreen = document.createElement("img");
        imgFullscreen.src = src;

        let divTexts = document.createElement("div");

        let legend = originalDiv.querySelector(".legend");
        if (legend) {
            let pLegend = document.createElement("p");
            pLegend.classList.add("legend");
            pLegend.textContent = legend.textContent;
            divTexts.appendChild(pLegend);
        }

        let date = originalDiv.querySelector(".date");
        if (date) {
            let pDate = document.createElement("p");
            pDate.classList.add("date");
            pDate.textContent = date.textContent;
            divTexts.appendChild(pDate);
        }

        imageFull.appendChild(imgFullscreen);
        imageFull.appendChild(divTexts);
        full.appendChild(imageFull);
    }
});
