function rank (pontos) {
    let elo
    if (pontos <= 10) {
        elo = "Ferro"
        return elo
    } else if (pontos <= 20) {
        elo = "Bronze"
        return elo
    } else if (pontos <= 50) {
        elo = "Prata"
        return elo
    } else if (pontos <= 80) {
        elo = "Ouro"
        return elo
    } else if (pontos <= 90) {
        elo = "Diamante"
        return elo
    } else if (pontos <= 100) {
        elo = "Lendário"
        return elo
    } else if (pontos > 100) {
        elo = "Imortal"
        return elo
    } 
}
let vitorias = 200
let derrotas = 2
const pontuacao = vitorias - derrotas
console.log(`O herói tem um saldo de ${vitorias - derrotas} e está no nível ${rank (pontuacao)}`)
