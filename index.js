console.log("js was hir")
fetch("list.json").then(json => json.json()).then((reponse) =>{
    reponse.forEach((product)=>{
        products_div = document.getElementById("products")
        div = document.createElement("div")
        div.className = "product"
        imageP = document.createElement("img")
        imageP.src = product[1]
        imageP.alt = "l'image de " + product[0]
        nameP = document.createElement("h2")
        nameP.textContent = product[0]
        div.appendChild(imageP)
        div.appendChild(nameP)
        products_div.appendChild(div)
    })}
)

