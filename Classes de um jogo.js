class personagem {
    constructor (nome, idade, tipo) {
        this.nome = nome,
        this.idade = idade,
        this.tipo = tipo
    }


    ataque (tipo) {
        if (tipo === "mago"){
            return "usando magia"
        } else if (tipo === "guerreiro") {
            return("usando espada")
        } else if (tipo === "monge") {
            return "usando artes marciais"
        } else if (tipo === "ninja") {
            return "usando shuriken"
        }
    }
}

let char = new personagem("Jonpierre", 25, "guerreiro")
console.log(`O ${char.tipo} atacou ${char.ataque(char.tipo)}`)
