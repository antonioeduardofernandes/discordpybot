from pysondb import db
database = db.getDb("database.json")

database.addMany([
{
  "nome": "John Taylor Cambridge",
  "jogador": "470765383868219403",
  "img":"https://m.media-amazon.com/images/I/51EMRSQ030L.jpg",
  "natureza": "rebelde",
  "comportamento": "solitário",
  "essencia": "investigador",
  "tradicao": "vazio",
  "arete": 3,
  "vontade": {"permanente":5, "temporario":5},
  "quintessencia": 3,
  "paradoxo": 0,
  "antecedentes": [
    {"label":"arcanum", "valor":3}, 
    {"label":"avatar","valor":3}, 
    {"label":"recursos", "valor":1}, 
    {"label":"sonho", "valor":1}
  ],
  "atributos": {
    "físicos":[ 
      {"label":"força", "valor": 2, "especializacao": "" },
      {"label":"destreza", "valor": 2, "especializacao": "" },
      {"label":"vigor", "valor": 2, "especializacao": "" }
    ],
    "sociais":[ 
      {"label":"carisma", "valor": 4, "especializacao": "" },
      {"label":"manipulação", "valor": 3, "especializacao": "" },
      {"label":"aparência", "valor": 3, "especializacao": "" }
    ],
    "mentais":[ 
      {"label":"inteligência", "valor": 3, "especializacao": "" },
      {"label":"percepção", "valor": 3, "especializacao": "" },
      {"label":"raciocínio", "valor": 2, "especializacao": "" }
    ],
  },
  "habilidades": {
    "talentos": [
       {"label": "prontidao","valor": 1, "especializacao": "" },
       {"label": "esportes", "valor": 1, "especializacao": "" },
       {"label": "consciência","valor": 3, "especializacao": "" },
       {"label": "briga", "valor": 1, "especializacao": "" },
       {"label": "esquiva","valor": 2, "especializacao": "" },
       {"label": "expressão", "valor": 1, "especializacao": "" },
       {"label": "intimidação","valor": 0, "especializacao": "" },
       {"label": "liderança", "valor": 0, "especializacao": "" },
       {"label": "manha","valor": 1, "especializacao": "" },
       {"label": "lábia", "valor": 1, "especializacao": "" },
    ],
    "perícias": [
       {"label": "ofícios","valor": 0, "especializacao": "" },
       {"label": "condução", "valor": 0, "especializacao": "" },
       {"label": "etiqueta","valor": 0, "especializacao": "" },
       {"label": "armas de fogo", "valor": 0, "especializacao": "" },
       {"label": "meditação","valor": 3, "especializacao": "" },
       {"label": "armas brancas", "valor": 1, "especializacao": "" },
       {"label": "atuação","valor": 0, "especializacao": "" },
       {"label": "furtividade", "valor": 1, "especializacao": "" },
       {"label": "sobrevivência","valor": 1, "especializacao": "" },
       {"label": "tecnologia", "valor": 0, "especializacao": "" },
    ],
    "conhecimentos": [
       {"label": "acadêmicos","valor": 3, "especializacao": "" },
       {"label": "computador", "valor": 1, "especializacao": "" },
       {"label": "cosmologia","valor": 3, "especializacao": "" },
       {"label": "enigmas", "valor": 2, "especializacao": "" },
       {"label": "investigação","valor": 1, "especializacao": "" },
       {"label": "direito", "valor": 0, "especializacao": "" },
       {"label": "linguística","valor": 2, "especializacao": "" },
       {"label": "medicina", "valor": 1, "especializacao": "" },
       {"label": "ocultismo","valor": 2, "especializacao": "" },
       {"label": "ciências", "valor": 1, "especializacao": "" },
    ],
  },
  "esferas": [
    {"label":"correspondência", "valor": 1, "especializacao": "" },
    {"label":"entropia", "valor": 0, "especializacao": "" },
    {"label":"forças" ,"valor": 1, "especializacao": "" },
    {"label":"vida" ,"valor": 1, "especializacao": "" },
    {"label":"mente" ,"valor": 2, "especializacao": "" },
    {"label":"matéria" ,"valor": 0, "especializacao": "" },
    {"label":"primórdio" ,"valor": 0, "especializacao": "" },
    {"label":"espírito" ,"valor": 2, "especializacao": "" },
    {"label":"tempo" ,"valor": 0, "especializacao": ""}
  ]
},
{
  "nome": "Leone",
  "jogador": "387372272849256459",
  "img":"https://vandal-us.s3.amazonaws.com/spree/products/81226/original/open-uri20180820-270-vn9epy.jpg",
  "natureza": "mártir",
  "comportamento": "sobrevivente",
  "essencia": "padrão",
  "tradicao": "eutanatos",
  "arete": 3,
  "vontade": {"permanente":10, "temporario":10},
  "quintessencia": 2,
  "paradoxo": 0,
  "antecedentes": [
    {"label":"arcanum", "valor":5}, 
    {"label":"avatar","valor":2}, 
  ],
  "atributos": {
    "físicos":[ 
      {"label":"força", "valor": 3, "especializacao": "" },
      {"label":"destreza", "valor": 4, "especializacao": "" },
      {"label":"vigor", "valor": 3, "especializacao": "" }
    ],
    "sociais":[ 
      {"label":"carisma", "valor": 2, "especializacao": "" },
      {"label":"manipulação", "valor": 2, "especializacao": "" },
      {"label":"aparência", "valor": 2, "especializacao": "" }
    ],
    "mentais":[ 
      {"label":"inteligência", "valor": 3, "especializacao": "" },
      {"label":"percepção", "valor": 2, "especializacao": "" },
      {"label":"raciocínio", "valor": 3, "especializacao": "" }
    ],
  },
  "habilidades": {
    "talentos": [
       {"label": "prontidao","valor": 3, "especializacao": "" },
       {"label": "esportes", "valor": 3, "especializacao": "" },
       {"label": "consciência","valor": 0, "especializacao": "" },
       {"label": "briga", "valor": 3, "especializacao": "" },
       {"label": "esquiva","valor": 3, "especializacao": "" },
       {"label": "expressão", "valor": 0, "especializacao": "" },
       {"label": "intimidação","valor": 1, "especializacao": "" },
       {"label": "liderança", "valor": 0, "especializacao": "" },
       {"label": "manha","valor": 0, "especializacao": "" },
       {"label": "lábia", "valor": 0, "especializacao": "" },
    ],
    "perícias": [
       {"label": "ofícios","valor": 0, "especializacao": "" },
       {"label": "condução", "valor": 0, "especializacao": "" },
       {"label": "etiqueta","valor": 0, "especializacao": "" },
       {"label": "armas de fogo", "valor": 4, "especializacao": "armas brancas" },
       {"label": "meditação","valor": 0, "especializacao": "" },
       {"label": "armas brancas", "valor": 3, "especializacao": "" },
       {"label": "atuação","valor": 0, "especializacao": "" },
       {"label": "furtividade", "valor": 3, "especializacao": "" },
       {"label": "sobrevivência","valor": 0, "especializacao": "" },
       {"label": "tecnologia", "valor": 0, "especializacao": "" },
    ],
    "conhecimentos": [
       {"label": "acadêmicos","valor": 0, "especializacao": "" },
       {"label": "computador", "valor": 0, "especializacao": "" },
       {"label": "cosmologia","valor": 0, "especializacao": "" },
       {"label": "enigmas", "valor": 1, "especializacao": "" },
       {"label": "investigação","valor": 2, "especializacao": "" },
       {"label": "direito", "valor": 0, "especializacao": "" },
       {"label": "linguística","valor": 0, "especializacao": "" },
       {"label": "medicina", "valor": 0, "especializacao": "" },
       {"label": "ocultismo","valor": 2, "especializacao": "" },
       {"label": "ciências", "valor": 0, "especializacao": "" },
    ],
  },
  "esferas": [
    {"label":"correspondência", "valor": 1, "especializacao": "" },
    {"label":"entropia", "valor": 2, "especializacao": "" },
    {"label":"forças" ,"valor": 1, "especializacao": "" },
    {"label":"vida" ,"valor": 0, "especializacao": "" },
    {"label":"mente" ,"valor": 0, "especializacao": "" },
    {"label":"matéria" ,"valor": 0, "especializacao": "" },
    {"label":"primórdio" ,"valor": 2, "especializacao": "" },
    {"label":"espírito" ,"valor": 0, "especializacao": "" },
    {"label":"tempo" ,"valor": 0, "especializacao": ""}
  ]
},
{
  "nome": "Eddy (Edward) Steverson",
  "jogador": "468216325492310037",
  "img":"https://m.media-amazon.com/images/I/51EMRSQ030L.jpg",
  "natureza": "solitário",
  "comportamento": "excêntrico",
  "essencia": "padrão",
  "tradicao": "vazio",
  "arete": 3,
  "vontade": {"permanente":5, "temporario":5},
  "quintessencia": 2,
  "paradoxo": 0,
  "antecedentes": [
    {"label":"arcanum", "valor":1}, 
    {"label":"avatar","valor":2}, 
    {"label":"biblioteca","valor":1}, 
    {"label":"contatos","valor":2}, 
    {"label":"sonho","valor":1}, 
  ],
  "atributos": {
    "físicos":[ 
      {"label":"força", "valor": 1, "especializacao": "" },
      {"label":"destreza", "valor": 3, "especializacao": "" },
      {"label":"vigor", "valor": 2, "especializacao": "" }
    ],
    "sociais":[ 
      {"label":"carisma", "valor": 4, "especializacao": "eloquência" },
      {"label":"manipulação", "valor": 4, "especializacao": "persuasão" },
      {"label":"aparência", "valor": 2, "especializacao": "" }
    ],
    "mentais":[ 
      {"label":"inteligência", "valor": 2, "especializacao": "" },
      {"label":"percepção", "valor": 3, "especializacao": "" },
      {"label":"raciocínio", "valor": 3, "especializacao": "" }
    ],
  },
  "habilidades": {
    "talentos": [
       {"label": "prontidao","valor": 1, "especializacao": "" },
       {"label": "esportes", "valor": 0, "especializacao": "" },
       {"label": "consciência","valor": 2, "especializacao": "" },
       {"label": "briga", "valor": 0, "especializacao": "" },
       {"label": "esquiva","valor": 0, "especializacao": "" },
       {"label": "expressão", "valor": 1, "especializacao": "" },
       {"label": "intimidação","valor": 2, "especializacao": "" },
       {"label": "liderança", "valor": 1, "especializacao": "" },
       {"label": "manha","valor": 3, "especializacao": "" },
       {"label": "lábia", "valor": 3, "especializacao": "" },
    ],
    "perícias": [
       {"label": "ofícios","valor": 1, "especializacao": "" },
       {"label": "condução", "valor": 1, "especializacao": "" },
       {"label": "etiqueta","valor": 0, "especializacao": "" },
       {"label": "armas de fogo", "valor": 0, "especializacao": "" },
       {"label": "meditação","valor": 1, "especializacao": "" },
       {"label": "armas brancas", "valor": 1, "especializacao": "" },
       {"label": "atuação","valor": 1, "especializacao": "" },
       {"label": "furtividade", "valor": 2, "especializacao": "" },
       {"label": "sobrevivência","valor": 1, "especializacao": "" },
       {"label": "tecnologia", "valor": 1, "especializacao": "" },
    ],
    "conhecimentos": [
       {"label": "acadêmicos","valor": 0, "especializacao": "" },
       {"label": "computador", "valor": 0, "especializacao": "" },
       {"label": "cosmologia","valor": 1, "especializacao": "" },
       {"label": "enigmas", "valor": 1, "especializacao": "" },
       {"label": "investigação","valor": 1, "especializacao": "" },
       {"label": "direito", "valor": 0, "especializacao": "" },
       {"label": "linguística","valor": 0, "especializacao": "" },
       {"label": "medicina", "valor": 0, "especializacao": "" },
       {"label": "ocultismo","valor": 1, "especializacao": "" },
       {"label": "ciências", "valor": 1, "especializacao": "" },
    ],
  },
  "esferas": [
    {"label":"correspondência", "valor": 1, "especializacao": "" },
    {"label":"entropia", "valor": 1, "especializacao": "" },
    {"label":"forças" ,"valor": 1, "especializacao": "" },
    {"label":"vida" ,"valor": 0, "especializacao": "" },
    {"label":"mente" ,"valor": 2, "especializacao": "" },
    {"label":"matéria" ,"valor": 1, "especializacao": "" },
    {"label":"primórdio" ,"valor": 0, "especializacao": "" },
    {"label":"espírito" ,"valor": 1, "especializacao": "" },
    {"label":"tempo" ,"valor": 0, "especializacao": ""}
  ]
}
])