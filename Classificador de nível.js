const heroi = "Anônimo"
let experiencia = 5000

if (experiencia <= 1000) {
    console.log("O herói "+ heroi+ " está no nível Ferro")
} else if (experiencia <= 2000) {
    console.log("O herói "+ heroi+ " está no nível Bronze")
} else if (experiencia <= 5000) {
    console.log("O herói "+ heroi+ " está no nível Prata")
} else if (experiencia <= 7000) {
    console.log("O herói "+ heroi+ " está no nível Ouro")
} else if (experiencia <= 8000) {
    console.log("O herói "+ heroi+ " está no nível Platina")
} else if (experiencia <= 9000) {
    console.log("O herói "+ heroi+ " está no nível Ascendente")
} else if (experiencia <= 10000) {
    console.log("O herói "+ heroi+ " está no nível Imortal")
} else if (experiencia > 10000) {
    console.log("O herói "+ heroi+ " está no nível Radiante")
}
