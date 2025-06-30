class Inventario {
  constructor() {
    this.itens = [];
  }

  adicionarItem(nome, quantidade) {
    const existente = this.itens.find(item => item.nome === nome);
    if (existente) {
      existente.quantidade += quantidade;
    } else {
      this.itens.push({ nome, quantidade });
    }
  }

  removerItem(nome, quantidade) {
    const item = this.itens.find(i => i.nome === nome);
    if (item) {
      item.quantidade -= quantidade;
      if (item.quantidade <= 0) {
        this.itens = this.itens.filter(i => i.nome !== nome);
      }
    }
  }

  listarItens() {
    console.log("Inventário:");
    this.itens.forEach(item => {
      console.log(`${item.nome}: ${item.quantidade}`);
    });
  }
}

// Exemplo de uso
const meuInventario = new Inventario();
meuInventario.adicionarItem("Espada", 1);
meuInventario.adicionarItem("Poção", 3);
meuInventario.removerItem("Poção", 1);
meuInventario.listarItens();
