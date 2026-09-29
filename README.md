<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=0:ff00cc,50:6a00ff,100:00e5ff&height=220&section=header&text=Cat%C3%A1logo%20&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Python%20%C2%B7%20MongoDB%20%C2%B7%20Terminal&descAlignY=58&descSize=18)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00E5FF&center=true&vCenter=true&width=620&lines=Cat%C3%A1logo+de+m%C3%BAsicas+no+terminal;Python+%2B+MongoDB;CRUD+completo+com+anima%C3%A7%C3%B5es;Projeto+de+estudo+de+banco+de+dados)](https://github.com/nyxaev)

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-CLI-1a1a2e?style=for-the-badge&logo=gnubash&logoColor=white)
![Status](https://img.shields.io/badge/Status-Projeto%20de%20estudo-ff00cc?style=for-the-badge)

</div>

---

> ⚠️ **Projeto de estudo.** Criado só para treinar banco de dados (MongoDB) e o CRUD básico. Não é um sistema pronto para produção.

## 🎛️ O que é

Um catálogo de músicas que roda no terminal. Cada música vira um documento no MongoDB, e tudo é salvo na hora: fechou o programa e abriu de novo, as músicas continuam lá.

## 🖥️ Preview

```

  ╔══════════════ MENU ══════════════╗
  ║  1  Adicionar música             ║
  ║  2  Listar músicas               ║
  ║  3  Buscar por artista           ║
  ║  4  Atualizar música             ║
  ║  5  Remover música               ║
  ║  0  Sair                         ║
  ╚══════════════════════════════════╝
```

## 📦 Requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [MongoDB Community Server](https://www.mongodb.com/try/download/community) rodando em `localhost:27017`
- (Opcional) [MongoDB Compass](https://www.mongodb.com/products/tools/compass) para visualizar os dados

## 🚀 Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/nyxaev/NOME-DO-REPOSITORIO.git
cd NOME-DO-REPOSITORIO
```

**2. Instale a dependência**
```bash
pip install pymongo
```

**3. Ligue o MongoDB** (por padrão em `mongodb://localhost:27017`)

**4. Execute**
```bash
python catalogo_techno_v2.py
```

> 💡 No PyCharm, marque **Emulate terminal in output console** em `Run > Edit Configurations` para a tela limpar e as animações funcionarem direito.

O banco `catalogo_techno` e a collection `musicas` são criados sozinhos na primeira música adicionada.

## 🗂️ Estrutura dos dados

```json
{
  "_id": "ObjectId(...)",
  "titulo": "Spastik",
  "artista": "Plastikman",
  "bpm": 130,
  "ano": 1993,
  "subgenero": "minimal"
}
```

O campo `_id` é gerado pelo próprio MongoDB.

## 🔎 Conferindo os dados

**Pelo Compass:** conecte em `localhost:27017`, abra o banco `catalogo_techno` e a collection `musicas`.

**Pelo terminal:**
```bash
mongosh
use catalogo_techno
db.musicas.find()
```

## 🛣️ Ideias para evoluir

- [ ] Filtrar por subgênero
- [ ] Filtrar por faixa de BPM
- [ ] Impedir músicas duplicadas
- [ ] Contar músicas por subgênero
- [ ] Versão em Kotlin para comparar com a de Python

---

<div align="center">

Feito por **Isaac** · [@nyxaev](https://github.com/nyxaev) · 🎧

![footer](https://capsule-render.vercel.app/api?type=waving&color=0:00e5ff,50:6a00ff,100:ff00cc&height=120&section=footer)

</div>

